import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="sys"
)

mycursor = mydb.cursor()

# Student information
mycursor.execute("""
CREATE TABLE Student_Info (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  class VARCHAR(10),
  section VARCHAR(5)
)
""")

# Student marks
mycursor.execute("""
CREATE TABLE marks (
  student_id INT PRIMARY KEY,
  m1 INT,
  m2 INT,
  m3 INT,
  m4 INT,
  m5 INT
)
""")

mydb.commit()

print("Tables created successfully")
