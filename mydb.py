#install mysql on your computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='d15fa51a'
)

#prepare a cursor object
cursorObject=dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE fabrico")

print("All done!")
