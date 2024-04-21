import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Inventory_management"
)

mycursor = mydb.cursor()

sql = "Insert into inventory(Id, Name, Quantity, Category, Price, Location, Stock) values(%s,%s,%s,%s,%s,%s,%s)"
val =  ("05", "Orange Spinanch", "50 bunches", "Produce", "$2.49 per bunch", "Refrigerated Section, Produce Department", "20bunch-100bunch")



mycursor.execute(sql, val)
mydb.commit()
print("Data Inserted successfully.")
