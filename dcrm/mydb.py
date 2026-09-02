import mysql.connector

dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'dev',
        passwd = 'password123'

        )



cursorObject = dataBase.cursor()


curorObject.execute("CREATE DATABASE gooner")
print("All one !")

