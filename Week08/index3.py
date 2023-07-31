#!/usr/bin/env python3
import cgitb
import cgi

cgitb.enable()

print("Content-Type:text/html;charset=utf-8")
print()

import pymysql

my_con = pymysql.connect(db='studentinfo',user='root',passwd='Password@07',host='localhost')

c = my_con.cursor()

c.execute("Select * from student")
print("<html>")
print("<body>")
print("<table border=1>")
print("<tr>")
print("<td>")
print("Fullname")
print("</td>")
print("<td>")
print("Average")
print("</td>")
print("</tr")
#print( c.fetchall())
re =c.fetchall()
for r in re:
	print("<tr>")
	print("<td>")
	print(r[0])
	print("</td>")
	print("<td>")
	print(r[1])
	print("</td>")
	print("</tr>")
print("</table>")
print("</body>")
print("</html>")
#for re in r:
#print(re)

