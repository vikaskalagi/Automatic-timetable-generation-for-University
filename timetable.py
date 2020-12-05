import psycopg2
import copy
import random
#from krishnarama import faculty_in_course
#from course import course
import json
from itertools import permutations
import csv
def listToDictionary( entry):
    return {entry[0:2]: list(entry[2:]) }

def jsonToList(dictionary, index):
    for key, value in dictionary.items():
        dictionary[key][index]= json.loads(value[index])
    return dictionary
connect_str = "dbname='timetable' user='postgres' host='localhost' " + \
                  "password='vskalagi'"
conn = psycopg2.connect(connect_str)
cursor = conn.cursor()
cursor.execute("(select * from section) ;")
result=cursor.fetchall()
year_section={}
pre_year_section={}
for i in result:
#	instructors = listToDictionary(cursor.fetchall())
	#print(i)
	instructors=listToDictionary(i)
	instructors = jsonToList(instructors, 0)
	year_section.update(instructors)
	pre_year_section.update(instructors)
#print(instructors[1][1][0][0])
#print(year_section[2,'a'])

cursor.execute("(select * from teacher) ;")
result=cursor.fetchall()
teacher_schedule={}
for i in result:
#	instructors = listToDictionary(cursor.fetchall())
	#print(i)
	instructors= {i[0]: list(i[2:]) }
	instructors = jsonToList(instructors, 0)
	teacher_schedule.update(instructors)
#two_hour=[7,16]
two_hour=[]
def remain_fun(stac,p,block_hour,track):
	teacher_on_mon={}
	#track={}
	
	last=[]
	loop=[]
	section_days={}
	block_hour_list=[]
	#print(year_section)
	#print(stac,"we")
	#print(year_section[(3,'a')],"df")
	for h in p:
		#print(stac[h][3],stac[h],lab_id)
		#if(stac[h][3] not in lab_id):
			#print(lo[3])
			#continue
			if(stac[h][2] not in block_hour):
				loop.append(stac[h])
			else:
				block_hour_list.append(stac[h])
	#print(block_hour_list,"sd",block_hour)
	lab_fun(block_hour_list,{})	
	#print(block_hour_list,"os",block_hour)		
	#print(year_section[(3,'b')])
	#print("abcd",loop,"hdfh\n")
	#print(loop,p,"fsd")
	#leng=len(loop)
	#loop=random.sample(loop,(len(loop)))
	for lo in loop:
		g=[0,1,2,3,4]
		random.shuffle(g)
		if(lo[1] not in section_days):
			section_days[lo[1]]=random.sample(g,5)
		#g=[0,4,3,1,2]
		#lo=random.choice(loop)
		#loop.remove(lo)
		i=lo[0]
		#print(lo)
		if(lo[1] not in track):
			track[lo[1]]={}

		if(lo[2] not in teacher_on_mon):
			teacher_on_mon[lo[2]]=0
		for ho in range(5):
			j=random.choice(g)
			#j=section_days[lo[1]][ho]
			#print(j,g)
			g.remove(j)
			if((j,lo[3]) not in track[lo[1]]):
				track[lo[1]][(j,lo[3])]=0	
			while(lo[4]>0 ):
				#print(lo[2] not in two_hour,track[lo[1]][(j,lo[3])])
				#print()
				#print(lo[2],teacher_schedule[lo[2]])
				#print()
				#print((i,lo[1]),year_section[(i,lo[1])])
				#print()
				#print(lo)
				#print(year_section)
				#print(teacher_schedule[lo[2]][0][j][4],teacher_schedule[lo[2]][0][j][4]==json.dumps((lo[0],lo[1])),)
				#print("fdsf")
				'''if(lo[1]=='e' and lo[2]==19):
					print()
					print(year_section[(i,lo[1])][0],track[lo[1]][(j,lo[3])],j,lo[4])
					print(teacher_schedule[lo[2]][0][j][4]=='empty' and year_section[(i,lo[1])][0][j][4]=='empty',teacher_schedule[lo[2]][0][j][4],year_section[(i,lo[1])][0][j][4])
					print()
				'''	
				#print(j,lo,teacher_schedule[lo[2]][0][j][5],year_section[(i,lo[1])][0][j][5],"aads", track[lo[1]][(j,lo[3])])
				#print(teacher_schedule[lo[2]][0][j][0]=='empty' ,year_section[(i,lo[1])][0][j][0])

				if(lo[2] not in two_hour):	
					if((j,lo[3]) in track[lo[1]] and track[lo[1]][(j,lo[3])]>=1):
					#loop.pop(0)
						break
					period=[0,1,2,3,4,5]
					#period=random.sample([0,1,2,3,4,5],6)
					for tim in range(6):
						#pre=random.choice(period)
						#period.remove(pre)
						pre=period[tim]
						#print(period)
						if(pre%2==0 and pre!=0):
							if(teacher_schedule[lo[2]][0][j][pre]=='empty' and year_section[(i,lo[1])][0][j][pre]=='empty'):
								teacher_schedule[lo[2]][0][j][pre]=json.dumps((lo[0],lo[1]))
								year_section[(i,lo[1])][0][j][pre]=json.dumps((lo[3],lo[2]))
								lo[4]-=1
								track[lo[1]][(j,lo[3])]+=1
								break
						elif(pre%2):
							if(teacher_schedule[lo[2]][0][j][pre]=='empty' and year_section[(i,lo[1])][0][j][pre]=='empty'  and teacher_schedule[lo[2]][0][j][pre-1]!=json.dumps((lo[0],lo[1]))):	
								teacher_schedule[lo[2]][0][j][pre]=json.dumps((lo[0],lo[1]))
								year_section[(i,lo[1])][0][j][pre]=json.dumps((lo[3],lo[2]))
								lo[4]-=1
								track[lo[1]][(j,lo[3])]+=1					
								break
						elif(teacher_schedule[lo[2]][0][j][0]=='empty'and year_section[(i,lo[1])][0][j][0]=='empty' and teacher_on_mon[lo[2]]<2):
							teacher_schedule[lo[2]][0][j][0]=json.dumps((lo[0],lo[1]))
							year_section[(i,lo[1])][0][j][0]=json.dumps((lo[3],lo[2]))
							lo[4]-=1
							track[lo[1]][(j,lo[3])]+=1
							teacher_on_mon[lo[2]]+=1
							break
							#print(stac)
							#print(teacher_on_mon,teacher_on_mon[lo[2]],lo[2])
					
					break
				else:
					#print("d")
					if((j,lo[3]) in track[lo[1]] and track[lo[1]][(j,lo[3])]>=2):
					#loop.pop(0)
						break
					if(teacher_schedule[lo[2]][0][j][0]=='empty'and year_section[(i,lo[1])][0][j][0]=='empty' and teacher_on_mon[lo[2]]<2):
						teacher_schedule[lo[2]][0][j][0]=json.dumps((lo[0],lo[1]))
						year_section[(i,lo[1])][0][j][0]=json.dumps((lo[3],lo[2]))
						lo[4]-=1
						track[lo[1]][(j,lo[3])]+=1
						teacher_on_mon[lo[2]]+=1
						#print(teacher_on_mon,teacher_on_mon[lo[2]],lo[2])
					elif(teacher_schedule[lo[2]][0][j][1]=='empty' and year_section[(i,lo[1])][0][j][1]=='empty'  ):	
						teacher_schedule[lo[2]][0][j][1]=json.dumps((lo[0],lo[1]))
						year_section[(i,lo[1])][0][j][1]=json.dumps((lo[3],lo[2]))
						lo[4]-=1
						track[lo[1]][(j,lo[3])]+=1

					elif(teacher_schedule[lo[2]][0][j][2]=='empty' and year_section[(i,lo[1])][0][j][2]=='empty'):
						teacher_schedule[lo[2]][0][j][2]=json.dumps((lo[0],lo[1]))
						year_section[(i,lo[1])][0][j][2]=json.dumps((lo[3],lo[2]))
						lo[4]-=1
						track[lo[1]][(j,lo[3])]+=1
					elif(teacher_schedule[lo[2]][0][j][3]=='empty' and year_section[(i,lo[1])][0][j][3]=='empty' ):	
						teacher_schedule[lo[2]][0][j][3]=json.dumps((lo[0],lo[1]))
						year_section[(i,lo[1])][0][j][3]=json.dumps((lo[3],lo[2]))
						lo[4]-=1
						track[lo[1]][(j,lo[3])]+=1
					elif(teacher_schedule[lo[2]][0][j][4]=='empty' and year_section[(i,lo[1])][0][j][4]=='empty'):	
						teacher_schedule[lo[2]][0][j][4]=json.dumps((lo[0],lo[1]))
						year_section[(i,lo[1])][0][j][4]=json.dumps((lo[3],lo[2]))
						lo[4]-=1
						track[lo[1]][(j,lo[3])]+=1
					elif(teacher_schedule[lo[2]][0][j][5]=='empty' and year_section[(i,lo[1])][0][j][5]=='empty' ):
						teacher_schedule[lo[2]][0][j][5]=json.dumps((lo[0],lo[1]))
						year_section[(i,lo[1])][0][j][5]=json.dumps((lo[3],lo[2]))
						lo[4]-=1
						track[lo[1]][(j,lo[3])]+=1
					else:
						#print(lo[4],lo[0],lo[1],teacher_schedule[lo[2]][0][4][5],year_section[(i,lo[1])][0][4][5],lo)
						break
			if(lo[4]<=0):
				break	
		#print(lo,"wr")
	test=0
	for nm in stac:
		if(nm[4]!=0):
			last.append(nm)
			#two_hour.append(nm[2])
		#if(nm[4]<=2 and nm[2] not in two_hour):
		#	two_hour.append(nm[2])
		#	test=1
	print(last,"df")
	print(two_hour)
	print(year_section[(2,'b')])
	#print(track['d'])
	if(test):
		#print(987)
		#print(stac)
		return remain_fun(stac,p,block_hour,track)		
		#print(last,"ee")
		#print()
		#print(stac)
		#print(section_days,"ab")
		#print((last[0][0],last[0][1]),year_section[(last[0][0],last[0][1])])
		#print()
		#print(last[0][2],teacher_schedule[last[0][2]])
		#print()
		#print(teacher_on_mon,teacher_on_mon[last[0][2]])
	return last
def lab_fun(stac,previous_year):
	track={}
	g=[0,1,2,3,4]
	for j in range(5):
		j=random.choice(g)
		g.remove(j)
		loop=copy.copy(stac)
		#print(stac,"ad")
		k=0
		#print(stac[k],"gfdhgfhg");

		#print(track,loop,j)
		while(loop!=[]):
			lo=loop[0]
			i=lo[0]
			#print(loop,lo)
			if(lo[1] not in track):
				track[lo[1]]=[]
			#print(stac[k],j,lo[4]==2 and stac[k][4]==2 and j not in track[lo[1]]);
			#print((i,lo[1]) in year_section,teacher_schedule[lo[2]][0][j][0],j)
			#print(lo[4]==2 and stac[k][4]==2 and j not in track[lo[1]],lo[2])
			if(lo[4]>0 and stac[k][4]>0 and j not in track[lo[1]]):
				#print(year_section[(i,lo[1])][j])

				if(teacher_schedule[lo[2]][0][j][2]=='empty'and year_section[(i,lo[1])][0][j][2]=='empty' ):
					teacher_schedule[lo[2]][0][j][2]=json.dumps((lo[0],lo[1]))
					teacher_schedule[lo[2]][0][j][3]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][2]=json.dumps((lo[3],lo[2]))
					year_section[(i,lo[1])][0][j][3]=json.dumps((lo[3],lo[2]))
					stac[k][4]-=2
					track[lo[1]]+=[j]
				elif(teacher_schedule[lo[2]][0][j][0]=='empty' and year_section[(i,lo[1])][0][j][0]=='empty'):
					teacher_schedule[lo[2]][0][j][0]=json.dumps((lo[0],lo[1]))
					teacher_schedule[lo[2]][0][j][1]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][0]=json.dumps((lo[3],lo[2]))
					year_section[(i,lo[1])][0][j][1]=json.dumps((lo[3],lo[2]))
					track[lo[1]]+=[j]
					stac[k][4]-=2
				elif(teacher_schedule[lo[2]][0][j][4]=='empty'and year_section[(i,lo[1])][0][j][4]=='empty' ):
					teacher_schedule[lo[2]][0][j][4]=json.dumps((lo[0],lo[1]))
					teacher_schedule[lo[2]][0][j][5]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][4]=json.dumps((lo[3],lo[2]))
					year_section[(i,lo[1])][0][j][5]=json.dumps((lo[3],lo[2]))
					stac[k][4]-=2
					track[lo[1]]+=[j]				
			loop.pop(0)
			k+=1

	#for nm in stac:
		#print((nm[0],nm[1]),year_section[(nm[0],nm[1])])
		#nm[4]=0
		#print(nm)
		#print(year_section[(nm[0],nm[1])])
		#previous_year[(nm[0],nm[1])]=year_section[(nm[0],nm[1])]

def only_for_lab(stac,previous_year,y,previous_allday_teacher):
	track={}
	course_track={}
	for i in stac:        #i is section
		
		track[i]=[]
		for k in stac[i]:         #k is course_id
			g=[0,1,2,3,4]
			if(k not in course_track):
				course_track[k]=[]
			final_temp=0	
			for j in range(5):
				#print(g)
				j=random.choice(g)
				g.remove(j)	
				if( j not in track):
					for a in range(0,5,2):
						if((j,a) not in course_track[k] and year_section[(y,i)][0][j][a]=='empty' and year_section[(y,i)][0][j][a+1]=='empty'):
							vatemp=1
							for b in stac[i][k]:
								if(teacher_schedule[b[2]][0][j][a]!='empty' or teacher_schedule[b[2]][0][j][a+1]!='empty'):
									vatemp=0
									break
							if(vatemp):
								for b in stac[i][k]:
									teacher_schedule[b[2]][0][j][a]=json.dumps((y,i))
									teacher_schedule[b[2]][0][j][a+1]=json.dumps((y,i))
									if(b[2] in previous_allday_teacher):
										previous_allday_teacher[b[2]]=copy.deepcopy(teacher_schedule[b[2]])
									b[4]-=2
								year_section[(y,i)][0][j][a]=json.dumps((k,b[2]))
								year_section[(y,i)][0][j][a+1]=json.dumps((k,b[2]))	
								final_temp=1
								course_track[k].append((j,a))
								break
						if(final_temp):
							break
					if(final_temp):
						break
	#print(course_track)
	for nm in stac:
		#print((nm[0],nm[1]),year_section[(nm[0],nm[1])])
		#nm[4]=0
		#print(nm)
		#print(year_section[(nm[0],nm[1])])
		previous_year[(y,nm)]=copy.deepcopy(year_section[(y,nm)])


def teacher_fun(stac,p,days,previous_year,lab_id,previous_lab_teacher):
	last=[]
	loop=copy.deepcopy(stac)
	#print(stac)
	for k in p:
		lo=loop[k]
		#if(lo[3] in lab_id):
		#	continue
		for j in days[lo[2]]:
			i=lo[0]
			j=int(j)

			#print(j)
			#print(teacher_schedule[lo[2]][0][j])#[4])#== 'empty' and year_section[(i,lo[1])][0][j][4]=='empty')
			if(lo[4]>=2 and stac[k][4]>=2):
				#print(year_section[(i,lo[1])][j])
				if(teacher_schedule[lo[2]][0][j][0]=='empty' and year_section[(i,lo[1])][0][j][0]=='empty'):
					teacher_schedule[lo[2]][0][j][0]=json.dumps((lo[0],lo[1]))
					teacher_schedule[lo[2]][0][j][1]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][0]=json.dumps((lo[3],lo[2]))
					year_section[(i,lo[1])][0][j][1]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=2
					stac[k][4]-=2
				elif(teacher_schedule[lo[2]][0][j][4]== 'empty' and year_section[(i,lo[1])][0][j][4]=='empty'):
					teacher_schedule[lo[2]][0][j][4]=json.dumps((lo[0],lo[1]))
					teacher_schedule[lo[2]][0][j][5]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][4]=json.dumps((lo[3],lo[2]))
					year_section[(i,lo[1])][0][j][5]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=2
					stac[k][4]-=2
				elif(teacher_schedule[lo[2]][0][j][2]=='empty'and year_section[(i,lo[1])][0][j][2]=='empty'):

					teacher_schedule[lo[2]][0][j][2]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][2]=json.dumps((lo[3],lo[2]))
					teacher_schedule[lo[2]][0][j][3]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][3]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=2
					stac[k][4]-=2
			elif(stac[k][4]>=1):
				if(teacher_schedule[lo[2]][0][j][0]=='empty'and year_section[(i,lo[1])][0][j][0]=='empty'):
					teacher_schedule[lo[2]][0][j][0]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][0]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=1
					stac[k][4]-=1
				elif(teacher_schedule[lo[2]][0][j][1]=='empty' and year_section[(i,lo[1])][0][j][1]=='empty'):	
					teacher_schedule[lo[2]][0][j][1]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][1]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=1
					stac[k][4]-=1
				elif(teacher_schedule[lo[2]][0][j][2]=='empty' and year_section[(i,lo[1])][0][j][2]=='empty'):
					teacher_schedule[lo[2]][0][j][2]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][2]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=1
					stac[k][4]-=1
				elif(teacher_schedule[lo[2]][0][j][3]=='empty' and year_section[(i,lo[1])][0][j][3]=='empty'):	
					teacher_schedule[lo[2]][0][j][3]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][3]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=1
					stac[k][4]-=1
				elif(teacher_schedule[lo[2]][0][j][4]=='empty' and year_section[(i,lo[1])][0][j][4]=='empty'):	
					teacher_schedule[lo[2]][0][j][4]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][4]=json.dumps((lo[3],lo[2]))
					track[lo[1]][(j,lo[3])]+=1
					stac[k][4]-=1
				elif(teacher_schedule[lo[2]][0][j][5]=='empty' and year_section[(i,lo[1])][0][j][5]=='empty'):
					teacher_schedule[lo[2]][0][j][5]=json.dumps((lo[0],lo[1]))
					year_section[(i,lo[1])][0][j][5]=json.dumps((lo[3],lo[2]))
					#track[lo[1]][(j,lo[3])]+=1
					stac[k][4]-=1

	for nm in stac:
		#print((nm[0],nm[1]),year_section[(nm[0],nm[1])])
		previous_year[(nm[0],nm[1])]=copy.deepcopy(year_section[(nm[0],nm[1])])
		if(nm[3] in previous_lab_teacher ):
			previous_lab_teacher[nm[3]]=copy.deepcopy(year_section[(nm[0],nm[1])])
		if(nm[4]!=0):
			last.append(nm)
	#print()
	#print("gfhdfh",last,stac,"gfhdfh")
	print(last)
	return last	
#print((year_section[(1,'a')]))
#oip=[1,2]
#h=oip[:]
#oip[0]=10
#print(h,oip)	
#opti=year_section[(1,'a')][:]
#print(opti)

def clear_first(temp,prev):
	for lo in prev:
		teacher_schedule[lo]=copy.deepcopy(prev[lo]) 
	for lo in temp:
		#teacher_schedule[lo[2]]=[json.loads(json.dumps([['empty']*6]*5))]
		year_section[(lo[0],lo[1])]=copy.deepcopy(pre_year_section[(lo[0],lo[1])])

def clear_second(temp,prev,previous_year,sec):
	#print("dff")
	#print(temp)
	#print(opti)
	for lo in year_section:
		#teacher_schedule[lo[2]]=[json.loads(json.dumps([['empty']*6]*5))]
		if(lo[1]==sec):
			year_section[lo]=copy.deepcopy(pre_year_section[lo])
	for lo in prev:
		teacher_schedule[lo]=copy.deepcopy(prev[lo]) 
	for lo in previous_year:
		year_section[lo]=copy.deepcopy(previous_year[lo])
	
	#print(year_section[(1,'a')]==[[['empty']*6]*5])
	#print(year_section)
def clear_lab(lab,y,previous_lab_teacher,previous_year,sec):
	#lab=[]
	cursor.execute("select * from takes where year=%s and section=%s and hour!=0 and course_id in(select id from course where type='lab');",[y,sec])
	result=cursor.fetchall()
	for t in result:
		if(t[1] not in lab):
			lab[t[1]]={}
		if(t[3] not in lab[t[1]]):
			lab[t[1]][t[3]]=[]

		teacher_schedule[list(t)[2]]=copy.deepcopy(previous_lab_teacher[list(t)[2] ])
		if((list(t)[0],list(t)[1]) in previous_year):
			year_section[(list(t)[0],list(t)[1])]=copy.deepcopy(previous_year[(list(t)[0],list(t)[1])])
		else:
			year_section[(list(t)[0],list(t)[1])]=copy.deepcopy(pre_year_section[(list(t)[0],list(t)[1])])
		lab[t[1]][t[3]].append(list(t))
		#lab_id.append(t[3])
def fun(y,sec):

	cursor.execute("select * from takes where year=%s and section =%s and hour!=0 and instructor_id in (select id from teacher as t where not exists(select * from teacher as t1 where t1.days like %s and t.days=t1.days));",[y,sec,json.dumps(['6'])])
	result=cursor.fetchall()
	day_teacher=[] #particular day teacher works
	temp_day_teacher=[]
	track={}
	i=0
	particular_list=[]
	#print()
	days={}
	previous_allday_teacher={}
	previous_someday_teacher={}
	previous_year={}
	for t in result:
		day_teacher.append(list(t))
		temp_day_teacher.append(list(t))
		cursor.execute("select days from teacher where id=%s ;",[t[2]])
		r=cursor.fetchall()
		previous_someday_teacher[list(t)[2]]=copy.deepcopy(teacher_schedule[list(t)[2]])
		#print(r[0][0])
		days[t[2]]=json.loads(r[0][0])
		particular_list.append(i)
		i+=1
	lab={}
	previous_lab_teacher={}
	lab_id=[]
	cursor.execute("select * from takes where year=%s and section=%s and hour!=0 and course_id in(select id from course where type='lab');",[y,sec])
	result=cursor.fetchall()
	for t in result:
		if(t[1] not in lab):
			lab[t[1]]={}
		if(t[3] not in lab[t[1]]):
			lab[t[1]][t[3]]=[]
		previous_lab_teacher[list(t)[2]]=copy.deepcopy(teacher_schedule[list(t)[2]])
		lab[t[1]][t[3]].append(list(t))
		lab_id.append(t[3])

	block_hour=[]
	cursor.execute("select id from teacher where two_hour=1;")
	result=cursor.fetchall()
	for t in result:
		block_hour.append(t[0])


	all_teacher=[]
	temp_all_teacher=[]
	cursor.execute("select * from takes where year=%s and section=%s and hour!=0 and instructor_id in (select id from teacher as t where exists(select * from teacher as t1 where t1.days like %s and t.days=t1.days));",[y,sec,json.dumps(['6'])])
	result=cursor.fetchall()
	#print(day_teacher)
	#print(days)
	all_list=[]
	i=0
	for t in result:
		#print(t)
		if(t[3] not in lab_id ):
			all_list.append(i)
			all_teacher.append(list(t))
			temp_all_teacher.append(list(t))
			i+=1

 
		previous_allday_teacher[list(t)[2]]=copy.deepcopy(teacher_schedule[list(t)[2]])
		
	all_permutation=permutations(all_list)
	particular_permutation=permutations(particular_list)
	#temp_day_teacher=copy.deepcopy(day_teacher)
	#temp_all_teacher=copy.deepcopy(all_teacher)
	#print("ads")
	print(all_teacher)
	#print(day_teacher)

	for i in particular_permutation:
		day_teacher=copy.deepcopy(temp_day_teacher)
		#print()
		#print(previous_someday_teacher)
		#print()
		clear_first(day_teacher,previous_someday_teacher)
		#print(year_section)
		#print(year_section[(1,'a')])
		#print(qw)
		#previous_year={}
		#just()
		if(teacher_fun(day_teacher,i,days,previous_year,lab_id,previous_lab_teacher)==[]):
			#print("\nhjjjfkd\n",y)
			
			lab={}
			clear_lab(lab,y,previous_lab_teacher,previous_year,sec)
			print(lab)
			only_for_lab(lab,previous_year,y,previous_allday_teacher)
			#lab_fun(lab,previous_year)
			print(lab)
			#print("as")
			for ij in all_permutation:
				all_teacher=copy.deepcopy(temp_all_teacher)
				#print(all_teacher)
				#print(1223)
				#print()
				#print(previous_year,"ffff")	
				#print(ij,y,all_teacher,temp_all_teacher)
				#print()
				#print(previous_allday_teacher,"rama")
				#print()
				clear_second(all_teacher,previous_allday_teacher,previous_year,sec)
				#print("\nhjdhf",qwer,"gdhf\n")
				#print(year_section[(3,'e')])
				#print(previous_year)
				#print(123)
				#just()
				#print(all_teacher)
				if(remain_fun(all_teacher,ij,block_hour,{})==[]):
					#print((y,'a'),year_section[(y,'a')])
					#print(all_teacher)
					#print(lab)
					#print(day_teacher)
					#return 1
					#if(y!=4):
					#	if(fun(y+1)):
					#		return 1
					#else:
					#print((3,'d'),year_section[(3,'d')])
					return 1
				#else:	
				#	print(y)
				#	print()
				#	return 0

			
	return 0				
#print(year_section[(1,'a')])
ye=int(input())
#w=fun(ye)
#print(w)
tog=1
for i in range(10):
	if(fun(ye,chr(ord('a')+i))==0):
		tog=0
		break
for  i in year_section:
	if(i[0]==3):
		print(i,year_section[i])
		print()
print(tog)
#print(year_section[(2,'a')])
tog=0
if(tog):
	for i in year_section:
		print(i,year_section[i])
		cursor.execute('UPDATE section SET schedule = %s WHERE year = %s and name=%s', [json.dumps(year_section[i][0]),i[0],i[1]])
		print()
	for i in teacher_schedule:
		print(i,teacher_schedule[i][0])
		cursor.execute('UPDATE teacher SET schedule = %s WHERE id=%s', [json.dumps(teacher_schedule[i][0]),i])
		print()	
	cursor.execute('UPDATE takes SET hour=0 where year=%s',[ye])
conn.commit()
conn.close()
'''
for i in teacher_schedule:
	print(i,teacher_schedule[i])
	print()'''