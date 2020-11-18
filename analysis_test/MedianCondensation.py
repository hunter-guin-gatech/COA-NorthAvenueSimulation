import sqlite3 as lite
import csv 
import statistics as st
import numpy as np 

def getType(length):
    char=['PC','B','SU','TT']
    if(length>10 and length<18):
        return 'PC'
    elif(length>35 and length<45):
        return 'B'
    elif(length>25 and length<35):
        return 'SU'
    elif(length>50 and length<60):
        return 'TT'

def MedianCondensation(infile, db_name, table_name):
	f_m = 0.3048006096012192
	CarList=[]; CarType=[]; CarU=[]; CarV=[]
	CarGrade=[]; CarTime=[]; CarDist=[]
	CarX=[]; CarY=[]; CarZ=[]; CarSpeed=[]; CarAccl=[]
	to_db=[]

	with open(infile) as loglines:
	    for line in loglines:
	        f=line.split('\n')[0].split(';')
	        t=float(f[0]); vN=int(f[2]); VType=getType(float(f[9]))
	        XYZ_f=[float(i) for i in f[3].split()]; XYZ_r=[float(i) for i in f[4].split()]
	        X=XYZ_f[0]; Y=XYZ_f[1]; Z=XYZ_f[2]
	        X_1=XYZ_r[0]; Y_1=XYZ_r[1]; Z_1=XYZ_r[2]
	        speed=float(f[5])*0.44704; accl=float(f[6])*f_m
	        u, v=X - X_1, Y - Y_1
	        uv=(u**2+v**2)**.5
	        u/=uv; v/=uv        

	        if vN not in CarList:
	            CarList.append(vN); CarType.append(VType)
	            CarDist.append(0.0); CarGrade.append(0.0); CarTime.append([t])
	            CarX.append([0.5*(X+X_1)]); CarY.append([0.5*(Y+Y_1)]); CarZ.append([0.5*(Z+Z_1)]); CarSpeed.append([speed]); CarAccl.append([accl])
	            CarU.append([u]); CarV.append([v])
	            j=len(CarList)-1
	        else:
	            j=CarList.index(vN)
	            CarTime[j].append(t)
	            if len(CarX[j])>0:
	                CarDist[j]+=((CarX[j][-1]-X)**2 + (CarY[j][-1]-Y)**2)**.5 
	            CarX[j].append(0.5*(X+X_1)); CarY[j].append(0.5*(Y+Y_1)); CarZ[j].append(0.5*(Z+Z_1)); CarSpeed[j].append(speed); CarAccl[j].append(accl)
	            CarU[j].append(u); CarV[j].append(v)

	        if round(CarTime[j][-1]*10)%10==9:
	            tim=int(np.floor(CarTime[j][0]))
	            X=st.median(CarX[j]); Y=st.median(CarY[j]);  Z=st.median(CarZ[j]); speed=st.median(CarSpeed[j]); accl=st.median(CarAccl[j])
	            tdist=sum(CarSpeed[j])*0.223694; ttime=0.1*len(CarSpeed[j])
	            u=np.mean(CarU[j]); v=np.mean(CarV[j])
	            uv=(u**2+v**2)**.5
	            u/=uv; v/=uv
	            Grade=CarGrade[j] 
	            if CarDist[j]>0.0:
	                Grade=(CarZ[j][-1]-CarZ[j][0])/CarDist[j]
	            CarTime[j]=[]; CarX[j]=[]; CarY[j]=[]; CarZ[j]=[]; CarSpeed[j]=[]; CarAccl[j]=[]; CarDist[j]=0.0; CarGrade[j]=Grade
	            CarU[j]=[]; CarV[j]=[]
	            to_db.append((tim, vN, VType, X, Y, Z, u, v, speed, accl, Grade, tdist, ttime))

	for j in range(len(CarList)):
		if len(CarX[j])>0:
			vN, VType = CarList[j], CarType[j]
			tim=int(np.floor(CarTime[j][0]))
			X=st.median(CarX[j]); Y=st.median(CarY[j]);  Z=st.median(CarZ[j]); speed=st.median(CarSpeed[j]); accl=st.median(CarAccl[j])
			tdist=sum(CarSpeed[j])*0.223694; ttime=0.1*len(CarSpeed[j])
			u=np.mean(CarU[j]); v=np.mean(CarV[j])
			uv=(u**2+v**2)**.5
			u/=uv; v/=uv
			Grade=CarGrade[j]
			if CarDist[j]>0.0:
				Grade=(CarZ[j][-1]-CarZ[j][0])/CarDist[j]
			to_db.append((tim, vN, VType, X, Y, Z, u, v, speed, accl, Grade, tdist, ttime))		

	con = lite.connect(db_name)
	cur = con.cursor()
	cur.executemany("INSERT INTO "+table_name+" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
	con.commit()
	con.close()      


db_name='./analysis_test/Sample-Condensed-Trajectory.db'
con = lite.connect(db_name)
cur = con.cursor()
cur.execute("CREATE TABLE OneHzData (TSt, VehID, VehType, X, Y, Z, vector_u, vector_v, speed_m_s, accl_m_s_s, grade, Distance_mphs, duration);")
con.commit()    
con.close()

MedianCondensation('./analysis_test/Sample_Trajectory.fzp', db_name, 'OneHzData')