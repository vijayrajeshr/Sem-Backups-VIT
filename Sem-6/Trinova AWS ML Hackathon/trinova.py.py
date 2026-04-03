# ==============================================================================
# TEAM - TRINOVA
# ==============================================================================

# --- [0/10] Setup and Imports ---
print("--- [0/10] Loading necessary libraries ---")
import pandas as pd
import numpy as np
import re
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

# Machine Learning Libraries
import lightgbm as lgb
import optuna
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import Ridge
from scipy.sparse import hstack

# --- [1/10] Install Required Libraries ---
print("\n--- [1/10] Installing required libraries ---")
!pip install optuna lightgbm

# --- [2/10] Load Raw Data ---
print("\n--- [2/10] Loading raw data from CSV files ---")
try:
    train_df = pd.read_csv('dataset/train.csv')
    test_df = pd.read_csv('dataset/test.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("ERROR: Make sure 'train.csv' and 'test.csv' are in a 'dataset' folder.")
    exit()

# --- [3/10] Helper Function for Evaluation ---
def smape(y_true, y_pred):
    numerator = 2 * np.abs(y_pred - y_true)
    denominator = (np.abs(y_true) + np.abs(y_pred))
    return np.mean(numerator / (denominator + 1e-6)) * 100

# --- [4/10] Feature Engineering ---
print("\n--- [4/10] Engineering features from text and metadata ---")
train_df['log_price'] = np.log1p(train_df['price'])

def extract_metadata(df):
    df['quantity'] = df['catalog_content'].str.extract(r'(pack|case|pk|count) of (\d+)', flags=re.IGNORECASE)[1].fillna(1).astype(int)
    df['brand'] = df['catalog_content'].str.extract(r'brand\s*[:\-]?\s*([A-Za-z0-9]+)', expand=False).fillna('Unknown')
    df['clean_text'] = df['catalog_content'].str.lower().str.replace(r'[^a-z0-9\s]', ' ', regex=True).str.replace(r'\s+', ' ', regex=True).str.strip()
    df['text_length'] = df['clean_text'].apply(len)
    df['word_count'] = df['clean_text'].apply(lambda x: len(x.split()))
    df['quantity_log'] = np.log1p(df['quantity'])
    return df

train_df = extract_metadata(train_df)
test_df = extract_metadata(test_df)

# --- [5/10] Feature Encoding and Vectorization ---
print("\n--- [5/10] Encoding features and vectorizing text ---")
le = LabelEncoder()
all_brands = pd.concat([train_df['brand'], test_df['brand']]).astype(str).unique()
le.fit(all_brands)
train_df['brand_encoded'] = le.transform(train_df['brand'].astype(str))
test_df['brand_encoded'] = le.transform(test_df['brand'].astype(str))

tfidf = TfidfVectorizer(stop_words='english', max_features=20000, ngram_range=(1, 3))
X_text_train = tfidf.fit_transform(train_df['clean_text'])
X_text_test = tfidf.transform(test_df['clean_text'])

numeric_features = ['quantity_log', 'text_length', 'word_count', 'brand_encoded']
scaler = StandardScaler()
meta_features_train_scaled = scaler.fit_transform(train_df[numeric_features])
meta_features_test_scaled = scaler.transform(test_df[numeric_features])

X_train_final = hstack([X_text_train, meta_features_train_scaled]).tocsr()
X_test_final = hstack([X_text_test, meta_features_test_scaled]).tocsr()
y_train = train_df['log_price']
print(f"Final training data shape: {X_train_final.shape}")

# --- [6/10] Hyperparameter Tuning with Optuna ---
print("\n--- [6/10] Tuning LightGBM hyperparameters with Optuna ---")
def objective(trial):
    params = {
        'objective': 'regression_l1', 'metric': 'mae', 'n_estimators': 2000,
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.05),
        'num_leaves': trial.suggest_int('num_leaves', 20, 80),
        'feature_fraction': trial.suggest_float('feature_fraction', 0.7, 1.0),
        'bagging_fraction': trial.suggest_float('bagging_fraction', 0.7, 1.0),
        'lambda_l1': trial.suggest_float('lambda_l1', 0.1, 5.0),
        'lambda_l2': trial.suggest_float('lambda_l2', 0.1, 5.0),
        'min_child_samples': trial.suggest_int('min_child_samples', 20, 80),
        'seed': 42, 'n_jobs': -1, 'verbose': -1, 'boosting_type': 'gbdt',
    }
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    train_idx, val_idx = next(kf.split(X_train_final))
    X_train_fold, X_val_fold = X_train_final[train_idx], X_train_final[val_idx]
    y_train_fold, y_val_fold = y_train.iloc[train_idx], y_train.iloc[val_idx]
    
    model = lgb.LGBMRegressor(**params)
    model.fit(X_train_fold, y_train_fold, eval_set=[(X_val_fold, y_val_fold)], callbacks=[lgb.early_stopping(100, verbose=False)])
    
    preds_log = model.predict(X_val_fold)
    return smape(np.expm1(y_val_fold), np.expm1(preds_log))

study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=20, show_progress_bar=True)
best_lgbm_params = study.best_params
print(f"Best SMAPE from tuning: {study.best_value:.4f}")
print("Best hyperparameters found:", best_lgbm_params)

# --- [7/10] K-Fold Training of Base Models ---
print("\n--- [7/10] Training base models (LGBM & Ridge) using 5-Fold CV ---")
N_SPLITS = 5
kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=42)
oof_preds_lgbm = np.zeros(len(train_df)); test_preds_lgbm = np.zeros(len(test_df))
oof_preds_ridge = np.zeros(len(train_df)); test_preds_ridge = np.zeros(len(test_df))

final_lgbm_params = { 'objective': 'regression_l1', 'metric': 'mae', 'n_estimators': 4000, 'seed': 42, 'n_jobs': -1, 'verbose': -1, 'boosting_type': 'gbdt'}
final_lgbm_params.update(best_lgbm_params)

for fold, (train_idx, val_idx) in enumerate(tqdm(kf.split(X_train_final), total=N_SPLITS, desc="Training Base Models")):
    X_train_fold, X_val_fold = X_train_final[train_idx], X_train_final[val_idx]
    y_train_fold, y_val_fold = y_train.iloc[train_idx], y_train.iloc[val_idx]

    lgbm = lgb.LGBMRegressor(**final_lgbm_params)
    lgbm.fit(X_train_fold, y_train_fold, eval_set=[(X_val_fold, y_val_fold)], callbacks=[lgb.early_stopping(150, verbose=False)])
    oof_preds_lgbm[val_idx] = lgbm.predict(X_val_fold)
    test_preds_lgbm += lgbm.predict(X_test_final) / N_SPLITS

    ridge = Ridge(alpha=3.0, random_state=42)
    ridge.fit(X_train_fold, y_train_fold)
    oof_preds_ridge[val_idx] = ridge.predict(X_val_fold)
    test_preds_ridge += ridge.predict(X_test_final) / N_SPLITS

# --- [8/10] Evaluate Base Models (OOF) ---
print("\n--- [8/10] Evaluating OOF performance of base models ---")
y_true_price = np.expm1(y_train)
smape_lgbm_val = smape(y_true_price, np.expm1(oof_preds_lgbm))
smape_ridge_val = smape(y_true_price, np.expm1(oof_preds_ridge))
print(f"LGBM OOF SMAPE: {smape_lgbm_val:.4f}")
print(f"Ridge OOF SMAPE: {smape_ridge_val:.4f}")

# --- [9/10] Ensemble Stacking ---
print("\n--- [9/10] Training stacking meta-model ---")
X_meta_train = np.column_stack((oof_preds_lgbm, oof_preds_ridge))
X_meta_test = np.column_stack((test_preds_lgbm, test_preds_ridge))

meta_model = Ridge(alpha=1.0)
meta_model.fit(X_meta_train, y_train)
print("Stacking meta-model trained.")

# --- [10/10] Generate Final Predictions and Submission File ---
print("\n--- [10/10] Generating final predictions from meta-model ---")
final_log_preds = meta_model.predict(X_meta_test)
final_prices = np.expm1(final_log_preds)
final_prices[final_prices < 0] = 0 # Ensure no negative prices

submission_df = pd.DataFrame({'sample_id': test_df['sample_id'], 'price': final_prices})
submission_df.to_csv('test_out_2.csv', index=False)
print("\n✅✅✅ Submission file 'test_out_2.csv' created successfully! ✅✅✅")
print("Top 5 predictions:")
print(submission_df.head())