#emp name,emp num,insert 10 value in table, and disp(table name= employee)
import mysql.connector


mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

mycursor = mydb.cursor()

# employee table
sql = "CREATE TABLE employee (emp_name VARCHAR(255), employee_id INT PRIMARY KEY, age INT)"
mycursor.execute(sql)

print("Employee table created successfully")
mydb.close()

