import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="sys"
)
 
mycursor = mydb.cursor()

# Customer info
mycursor.execute(
  "CREATE TABLE Customers ("
  "  customer_id VARCHAR(20) PRIMARY KEY,"
  "  name VARCHAR(50),"
  "  address VARCHAR(100),"
  "  phone_number VARCHAR(20)"
  ")"
)

# accounts
mycursor.execute(
  "CREATE TABLE Accounts ("
  "  account_number VARCHAR(20) PRIMARY KEY,"
  "  account_type VARCHAR(20),"
  "  balance DECIMAL(10,2),"
  "  customer_id VARCHAR(20)"
  ")"
)

# transac
mycursor.execute(
  "CREATE TABLE Transactions ("
  "  transaction_id VARCHAR(36) PRIMARY KEY,"
  "  account_number VARCHAR(20),"
  "  amount DECIMAL(10,2)"
  ")"
)

mydb.commit()

print("Tables created successfully")
