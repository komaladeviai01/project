import mysql.connector
con=mysql.connector.connect(

    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_komathi"
)


print(con)
result=con.cursor()
result.execute("show tables")
result_show=result.fetchall()
for x in result_show:
    print(x)

result.execute("select * from std_info")
result_show=result.fetchall()
for x in result_show:
    print(x)



result.execute
result_show=result.fetchall()
for x in result_show:
   print(x)
result.execute("select * from std_info")
result_show=result.fetchall()
for x in result_show:
    print(x)
#result.execute("describe purchase")
#result_show=result.fetchall()
#for x in result_show :
 #   print(x)



