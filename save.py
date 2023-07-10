#save to the database
import pymysql
import mysql.connector
#define the connection
connection=pymysql.connect(host="localhost",user="root",password="",database="chep")
#define the column to save
name="Joan Chebet"
email="eve@gmail.com"
course="Arts and Music"
university="TUK"
# order_id="38"
# user_id="4"
# order_name="clothes"
# destination="Mombasa"
# #define the sql query
# sql="insert into orders(order_id,user_id,orde_name,destination) values(%s,%s,%s,%s)"
sql="insert into orders(name,email,course,universiy) values(%s,%s,%s,%s)"
# #create cursor- used to execute the sql query
cursor=connection.cursor()
#execute sql
#cursor.execute(sql,(order_id,user_id,order_name,destination))
cursor.execute(sql,(name,email,course,university))
# commit the changes to the database
connection.commit()
print("saved successfully")
#close the cursor
cursor.close()