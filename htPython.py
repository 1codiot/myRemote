#!/usr/bin/python
import MySQLdb
print("Content-Type: text/html")
print("")
print("<html><head><title>Books</title></head>")
print("<body>")
print("<h1>Books</h1>")
print("<ul>")

connection = MySQLdb.connect(user='root', passwd='Akash@112', db='DbmsLab')
cursor = connection.cursor()
cursor.execute("SELECT * FROM Student")

for row in cursor.fetchall():
  print("<li>%s</li>" % row[0])
  print("</ul>")
  print("</body></html>")

connection.close()