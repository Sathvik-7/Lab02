#!/usr/bin/env python3
# Turn on debug mode
import cgitb
import cgi

cgitb.enable()
form = cgi.FieldStorage()
fullname = form.getvalue("fullname") 

print('Content-Type:text/html;charset=utf-8')
print()

import pymysql

my_con = pymysql.connect(db='studentinfo',user='root',passwd='Password@07',host='localhost')
c = my_con.cursor()

delete_q = "delete from student where fullname = %s"

c.execute(delete_q,(fullname,))

my_con.commit()

print('Record deleted successfully')

c.close()
my_con.close()
