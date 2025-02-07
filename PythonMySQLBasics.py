import mysql.connector


#Connection to the DB hosted over loval server
db_conn = mysql.connector.connect(host='localhost',database='test_db',user='root',password='root')

#Checking the connection status.
print(db_conn.is_connected())

#Cursor object creation to execute the queries with streamlined connection.
cursor = db_conn.cursor()

#SQL Query to get all the data from Users table in test_db DB
cursor.execute("Select * FROM test_db.users")
#Fetch only the first row from the results
user_row = cursor.fetchone()
print(user_row[0:3])

#Fetch all the row from the results
user_rows = cursor.fetchall()
print(user_rows[1][0])

#SQL Query to get all the data from Orders table in test_db DB
cursor.execute("Select * FROM test_db.orders")
order_rows = cursor.fetchall()
print(order_rows)


#Get the total of order price of all the users.
cursor1 = db_conn.cursor()
cursor1.execute("Select * FROM test_db.orders")
rows = cursor.fetchall()
order_price = 0
#Iterates over the tables for order_price
for row in rows:
    order_price = order_price + row[3]
    print("Total Order Price: INR",order_price)

#Close the SQL Connection
db_conn.close()

