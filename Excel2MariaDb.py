
import mariadb

import openpyxl as xl

import pandas as pd


dbconn=mariadb.connect(

    user="",
    password="",
    host="",
    port=3306,
    database=""

)
cur=dbconn.cursor()
#cur.execute("select * from assets")
#result=cur.fetchall()

data=pd.read_excel("Excel_name.xlsx")
excelindex=data.index
boyut=len(excelindex)

sonuc=[]
for i in range(0,boyut):
    column1=data.loc[i][X]
    column2 = data.loc[i][Y]
    column3 = data.loc[i][Z]

    cur.execute("insert into assets (`db_column1`,`db_column2`,`db_column3`) values (%s,%s,%s)",(column1,column2,column3))


dbconn.commit()
