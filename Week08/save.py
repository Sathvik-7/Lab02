#!/usr/bin/env python3
# Turn on debug mode
import cgitb
import cgi

cgitb.enable()
print("Content-Type:text/html;charset=utf-8")
print()

form = cgi.FieldStorage()
fullname = form.getvalue('fname')
mid1 = int(form.getvalue('midterm1'))
mid2 = int(form.getvalue('midterm2'))
mid3 = int(form.getvalue('midterm3'))
r = (mid1 + mid2 + (2 * mid3))//4

import pymysql

my_con = pymysql.connect(db='studentinfo',user='root',passwd='Password@07',host='localhost')
c = my_con.cursor()

c.execute("TRUNCATE student")

c.execute("INSERT INTO student(fullname,average) values(%s,%s)",(fullname,r))

my_con.commit()

c.close()
my_con.close()
