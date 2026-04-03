import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="sys"
)

mycursor = mydb.cursor()

# Insert data into Customers table
customer_data = [
  ("C001", "Vijay", "Indore, Madhya Pradesh", "9876543210")
]
sql = "INSERT INTO Customers (customer_id, name, address, phone_number) VALUES (%s, %s, %s, %s)"
mycursor.executemany(sql, customer_data)

mydb.commit()

print("Data inserted successfully")

# View Customers table
mycursor.execute("SELECT * FROM Customers")
result = mycursor.fetchall()

print("\nCustomers Table:")
for row in result:
  print(row)

mydb.close()
