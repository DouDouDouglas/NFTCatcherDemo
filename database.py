import mysql.connector
# from multiprocessing import cpu_count
# print(cpu_count()) 8

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="WEB3"
)

mycursor = mydb.cursor()

# contracts or transactions
def selectAll(table):
    mycursor.execute(f"select * from {table}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# insert information
def insertTx(minter_address,contract_address,gas,gasPrice,time):
    sql = "insert into transactions (minter_address,contract_address,gas,gasPrice,time) values (%s,%s,%s,%s,%s)"
    val = (minter_address,contract_address,gas,gasPrice,time)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")