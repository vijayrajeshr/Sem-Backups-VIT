#1------------------------------------
import pandas as pd
import numpy as np 

file = pd.read_csv("insurance.csv")
file.head(3)

#2------------------------------------
file.isnull().sum()
file.head(3)

#3------------------------------------
n_file = pd.get_dummies(file, drop_first=True)
n_file.head(3)

#4------------------------------------
x = n_file.drop('charges', axis=1)
y = n_file['charges']

#5------------------------------------
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#6------------------------------------
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train, y_train)

#7------------------------------------
y_pred = model.predict(x_test)

#8------------------------------------
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MSE : ", mse)
print("RMSE : ", rmse)
print("R2 Score : ", r2)

