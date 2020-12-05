#!/usr/bin/env python
#!C:/Users/Vikas/AppData/Local/Programs/Python/Python36-32/python.exe
import psycopg2
import json
#from course import course,info_course
'''

connect_str = "dbname='timetable' user='postgres' host='localhost' " + \
                  "password='vskalagi'"
conn = psycopg2.connect(connect_str)
cursor = conn.cursor()'''
print("content-type: text/html\n\n")
print("<br>hello")
#in_id=input()
'''for i in info_course:
		for j in info_course[i]:
			u=j.split(":")
			cursor.execute('UPDATE takes set hour=%s where  course_id=%s ', [int(u[2]),int(u[0])])

	conn.commit()
conn.close()
'''
