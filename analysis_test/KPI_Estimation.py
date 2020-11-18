import sqlite3 as lite
import csv 
import statistics as st
import numpy as np 

def getBin(speed, accl, VSP):
    if accl<=-2.0:
        return 0
    elif speed<1.0:
        return 1
    elif speed<25:
        if VSP<0:
            return 11
        elif VSP<3:
            return 12
        elif VSP<6:
            return 13
        elif VSP<9:
            return 14
        elif VSP<12:
            return 15
        else:
            return 16
    elif speed<50:
        if VSP<0:
            return 21
        elif VSP<3:
            return 22
        elif VSP<6:
            return 23
        elif VSP<9:
            return 24
        elif VSP<12:
            return 25
        elif VSP<18:
            return 27
        elif VSP<24:
            return 28
        elif VSP<30:
            return 29
        else:
            return 30
    else:
        if VSP<6:
            return 33
        elif VSP<12:
            return 35
        elif VSP<18:
            return 37
        elif VSP<24:
            return 38
        elif VSP<30:
            return 39
        else:
            return 40

def KPI_Estimation(v,acc,VType,grade):
    Energy=[]
    char=['PC','B','SU','TT']
    A=[0.156461,1.03968,0.596526,1.47389]
    B=[0.002001,0,0,0]
    C=[0.000492,0.003587,0.001603,0.003681]
    M=[1.4788,17.1,17.1,17.1]
    m=[1.4788,16.556,8.5389,24.419]
    g=9.81
    j=char.index(VType)
    VSP=(A[j]/M[j])*v+(B[j]/M[j])*v**2+(C[j]/M[j])*v**3+(m[j]/M[j])*(acc+g*grade)*v
    Bin=getBin(v*2.23694,acc*2.23694,VSP)
    BinDetails=list(map(list, zip(*(list(csv.reader(open('../EnergyLookup/EnergyEmissions_'+VType+'_2017.csv')))))))
    for i in range(8):
        Energy.append(float(BinDetails[i+1][BinDetails[0].index(str(Bin))]))
    return Energy


db_name='Sample-Condensed-Trajectory.db'
con = lite.connect(db_name)
cur = con.cursor()
cur.execute("SELECT * FROM OneHzData;")
#cur.execute("CREATE TABLE KPIData (TSt, VehID, VehType, X, Y, vector_u, vector_v, Energy_kJ, CO2_gm);")
data=cur.fetchall()
con.commit()    
con.close()
to_db=[]

for i in data:
	energy=[x*i[12]/3600.0 for x in KPI_Estimation(i[8], i[9], i[2], i[10])]
	to_db.append((i[0], i[1], i[2], i[3], i[4], i[6], i[7], energy[0], energy[1]))

print(data)

con = lite.connect(db_name)
cur = con.cursor()
cur.executemany("INSERT INTO KPIData VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()    
con.close()