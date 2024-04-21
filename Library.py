import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Library_Management"
)

mycursor = mydb.cursor()

sql = "Insert into library1(Book_Id, Book_Name, Author, Genre, Publication_Year, Language, Copies_Available) values(%s,%s,%s,%s,%s,%s,%s)"
val =  ('', "Le Petit Prince", "Antoine de Saint-Exuper","Childern Literture", "1943","French","5")



mycursor.execute(sql, val)
mydb.commit()
print("Data Inserted successfully.")
