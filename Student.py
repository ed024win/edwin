import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student_management"
)

mycursor = mydb.cursor()

sql = "Insert into student(Student_Id, Name, Roll_Number, Address, Phone) values(%s,%s,%s,%s,%s)"
val =  ('', "Kaishap Thakuri", "5", "Darjeeling", "7757224567")



mycursor.execute(sql, val)
mydb.commit()
print("Data Inserted successfully.")
