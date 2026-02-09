import mysql.connector
from database_details import DatabaseDetails
db=DatabaseDetails()

#========================Table for new customer============================
mydb=mysql.connector.connect(host=db.host,user=db.user,password=db.password,database=db.database)
cur=mydb.cursor()
s1="CREATE TABLE customer1 (ref int primary key,name varchar(50),mother varchar(50),Gender varchar(50),Postcode varchar(50),mobile varchar(50),Email varchar(50),Nationality varchar(50),Idproof varchar(50),Idnumber varchar(50),Address varchar(50))"
cur.execute(s1)
#========================Table for new room availablity============================
s2="CREATE TABLE room1 (Contact VARCHAR(50) ,check_in VARCHAR(50) ,check_out VARCHAR(50) ,Room_type varchar(50)  ,room_available varchar(50) primary key ,Meal VARCHAR(50) ,Numberofdays VARCHAR(50))"
cur.execute(s2)
#========================Table for room details ============================
s3="CREATE TABLE room_data1 (Floor VARCHAR(50) NULL ,Roomno VARCHAR(50) PRIMARY KEY,Roomtype VARCHAR(50) NULL)"
cur.execute(s3)
#========================Table for new Login Page============================
s4="CREATE TABLE Login1 (First_name VARCHAR(50),Last_name VARCHAR(50),Password VARCHAR(50) ,Contact varchar(50) primary key,Username varchar(50),Gender VARCHAR(50),Country VARCHAR(50),Quetion VARCHAR(50),Answer VARCHAR(50))"
cur.execute(s4)




