import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Recepie_Management"
)

mycursor = mydb.cursor()

sql = "Insert into recepie(Recipe_Name, Number_Of_Instructions, Cook_Time, Difficulty, Category) values(%s,%s,%s,%s,%s)"
val = ("Mango Salsa", "7 Instructions", "15 minutes", "Easy", "Side Dish")

mycursor.execute(sql, val)
mydb.commit()
print("Data Inserted Successful")