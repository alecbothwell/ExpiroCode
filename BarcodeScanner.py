import csv
import mysql.connector
from MyQR import myqr

with open("BarcodeData.csv") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append(row)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="expirodb"
)

mycursor = mydb.cursor()
bcInfo = ""
for i in range(len(data)):
    sql = """SELECT prod_name FROM barcodemapping WHERE prod_id = %s"""
    mycursor.execute(sql, data[i])
    myresult = mycursor.fetchall()
    for x in myresult:
        bcInfo += str(x)

myqr.run(words=bcInfo, save_name = "test.png")