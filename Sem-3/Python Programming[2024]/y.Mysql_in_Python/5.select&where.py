import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="sys"
)

mycursor = mydb.cursor()

# Create table
mycursor.execute(
  "CREATE TABLE VIT_BHOPAL_SCHOOLS ("
  "  school_id INT AUTO_INCREMENT PRIMARY KEY,"
  "  school_name VARCHAR(100)"
  ")"
)

# Insert data
schools = [
  "School of Computing Science & Engineering (SCOPE)",
  "School of Biosciences, Engineering and Technology (SBET)",
  "School of Advanced Sciences & Languages (SASL)",
  "VIT Business School (BS)",
  "School of Mechanical Engineering (SME)",
  "School of Computing Science Engineering and Artificial Intelligence (SCAI)",
  "School of Architecture (SA)",
  "School of Electrical & Electronics Engineering (SEEE)"
]

for school in schools:
  sql = "INSERT INTO VIT_BHOPAL_SCHOOLS (school_name) VALUES (%s)"
  val = (school,)
  mycursor.execute(sql, val)

mydb.commit()

print("Table created and populated successfully")

# Check if SCSE school exists
sql = "SELECT * FROM VIT_BHOPAL_SCHOOLS WHERE school_name LIKE '%SCSE%'"
mycursor.execute(sql)

result = mycursor.fetchall()

if result:
  print("SCSE school found:")
  for row in result:
    print(row)
else:
  print("SCSE school not found")

mydb.close()
