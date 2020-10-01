from django.shortcuts import render
from sqlserverconnect.models import sqlserverconn
import pyodbc

def connsql(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-0S9HS02\SQLEXPRESS;'
                        'Database=cm;'
                        'Trusted_Connections=yes;')
    cursor=conn.cursor()
    cursor.execute("select * from Emprecords")
    result=cursor.fetchall()
    return render(request,'index.html',{'sqlserverconn':result})
