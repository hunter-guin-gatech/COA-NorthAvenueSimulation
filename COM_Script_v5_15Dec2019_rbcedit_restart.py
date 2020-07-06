# -*- coding: cp1252 -*-
# COM-Server
import win32com.client as com
import os
import csv
import datetime
from datetime import date
#import arrow
import time
import urllib
import math
import binascii
import pathlib
import requests
#import urllib2
global Vissim
import urllib.request
import ast
import pandas as pd
import numpy as np
from flask import request
import glob
import gc
import sys
import datetime as dt

## Connecting the CDM Server => Open a new Vissim Window
Vissim = com.Dispatch("Vissim.Vissim.900")

Path_of_COM_Basic_Commands_network = os.getcwd()
print (os.getcwd())

def clear_jsons():
	files = glob.glob('//ad.gatech.edu/gtfs/COE/CEE/Transpo/smartdata/RealTimeRunTrajectoryFiles_5Sep2019/trajectoryfiles/*.json')
	for f1 in files:
		os.remove(f1)
	files_signal = glob.glob('//ad.gatech.edu/gtfs/COE/CEE/Transpo/smartdata/RealTimeRunTrajectoryFiles_5Sep2019/signalfiles/*.json')
	for f2 in files_signal:
		os.remove(f2)

## Defining random seeds
Random_Seed = [21]

## 
with open('simulation_time.txt', 'w+') as tfile:
	print('Simulation Time File created!')

	
## for loop to do simulation for every random seed
for r in range(0, len(Random_Seed)):
	clear_jsons()
	## Load a Network:
	Filename = os.path.join(Path_of_COM_Basic_Commands_network, 'North Avenue Thesis 1% Truck_nofreedompkway_v13_14mar2019.inpx')
	flag_read_additionally  = False
	Vissim.LoadNet(Filename,flag_read_additionally)

	## Load a Layout:
	Filename = os.path.join(Path_of_COM_Basic_Commands_network, 'North Avenue Thesis 1% Truck_nofreedompkway_v13_14mar2019.layx')
	Vissim.LoadLayout(Filename)

	Vissim.Net.Scripts.SetAllAttValues('RunType', 1)
	simRes = Vissim.Simulation.AttValue('SimRes')
	simtime = 3600
	Vissim.Simulation.SetAttValue('SimPeriod', simtime)
	Vissim.Simulation.SetAttValue('UseMaxSimSpeed', True)
	#Vissim.Simulation.SetAttValue('SimSpeed', 1)
	
	Vissim.Simulation.SetAttValue('RandSeed', Random_Seed[r])
##	Vissim.ResumeUpdateGUI(True)

## To rin fast simulations, activate QUICKMODE - disables the visibility of al dynamic elements
	Vissim.Graphics.CurrentNetworkWindow.SetAttValue("QuickMode",1)
	Vissim.SuspendUpdateGUI()

	# Assigninig Signal Heads for Glen Iris Intersection
	#Assigning signal head for phase 5
	obj_wbL=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(5)

	#Assigning signal head for phase 6
	obj_ebt1=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(6)
	obj_ebt2=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(6)
	obj_ebt3=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(6)

	#Assigning signal head for phase 7
	obj_nbL=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(7)

	#Assigning signal head for phase 8
	obj_sbt1=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(8)

	#Assigning signal head for phase 1
	obj_ebL=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(1)

	#Assigning signal head for phase 2
	obj_wbt1=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(2)
	obj_wbt2=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(2)

	#Assigning signal head for phase 3
	obj_sbL=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(3)

	#Assigning signal head for phase 4
	obj_nbt1=Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(4)

	## Assigning signal heads for ponce city market intersection
	#Assigning signal head for phase 1
	ponce_ebL=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(1)

	#Assigning signal head for phase 6
	ponce_ebt1=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(6)
	ponce_ebt2=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(6)

	#Assigning signal head for phase 4
	ponce_nbLT=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(4)

	#Assigning signal head for phase 2
	ponce_wbL=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(2)
	ponce_wbt1=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(2)
	ponce_wbt2=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(2)

	#Assigning signal head for phase 3
	ponce_sbL=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(3)

	#Assigning signal head for phase 8
	ponce_sbt1=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(8)

	## Assigning signal heads for state street intersection
	#Assigning signal head for phase 2
	state_ebLT=Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2)

	#Assigning signal head for phase 6
	state_wbt=Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6)

	#Assigning signal head for phase 8
	state_sbL=Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8)

	## Assigning signal heads for tech parkway intersection
	#Assigning signal head for phase 6
	techparkway_ebLT=Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(6)

	#Assigning signal head for phase 7 and 4
	techparkway_nbL=Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(7)
	techparkway_nbt=Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4)

	#Assigning signal head for phase 5 and 2 
	techparkway_wbL=Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(5)
	techparkway_wbt1=Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2)
	
	#Assigning signal head for phase 3
	techparkway_sbL=Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3)

	#Assigning signal head for phase 8
	techparkway_sbt1=Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(8)

	## Assigning signal heads for techwood intersection
	#Assigning signal head for phase 1
	techwood_ebL=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1)

	#Assigning signal head for phase 6
	techwood_ebt1=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(6)
	#techwood_ebt2=Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(6)

	#Assigning signal head for phase 7
	techwood_nbLT=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(7)

	#Assigning signal head for phase 4
	techwood_nbt=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4)

	#Assigning signal head for phase 5 and phase 2
	techwood_wbL=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(5)
	techwood_wbt1=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2)

	#Assigning signal head for phase 3
	techwood_sbL=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3)

	#Assigning signal head for phase 8
	techwood_sbt1=Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(8)

	## Assigning signal heads for I75 Off Ramp intersection
	#Assigning signal head for phase 2
	i75_ebLT=Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2)

	#Assigning signal head for phase 6
	i75_wbt1=Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(6)

	#Assigning signal head for phase 4
	i75_sbL=Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4)

	## Assigning signal heads for spring intersection
	#Assigning signal head for phase 8
	spring_ebt=Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(8)

	#Assigning signal head for phase 4 and 7
	spring_wbL=Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(7)
	spring_wbt=Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4)

	#Assigning signal head for phase 2
	spring_sbLT=Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2)

	## Assigning signal heads for west peachtree intersection
	#Assigning signal head for phase 3
	westpeachtree_ebL=Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3)

	#Assigning signal head for phase 8
	westpeachtree_ebt=Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(8)

	#Assigning signal head for phase 6
	westpeachtree_nbLT=Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(6)

	#Assigning signal head for phase 4
	westpeachtree_wbt=Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4)

	## Assigning signal heads for peachtree intersection
	#Assigning signal head for phase 2
	peachtree_ebLT=Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2)

	#Assigning signal head for phase 2
	peachtree_wbLT=Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2)
   
	#Assigning signal head for phase 4
	peachtree_nbLT=Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4)

	#Assigning signal head for phase 4
	peachtree_sbLT=Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4)

	## Assigning signal heads for juniper intersection
	#Assigning signal head for phase 6
	juniper_ebt=Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(6)

	#Assigning signal head for phase 2 and phase 5
	juniper_wbL=Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(5)
	juniper_wbt=Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2)

	#Assigning signal head for phase 4
	juniper_sbLT=Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4)

	## Assigning signal heads for piedmont intersection
	#Assigning signal head for phase 1 and phase 6
	piedmont_ebL=Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1)
	piedmont_ebT=Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(6)

	#Assigning signal head for phase 2
	piedmont_wbT=Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2)
   
	#Assigning signal head for phascurrent_peachtree = getHexSignal(4800, sig_ttime,sig_sttime,swt)e 4
	piedmont_nbLT=Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4)

	## Assigning signal heads for Central Park intersection
	#Assigning signal head for phase 6
	centralpark_ebLT=Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(6)

	#Assigning signal head for phase 8
	centralpark_sbLT=Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(8)
   
	#Assigning signal head for phase 4
	centralpark_nbLT=Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4)
	#Assigning signal head for phase 2
	centralpark_wbLT=Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2)

	## Assigning signal heads for Hunt intersection
	#Assigning signal head for phase 2
	hunt_ebLT=Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2)

	#Assigning signal head for phase 6
	hunt_wbLT=Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(6)

	#Assigning signal head for phase 8
	hunt_sbLT=Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(8)
   
	#Assigning signal head for phase 4
	hunt_nbLT=Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4)

	## Assigning signal heads for Parkway intersection
	#Assigning signal head for phase 2
	parkway_ebLT=Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2)

	#Assigning signal head for phase 6
	parkway_wbLT=Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(6)

	#Assigning signal head for phase 8
	parkway_sbLT=Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(8)
   
	#Assigning signal head for phase 4
	parkway_nbLT=Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4)

	## Assigning signal heads for Boulevard intersection
	#Assigning signal head for phase 2
	boulevard_ebLT=Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2)

	#Assigning signal head for phase 6
	boulevard_wbLT=Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(6)

	#Assigning signal head for phase 8
	boulevard_sbLT=Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(8)
   
	#Assigning signal head for phase 4
	boulevard_nbLT=Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4)

	#ip_address='128.61.130.150'
	# ip_address_post='128.61.129.39'
	ip_address_post='127.0.0.1'
	## Function to fetch data using flask
	def getLiveSignal(epoch, simtime):
	    ip_address='128.61.130.150'
	    intcode=[4794, 4795, 4796, 4797, 4798, 4799, 4800, 4801, 4802, 4804, 4805, 4806, 4807, 4808, 4809, 7322]
	    hexcode=[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
	    link='http://'+ip_address+':5000/LiveSignal/startepoch='+str(epoch)+'&simtime='+str(simtime)
	    with urllib.request.urlopen(link) as url:
	        data = url.read()
	    data = ast.literal_eval(str(data)[2:-1])
	    link1='http://'+ip_address+':5000/LiveSignal/startepoch='+str(epoch)+'&simtime='+str(simtime-1)
	    with urllib.request.urlopen(link1) as url:
	        data1 = url.read()
	    data1 = ast.literal_eval(str(data1)[2:-1])  
	    #return [[] if (x==y and x!=-1) else x for x,y in zip(data, data1)] 
	    if simtime>0:
	        return [x if x!=y else [] if x!=-1 else 2 for x,y in zip(data, data1)] 
	    else:
	        return [[] if (x==y and x!=-1) else x for x,y in zip(data, data1)]

	def getLiveVolume(intrsc, approach, epoch, simtime):
		ip_address='128.61.130.150'
		#ip_address='128.61.129.39'
		link='http://'+ip_address+':5000/LiveVolume/startepoch='+str(epoch)+'&intersection='+str(intrsc)+'&approach='+approach+"&simtime="+str(simtime)
		with urllib.request.urlopen(link) as url:
			data = url.read()
		data = ast.literal_eval(str(data)[2:-1])
		print (data)
		return data

	def getTurn(epoch, simtime, intrsc, approach):
		ip_address='128.61.130.150'
		#ip_address='128.61.129.39'
		link='http://'+ip_address+':5000/Turn/startepoch='+str(epoch)+'&simtime='+str(simtime)+'&intersection='+str(intrsc)+'&approach='+approach 
		with urllib.request.urlopen(link) as url:
			data = url.read()
		data = ast.literal_eval(str(data)[2:-1])
		return [round(i, 2) for i in data]


	i = 0
	flag = 0
	turn_count_key_df = pd.read_csv('turn_count_vissim_com_key_intcodes.csv', sep=',')
	volume_count_key_df = pd.read_csv('volume_count_vissim_com_key_intcodes.csv', sep=',')
	## Update these volume arrays
	volume_intersection_key_array = np.array(volume_count_key_df[['intersection']]).tolist()
	volume_approach_key_array = np.array(volume_count_key_df[['approach']]).tolist()
	volume_itemkey_array = np.array(volume_count_key_df[['item_key']]).tolist()

	## Update these turn count arrays
	turn_intersection_nm_array = np.array(turn_count_key_df[['intersection_name']]).tolist()
	turn_approach_array = np.array(turn_count_key_df[['approach']]).tolist()
	app_item_array =  np.array(turn_count_key_df[['app_item_key']]).tolist()
	turn_item_key_array = np.array(turn_count_key_df[['turn_item_key']]).tolist()
	turn_position_key_array = np.array(turn_count_key_df[['array_turn_position']]).tolist()

	########### Giving Info on Vehicle Input IDs ######################################
	########### Giving Info on Vehicle Input IDs ######################################
	bobbydodd_driveway = 28
	connector_driveway = 29
	huntdriveway_nb= 27
	parkway_driveway = 31
	driveway_volume_itemkeys = [28, 29, 27, 31]

	############### PROVIDING BALANCED VOLUMES (Vissim volumes obtained and balanced using synchro and field collected data) #######################
	vol_bobbydodd_driveway = 190
	vol_connector_driveway = 43
	vol_huntdriveway_nb = 418
	vol_parkway_driveway = 75
	driveway_volume_namekeys = [190, 43, 418, 75]

	############### SET TIME INTERVAL COLLECTION FOR VOLUME INPUTS ##########################################
	for timeInt in range(2, (int(simtime/360)+1)):
		Vissim.Net.TimeIntervalSets.ItemByKey(2).TimeInts.AddTimeInterval(timeInt)
		TimeIntNoNew = Vissim.Net.TimeIntervalSets.ItemByKey(2).TimeInts.ItemByKey(timeInt)
		TimeIntNoNew.SetAttValue('Start',360*(timeInt-1))
		Vissim.Net.TimeIntervalSets.ItemByKey(1).TimeInts.AddTimeInterval(timeInt)
		TimeIntNoNew1 = Vissim.Net.TimeIntervalSets.ItemByKey(1).TimeInts.ItemByKey(timeInt)
		TimeIntNoNew1.SetAttValue('Start',360*(timeInt-1))
		for t in range(len(volume_itemkey_array)):
			key_no = volume_itemkey_array[t][0]
			print (key_no)
			Vissim.Net.VehicleInputs.ItemByKey(key_no).SetAttValue('Cont('+str(timeInt)+')', False)
		for p in range(len(driveway_volume_itemkeys)):
			key_no_dr = driveway_volume_itemkeys[p]
			print (key_no_dr)
			Vissim.Net.VehicleInputs.ItemByKey(key_no_dr).SetAttValue('Cont('+str(timeInt)+')', False)
		
		
	#######################  SET REAL TIME START TIMES FOR THE SIMULATION ########################

	### SIMULATION WAIT TILL INITIALIZATION VALUE ################################################
	sim_start_flag = 0
	while (sim_start_flag==0):
		minute = int(time.strftime("%M"))
		second = int(time.strftime("%S"))
		print (minute)
		print (second)
		if ((minute-1)%6==0) & (second==5):
			start_sim_wall_clock = time.strftime('%H:%M:%S')
			#print (start_sim_wall_clock.split(":")[1])
			print (start_sim_wall_clock)

			start_sim_wall_clock = math.floor(time.time())
			f= open("//ad.gatech.edu/gtfs/COE/CEE/Transpo/smartdata/RealTimeRunTrajectoryFiles_5Sep2019/start_sim_wall_clock.txt","w")
			f.write(str(start_sim_wall_clock))
			f.close()
			#startepoch = time.time()
	####### START TIMESTAMP FOR REAL TIME RUN ####################################################
			while (i<((simtime)*simRes)):
				if (i==0):
					json_list = []
					json_list_signals = []
				
				if (i%10==0):
					simTime = int(i/10)
					signal_json_simtime={'simTime':'%i'%(simTime)}
					json_list_signals.append(signal_json_simtime)	
				## set vissim volumes every 6 minute 
					if (i%3600==0):
						#Vissim.Simulation.Stop()
						print (int(i/3600))
						simTime = int(i/10)
						if i%100==0:
							with open('simulation_time.txt', 'a') as tfile:
									tfile.write(str(time.time())+'\t'+str(i/10)+'\n')
						vol_int_number = int(i/3600)+1 #Volume interval number = Vehicle Input Number
						print (vol_int_number)

						
						##Fetch volume and route ratios per 6 minutes
						no_of_intervals = int(simtime/360)
						for tt in range(len(volume_itemkey_array)):
							#key_no = volume_itemkey_array[tt]
							# for t in range(no_of_intervals):
							#	 vol_int_number = t+1
							volume_interval = 'Volume('+str(vol_int_number)+')'
							#print (volume_interval)
							relative_flow_interval = 'RelFlow('+str(vol_int_number)+')'
							#print (relative_flow_interval)
							#tst = start_time_in_Tst+360*(t)
							v_time = start_sim_wall_clock
							input_volume_value = getLiveVolume(volume_intersection_key_array[tt][0], volume_approach_key_array[tt][0], v_time, simTime)
							#print (tst)
							print (input_volume_value)
							#print (input_volume_value)
							Vissim.Net.VehicleInputs.ItemByKey(volume_itemkey_array[tt][0]).SetAttValue(volume_interval, int((input_volume_value)*10))
						#v_time_frmt = dt.datetime.utcfromtimestamp(v_time+simTime).strftime("%H:%M:%S")					
						print ("Volume Data Requested For - "+ str(v_time))
						####Add the new vehicle inputs to driveways approaches
						# for m in range(no_of_intervals):
						#	 vol_int_number = m+1
						volume_interval = 'Volume('+str(vol_int_number)+')'
						#print (volume_interval)
						relative_flow_interval = 'RelFlow('+str(vol_int_number)+')'
						#print (relative_flow_interval)
						Vissim.Net.VehicleInputs.ItemByKey(bobbydodd_driveway).SetAttValue(volume_interval, vol_bobbydodd_driveway)
						Vissim.Net.VehicleInputs.ItemByKey(huntdriveway_nb).SetAttValue(volume_interval, vol_huntdriveway_nb)
						Vissim.Net.VehicleInputs.ItemByKey(parkway_driveway).SetAttValue(volume_interval, vol_parkway_driveway)
						Vissim.Net.VehicleInputs.ItemByKey(connector_driveway).SetAttValue(volume_interval, vol_connector_driveway) 

						## Add turn count for vehicle approaches to Vissim 
						for y in range(len(app_item_array)):
							# for t in range(no_of_intervals):
							#	 vol_int_number = t+1
							volume_interval = 'Volume('+str(vol_int_number)+')'
							#print (volume_interval)
							relative_flow_interval = 'RelFlow('+str(vol_int_number)+')'
							#print (relative_flow_interval)
						   # tst = start_time_in_Tst+360*(t)
							## Call turn percent function to get turn percent
							print (turn_intersection_nm_array[y][0])
							print (turn_approach_array[y][0])
							get_turn_array = getTurn(v_time, simTime, turn_intersection_nm_array[y][0], turn_approach_array[y][0])
							t_position = turn_position_key_array[y][0]
							Vissim.Net.VehicleRoutingDecisionsStatic.ItemByKey(app_item_array[y][0]).VehRoutSta.ItemByKey(turn_item_key_array[y][0]).SetAttValue(relative_flow_interval, get_turn_array[t_position])


						
					print ('SIM SECOND BEFORE  '+str(Vissim.Simulation.SimulationSecond))
					Vissim.Simulation.RunSingleStep()
					print ('SIM SECOND AFTER  '+str(Vissim.Simulation.SimulationSecond))

					print (str(i)+'  RUN STEP')

					##Set Start States of the Signal Heads##
					if (i==0):
						#starttime=datetime.now().strftime("%H-%M-%S")
					   # starttime=set_to_midnight(simday).strftime("%H-%M-%S")
						#print ("Setting this "+str(starttime)+" as start time")
						# Glen default stat when master clock =0; 4 and 8 at green
						obj_wbL.SetAttValue("SigState", "RED")
						obj_wbt1.SetAttValue("SigState", "RED")
						obj_wbt2.SetAttValue("SigState", "RED")

						obj_ebL.SetAttValue("SigState", "RED")
						obj_ebt1.SetAttValue("SigState", "RED")
						obj_ebt2.SetAttValue("SigState", "RED")
						obj_ebt3.SetAttValue("SigState", "RED")

						obj_nbL.SetAttValue("SigState", "RED")
						obj_nbt1.SetAttValue("SigState", "RED")

						obj_sbL.SetAttValue("SigState", "RED")
						obj_sbt1.SetAttValue("SigState", "RED")

						
						# Ponce default stat when master clock =0; 2 and 6 at Amber
						ponce_wbL.SetAttValue("SigState", "RED")
						ponce_wbt1.SetAttValue("SigState", "RED")
						ponce_wbt2.SetAttValue("SigState", "RED")

						ponce_ebL.SetAttValue("SigState", "RED")
						ponce_ebt1.SetAttValue("SigState", "RED")
						ponce_ebt2.SetAttValue("SigState", "RED")

						ponce_nbLT.SetAttValue("SigState", "RED")

						ponce_sbL.SetAttValue("SigState", "RED")
						ponce_sbt1.SetAttValue("SigState", "RED")
						
						# State default state
						state_ebLT.SetAttValue("SigState", "RED")
						state_wbt.SetAttValue("SigState", "RED")
						state_sbL.SetAttValue("SigState", "RED")

						# Tech parkway default stat
						techparkway_ebLT.SetAttValue("SigState", "RED")
						techparkway_nbL.SetAttValue("SigState", "RED")
						techparkway_nbt.SetAttValue("SigState", "RED")
						techparkway_wbL.SetAttValue("SigState", "RED")
						techparkway_wbt1.SetAttValue("SigState", "RED")
						techparkway_sbL.SetAttValue("SigState", "RED")
						techparkway_sbt1.SetAttValue("SigState", "RED")
						
						# Techwood default stat
						techwood_ebL.SetAttValue("SigState", "RED")
						techwood_ebt1.SetAttValue("SigState", "RED")
						techwood_nbLT.SetAttValue("SigState", "RED")
						techwood_nbt.SetAttValue("SigState", "RED")
						techwood_wbL.SetAttValue("SigState", "RED")
						techwood_wbt1.SetAttValue("SigState", "RED")
						techwood_sbL.SetAttValue("SigState", "RED")
						techwood_sbt1.SetAttValue("SigState", "RED")

						# I75 Off Ramp
						i75_ebLT.SetAttValue("SigState", "RED")
						i75_wbt1.SetAttValue("SigState", "RED")
						i75_sbL.SetAttValue("SigState", "RED")

						# Spring
						spring_ebt.SetAttValue("SigState", "RED")
						spring_wbL.SetAttValue("SigState", "RED")
						spring_wbt.SetAttValue("SigState", "RED")
						spring_sbLT.SetAttValue("SigState", "RED")

						# West Peachtree
						westpeachtree_ebL.SetAttValue("SigState", "RED")
						westpeachtree_ebt.SetAttValue("SigState", "RED")
						westpeachtree_nbLT.SetAttValue("SigState", "RED")
						westpeachtree_wbt.SetAttValue("SigState", "RED")

						# Peachtree
						peachtree_ebLT.SetAttValue("SigState", "RED")
						peachtree_wbLT.SetAttValue("SigState", "RED")
						peachtree_nbLT.SetAttValue("SigState", "RED")
						peachtree_sbLT.SetAttValue("SigState", "RED")

						# Juniper
						juniper_ebt.SetAttValue("SigState", "RED")
						juniper_wbL.SetAttValue("SigState", "RED")
						juniper_wbt.SetAttValue("SigState", "RED")
						juniper_sbLT.SetAttValue("SigState", "RED")

						# Piedmont
						piedmont_ebL.SetAttValue("SigState", "RED")
						piedmont_ebT.SetAttValue("SigState", "RED")
						piedmont_wbT.SetAttValue("SigState", "RED")
						piedmont_nbLT.SetAttValue("SigState", "RED")

						# Central park
						centralpark_ebLT.SetAttValue("SigState", "RED")
						centralpark_wbLT.SetAttValue("SigState", "RED")
						centralpark_sbLT.SetAttValue("SigState", "RED")
						centralpark_nbLT.SetAttValue("SigState", "RED")

						# Hunt
						hunt_ebLT.SetAttValue("SigState", "RED")
						hunt_wbLT.SetAttValue("SigState", "RED")
						hunt_sbLT.SetAttValue("SigState", "RED")
						hunt_nbLT.SetAttValue("SigState", "RED")

						# Parkway
						parkway_ebLT.SetAttValue("SigState", "RED")
						parkway_wbLT.SetAttValue("SigState", "RED")
						parkway_sbLT.SetAttValue("SigState", "RED")
						parkway_nbLT.SetAttValue("SigState", "RED")

						# Boulevard
						boulevard_ebLT.SetAttValue("SigState", "RED")
						boulevard_wbLT.SetAttValue("SigState", "RED")
						boulevard_sbLT.SetAttValue("SigState", "RED")
						boulevard_nbLT.SetAttValue("SigState", "RED")

					

			##	  #Fetch signal data for i/10 and set p=0

					#Set by default the intersections previous signal data as null
					previous_glen_iris=[]
					previous_pcm=[]
					previous_state=[]
					previous_techparkway=[]
					previous_techwood=[]
					previous_connector=[]
					previous_spring=[]
					previous_wpeachtree=[]
					previous_peachtree=[]
					previous_juniper=[]
					previous_piedmont=[]
					previous_centralpark=[]
					previous_hunt=[]
					previous_parkway=[]
					previous_boulevard=[]
					previous_freedom=[]

					#Set flags for signal changes for all intersections
					flag_glen_iris=0
					flag_pcm=0
					flag_state=0
					flag_techparkway=0
					flag_techwood=0
					flag_connector=0
					flag_spring=0
					flag_wpeachtree=0
					flag_peachtree=0
					flag_juniper=0
					flag_piedmont=0
					flag_centralpark=0
					flag_hunt=0
					flag_parkway=0
					flag_boulevard=0
					flag_freedom=0

					flag_rbc_glen_iris=0
					flag_rbc_pcm=0
					flag_rbc_state=0
					flag_rbc_techparkway=0
					flag_rbc_techwood=0
					flag_rbc_connector=0
					flag_rbc_spring=0
					flag_rbc_wpeachtree=0
					flag_rbc_peachtree=0
					flag_rbc_juniper=0
					flag_rbc_piedmont=0
					flag_rbc_centralpark=0
					flag_rbc_hunt=0
					flag_rbc_parkway=0
					flag_rbc_boulevard=0
					flag_rbc_freedom=0

					#####NEW CODE#######################################
					#if(math.floor(Vissim.Simulation.SimulationSecond))==(int(i//10)):
						## fetch signal hexcodes for all intersections ##
						#all_hex = getAllHex_1(sig_simtime, sig_sttime, swt)
					sig_simtime = start_sim_wall_clock-424
					print (start_sim_wall_clock)
					print (sig_simtime)
					# sig_simtime_frmt = dt.datetime.utcfromtimestamp(sig_simtime+simTime).strftime("%H:%M:%S")					
					# print ("Sig Data Requested For - "+ str(sig_simtime_frmt))
					all_hex = getLiveSignal(sig_simtime, simTime)
					if (all_hex[0]!=[]):
						flag_state=1
						if all_hex[0]==-1:
							flag_rbc_state = 1
							print ("State Change for State St.")
						elif all_hex[0]==2:
							flag_rbc_state = 1
							print ("State Operating on rbc")
						else:
							flag_rbc_state = 0
							hex_string_state=all_hex[0]
							binary_string_state = (bin(int('1'+hex_string_state, 16))[3:]).zfill(4)

					if (all_hex[1]!=[]):
						flag_techparkway=1
						
						if all_hex[1]==-1:
							flag_rbc_techparkway = 1
						elif all_hex[1]==2:
							flag_rbc_techparkway = 1
							print ("Tech parkway Operating on rbc")
						else:
							flag_rbc_techparkway = 0
							hex_string_techparkway=all_hex[1]
							binary_string_techparkway = (bin(int('1'+hex_string_techparkway, 16))[3:]).zfill(4)

					if (all_hex[2]!=[]) :
						flag_techwood=1
						
						if all_hex[2]==-1:
							flag_rbc_techwood = 1
						elif all_hex[2]==2:
							flag_rbc_techwood = 1
							print ("Techwood Operating on rbc")
						else:
							flag_rbc_techwood = 0
							hex_string_techwood=all_hex[2]
							binary_string_techwood = (bin(int('1'+hex_string_techwood, 16))[3:]).zfill(4)

					if (all_hex[3]!=[]) :
						flag_connector=1
						
						if all_hex[3]==-1:
							flag_rbc_connector = 1
						elif all_hex[3]==2:
							flag_rbc_connector = 1
							print ("Connector Operating on rbc")
						else:
							flag_rbc_connector = 0
							hex_string_connector=all_hex[3]
							binary_string_connector = (bin(int('1'+hex_string_connector, 16))[3:]).zfill(4)

					if (all_hex[4]!=[]) :
						flag_spring=1
						
						if all_hex[4]==-1:
							flag_rbc_spring = 1
						elif all_hex[4]==2:
							flag_rbc_spring = 1
							print ("Spring Operating on rbc")
						else:
							flag_rbc_spring = 0
							hex_string_spring=all_hex[4]
							binary_string_spring = (bin(int('1'+hex_string_spring, 16))[3:]).zfill(4)

					if (all_hex[5]!=[]):
						flag_wpeachtree=1
						
						if all_hex[5]==-1:
							flag_rbc_wpeachtree = 1
						elif all_hex[5]==2:
							flag_rbc_wpeachtree = 1
							print ("West Peachtree Operating on rbc")
						else:
							flag_rbc_wpeachtree = 0
							hex_string_wpeachtree=all_hex[5]
							binary_string_wpeachtree = (bin(int('1'+hex_string_wpeachtree, 16))[3:]).zfill(4)

					if (all_hex[6]!=[]) :
						flag_peachtree=1
						
						if all_hex[6]==-1:
							flag_rbc_peachtree = 1
						elif all_hex[6]==2:
							flag_rbc_peachtree = 1
							print ("Peachtree Operating on rbc")
						else:
							flag_rbc_peachtree = 0
							hex_string_peachtree=all_hex[6]
							binary_string_peachtree = (bin(int('1'+hex_string_peachtree, 16))[3:]).zfill(4)

					if (all_hex[7]!=[]) :
						flag_juniper=1
						
						if all_hex[7]==-1:
							flag_rbc_juniper = 1
						elif all_hex[7]==2:
							flag_rbc_juniper = 1
							print ("Juniper Operating on rbc")
						else:
							flag_rbc_juniper = 0
							hex_string_juniper=all_hex[7]
							binary_string_juniper = (bin(int('1'+hex_string_juniper, 16))[3:]).zfill(4)

					if (all_hex[8]!=[]) :
						flag_piedmont=1

						if all_hex[8]==-1:
							flag_rbc_piedmont = 1
						elif all_hex[8]==2:
							flag_rbc_piedmont = 1
							print ("Piedmont Operating on rbc")
						else:
							flag_rbc_piedmont = 0
							hex_string_piedmont=all_hex[8]
							binary_string_piedmont = (bin(int('1'+hex_string_piedmont, 16))[3:]).zfill(4) 

					if (all_hex[9]!=[]):
						flag_hunt=1
						if all_hex[9]==-1:
							flag_rbc_hunt = 1
						elif all_hex[9]==2:
							flag_rbc_hunt = 1
							print ("Hunt Operating on rbc")
						else:
							flag_rbc_hunt = 0
							hex_string_hunt=all_hex[9]
							binary_string_hunt = (bin(int('1'+hex_string_hunt, 16))[3:]).zfill(4)

					if (all_hex[10]!=[]):
						flag_parkway=1
						if all_hex[10]==-1:
							flag_rbc_parkway = 1
						elif all_hex[10]==2:
							flag_rbc_parkway = 1
							print ("Parkway Operating on rbc")
						else:
							flag_rbc_parkway = 0
							hex_string_parkway=all_hex[10]
							binary_string_parkway = (bin(int('1'+hex_string_parkway, 16))[3:]).zfill(4)

					if (all_hex[11]!=[]):
						flag_boulevard=1
						if all_hex[11]==-1:
							flag_rbc_boulevard = 1
						elif all_hex[11]==2:
							flag_rbc_boulevard = 1
							print ("Boulevard Operating on rbc")
						else:
							flag_rbc_boulevard = 0
							hex_string_boulevard=all_hex[11]
							binary_string_boulevard = (bin(int('1'+hex_string_boulevard, 16))[3:]).zfill(4)

					if (all_hex[12]!=[]):
						flag_glen_iris=1
						if all_hex[12]==-1:
							flag_rbc_glen_iris = 1
						elif all_hex[12]==2:
							flag_rbc_glen_iris = 1
							print ("Glen Iris Operating on rbc")
						else:
							flag_rbc_glen_iris = 0
							hex_string_glen_iris=all_hex[12]
							binary_string_glen_iris = (bin(int('1'+hex_string_glen_iris, 16))[3:]).zfill(4)

					if (all_hex[13]!=[]) :
						flag_pcm=1
						if all_hex[13]==-1:
							flag_rbc_pcm = 1
						elif all_hex[13]==2:
							flag_rbc_pcm = 1
							print ("PCM Operating on rbc")
						else:
							flag_rbc_pcm = 0
							hex_string_pcm=all_hex[13]
							binary_string_pcm = (bin(int('1'+hex_string_pcm, 16))[3:]).zfill(4)

					if (all_hex[14]!=[]) :
						flag_freedom=1
						if all_hex[14]==-1:
							flag_rbc_freedom = 1
						elif all_hex[14]==2:
							flag_rbc_freedom = 1
							print ("Freedom Operating on rbc")
						else:
							flag_rbc_freedom = 0
							hex_string_freedom=all_hex[14]
							binary_string_freedom = (bin(int('1'+hex_string_freedom, 16))[3:]).zfill(4)

					if (all_hex[15]!=[]):
						flag_centralpark=1
						if all_hex[15]==-1:
							flag_rbc_centralpark = 1
						elif all_hex[15]==2:
							flag_rbc_centralpark = 1
							print ("Central Park Operating on rbc")
						else:
							flag_rbc_centralpark = 0
							hex_string_centralpark=all_hex[15]
							binary_string_centralpark = (bin(int('1'+hex_string_centralpark, 16))[3:]).zfill(4)
							
							
					 ######If any of the intersection flag value is 1, that is it requires to be changed, then go ahead and change else skip#######################################################   
					if (flag_glen_iris>0 or flag_pcm>0 or flag_state>0 or flag_techparkway>0 or flag_techwood>0 or flag_wpeachtree>0 or flag_peachtree>0 or flag_hunt>0 or flag_piedmont>0 or flag_boulevard>0 or flag_centralpark>0 or flag_parkway>0 or flag_spring>0 or flag_connector>0 or flag_freedom>0 or flag_juniper>0):			 
						
						if (flag_glen_iris>0):
							if flag_rbc_glen_iris == 1:
								print ('Switching GLEN IRIS to RBC '+str(i))
								obj_ebL.SetAttValue("ContrByCOM", False)
								obj_ebt1.SetAttValue("ContrByCOM", False)
								obj_ebt2.SetAttValue("ContrByCOM", False)
								obj_ebt3.SetAttValue("ContrByCOM", False)
								obj_nbL.SetAttValue("ContrByCOM", False)
								obj_sbt1.SetAttValue("ContrByCOM", False)
								obj_wbL.SetAttValue("ContrByCOM", False)
								obj_wbt1.SetAttValue("ContrByCOM", False)
								obj_wbt2.SetAttValue("ContrByCOM", False)
								obj_sbL.SetAttValue("ContrByCOM", False)
								obj_nbt1.SetAttValue("ContrByCOM", False)
							else:
								print ('in here - GLEN IRIS IN IN  '+str(i))
								#print (hex_string_glen_iris)
								#print (sig_ttime)

								#Phase 1 config update
								if int(binary_string_glen_iris[23])==1:
									obj_ebL.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[15])==1:
									obj_ebL.SetAttValue("SigState","AMBER")
								elif int(binary_string_glen_iris[7])==1:
									obj_ebL.SetAttValue("SigState","RED")
								else:
									obj_ebL.SetAttValue("SigState","RED")

								#Phase 6 config update
								if int(binary_string_glen_iris[18])==1:
									obj_ebt1.SetAttValue("SigState","GREEN")
									obj_ebt2.SetAttValue("SigState","GREEN")
									obj_ebt3.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[10])==1:
									obj_ebt1.SetAttValue("SigState","AMBER")
									obj_ebt2.SetAttValue("SigState","AMBER")
									obj_ebt3.SetAttValue("SigState","AMBER")
									print ("p")
									print ("works")
								elif int(binary_string_glen_iris[2])==1:
									obj_ebt1.SetAttValue("SigState","RED")
									obj_ebt2.SetAttValue("SigState","RED")
									obj_ebt3.SetAttValue("SigState","RED")
								else:
									obj_ebt1.SetAttValue("SigState","RED")
									obj_ebt2.SetAttValue("SigState","RED")
									obj_ebt3.SetAttValue("SigState","RED")

								#Phase 7 config update
								if int(binary_string_glen_iris[17])==1:
									obj_nbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[9])==1:
									obj_nbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_glen_iris[1])==1:
									obj_nbL.SetAttValue("SigState","RED")
								else:
									obj_nbL.SetAttValue("SigState","RED")

								#Phase 8 config update
								if int(binary_string_glen_iris[16])==1:
									obj_sbt1.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[8])==1:
									obj_sbt1.SetAttValue("SigState","AMBER")
								elif int(binary_string_glen_iris[0])==1:
									obj_sbt1.SetAttValue("SigState","RED")
								else:
									obj_sbt1.SetAttValue("SigState","RED")
									
								#Phase 5 config update
								if int(binary_string_glen_iris[19])==1:
									obj_wbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[11])==1:
									obj_wbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_glen_iris[3])==1:
									obj_wbL.SetAttValue("SigState","RED")
								else:
									obj_wbL.SetAttValue("SigState","RED")

								#Phase 2 config update
								if int(binary_string_glen_iris[22])==1:
									obj_wbt1.SetAttValue("SigState","GREEN")
									obj_wbt2.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[14])==1:
									obj_wbt1.SetAttValue("SigState","AMBER")
									obj_wbt2.SetAttValue("SigState","AMBER")
								elif int(binary_string_glen_iris[6])==1:
									obj_wbt1.SetAttValue("SigState","RED")
									obj_wbt2.SetAttValue("SigState","RED")
								else:
									obj_wbt1.SetAttValue("SigState","RED")
									obj_wbt2.SetAttValue("SigState","RED")
											
								#Phase 3 config update
								if int(binary_string_glen_iris[21])==1:
									obj_sbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[13])==1:
									obj_sbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_glen_iris[5])==1:
									obj_sbL.SetAttValue("SigState","RED")
								else:
									obj_sbL.SetAttValue("SigState","RED")

								#Phase 4 Config update
								if int(binary_string_glen_iris[20])==1:
									obj_nbt1.SetAttValue("SigState","GREEN")
								elif int(binary_string_glen_iris[12])==1:
									obj_nbt1.SetAttValue("SigState","AMBER")
								elif int(binary_string_glen_iris[4])==1:
									obj_nbt1.SetAttValue("SigState","RED")
								else:
									obj_nbt1.SetAttValue("SigState","RED")
								


							# Print Signal States
							EBL_number =1
							EBT_number =6
							WBL_number =5
							WBT_number =2
							NBL_number =7
							NBT_number =4
							SBL_number =3
							SBT_number =8
								
							State_of_EBL_gleniris = Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(EBL_number).AttValue('SigState')
							State_of_EBT_gleniris = Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(EBT_number).AttValue('SigState')
							State_of_WBL_gleniris = Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(WBL_number).AttValue('SigState')
							State_of_WBT_gleniris = Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(WBT_number).AttValue('SigState')

							State_of_NBL_gleniris= Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(NBL_number).AttValue('SigState')
							State_of_NBT_gleniris= Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(NBT_number).AttValue('SigState')
							State_of_SBL_gleniris= Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(SBL_number).AttValue('SigState')
							State_of_SBT_gleniris = Vissim.Net.SignalControllers.ItemByKey(14).SGs.ItemByKey(SBT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (EBL_number,State_of_EBL_gleniris ))
							print ('Actual state of SignalHead(%d) is: %s' % (EBT_number,State_of_EBT_gleniris ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBL_number,State_of_WBL_gleniris ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_gleniris ))
							print ('Actual state of SignalHead(%d) is: %s' % (NBL_number,State_of_NBL_gleniris ))
							print ('Actual state of SignalHead(%d) is: %s' % (NBT_number,State_of_NBT_gleniris ))
							print ('Actual state of SignalHead(%d) is: %s' % (SBL_number,State_of_SBL_gleniris ))
							print ('Actual state of SignalHead(%d) is: %s' % (SBT_number,State_of_SBT_gleniris ))
							signal_json_gleniris={'4807': '%s|%s|%s|%s|%s|%s|%s|%s'%(State_of_EBL_gleniris, State_of_WBT_gleniris, State_of_SBL_gleniris, State_of_NBT_gleniris, State_of_WBL_gleniris, State_of_EBT_gleniris, State_of_NBL_gleniris, State_of_SBT_gleniris)}
							json_list_signals.append(signal_json_gleniris)

						if (flag_pcm>0):
							if flag_rbc_pcm == 1:
								print ('Switching PCM to RBC '+str(i))
								ponce_ebL.SetAttValue("ContrByCOM", False)
								ponce_ebt1.SetAttValue("ContrByCOM", False)
								ponce_ebt2.SetAttValue("ContrByCOM", False)
								ponce_nbLT.SetAttValue("ContrByCOM", False)
								ponce_wbL.SetAttValue("ContrByCOM", False)
								ponce_wbt1.SetAttValue("ContrByCOM", False)
								ponce_wbt2.SetAttValue("ContrByCOM", False)
								ponce_sbL.SetAttValue("ContrByCOM", False)
								ponce_sbt1.SetAttValue("ContrByCOM", False)


							else:						
								print ('in here - PONCE MARKET '+str(i))
								# check if it needs signal status change
								print ("PCM Enter")
								print (hex_string_pcm)
								#print (sig_ttime)
								
								#Phase 1 Config Update
								if int(binary_string_pcm[23])==1:
									ponce_ebL.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_pcm[15])==1:
									ponce_ebL.SetAttValue("SigState","AMBER")
								
								elif int(binary_string_pcm[7])==1:
									ponce_ebL.SetAttValue("SigState","RED")
									
								else:
									ponce_ebL.SetAttValue("SigState","RED")

								#Phase 2 Config Update
								if int(binary_string_pcm[22])==1:
									ponce_wbL.SetAttValue("SigState","GREEN")
									ponce_wbt1.SetAttValue("SigState","GREEN")
									ponce_wbt2.SetAttValue("SigState","GREEN")
								elif int(binary_string_pcm[14])==1:
									ponce_wbL.SetAttValue("SigState","AMBER")
									ponce_wbt1.SetAttValue("SigState","AMBER")
									ponce_wbt2.SetAttValue("SigState","AMBER")
									print ("p1")
									print ("works1")
								elif int(binary_string_pcm[6])==1:
									ponce_wbL.SetAttValue("SigState","RED")
									ponce_wbt1.SetAttValue("SigState","RED")
									ponce_wbt2.SetAttValue("SigState","RED")
								else:
									ponce_wbL.SetAttValue("SigState","RED")
									ponce_wbt1.SetAttValue("SigState","RED")
									ponce_wbt2.SetAttValue("SigState","RED")

								#Phase 3 Config Update
								if int(binary_string_pcm[21])==1:
									ponce_sbL.SetAttValue("SigState","GREEN")
							
								elif int(binary_string_pcm[13])==1:
									ponce_sbL.SetAttValue("SigState","AMBER")
									print ("p1")
									print ("works1")
									
								elif int(binary_string_pcm[5])==1:
									ponce_sbL.SetAttValue("SigState","RED")
								   
								else:
									ponce_sbL.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_pcm[20])==1:
									ponce_nbLT.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_pcm[12])==1:
									ponce_nbLT.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_pcm[4])==1:
									ponce_nbLT.SetAttValue("SigState","RED")
									
								else:
									ponce_nbLT.SetAttValue("SigState","RED")

								#Phase 6 Config Update
								if int(binary_string_pcm[18])==1:
									ponce_ebt1.SetAttValue("SigState","GREEN")
									ponce_ebt2.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_pcm[10])==1:
									ponce_ebt1.SetAttValue("SigState","AMBER")
									ponce_ebt2.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_pcm[2])==1:
									ponce_ebt1.SetAttValue("SigState","RED")
									ponce_ebt2.SetAttValue("SigState","RED")
									
								else:
									ponce_ebt1.SetAttValue("SigState","RED")
									ponce_ebt2.SetAttValue("SigState","RED")
										

								#Phase 8 Config Update
								if int(binary_string_pcm[16])==1:
									ponce_sbt1.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_pcm[8])==1:
									ponce_sbt1.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_pcm[0])==1:
									ponce_sbt1.SetAttValue("SigState","RED")
									
								else:
									ponce_sbt1.SetAttValue("SigState","RED")
									
							# Print Signal States
							EBL_number =1
							EBT_number =6
							WBL_number =2
							WBT_number =2
							NBL_number =4
							NBT_number =4
							SBL_number =3
							SBT_number =8
								
							State_of_EBL_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(EBL_number).AttValue('SigState')
							State_of_EBT_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(EBT_number).AttValue('SigState')
							State_of_WBL_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(WBL_number).AttValue('SigState')
							State_of_WBT_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(WBT_number).AttValue('SigState')

							State_of_NBL_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(NBL_number).AttValue('SigState')
							State_of_NBT_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(NBT_number).AttValue('SigState')
							State_of_SBL_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(SBL_number).AttValue('SigState')
							State_of_SBT_Ponce = Vissim.Net.SignalControllers.ItemByKey(15).SGs.ItemByKey(SBT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (EBL_number,State_of_EBL_Ponce))
							print ('Actual state of SignalHead(%d) is: %s' % (EBT_number,State_of_EBT_Ponce))
							print ('Actual state of SignalHead(%d) is: %s' % (WBL_number,State_of_WBL_Ponce))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_Ponce))
							print ('Actual state of SignalHead(%d) is: %s' % (NBL_number,State_of_NBL_Ponce))
							print ('Actual state of SignalHead(%d) is: %s' % (NBT_number,State_of_NBT_Ponce))
							print ('Actual state of SignalHead(%d) is: %s' % (SBL_number,State_of_SBL_Ponce))
							print ('Actual state of SignalHead(%d) is: %s' % (SBT_number,State_of_SBT_Ponce))
							signal_json_ponce={'4808': '%s|%s|%s|%s|%s|%s'%(State_of_EBL_Ponce, State_of_WBL_Ponce, State_of_SBL_Ponce, State_of_NBT_Ponce, State_of_EBT_Ponce, State_of_SBT_Ponce)}
							json_list_signals.append(signal_json_ponce)

						if (flag_state>0):
							if flag_rbc_state == 1:
								print ('Switching State to RBC '+str(i))
								state_ebLT.SetAttValue("ContrByCOM", False)
								state_wbt.SetAttValue("ContrByCOM", False)
								state_sbL.SetAttValue("ContrByCOM", False)
								
							else:					   
								print ('in here - STATE '+str(i))
								# check if it needs signal status change
								print ("STATE enter")
								print (hex_string_state)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_state[22])==1:
									state_ebLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_state[14])==1:
									state_ebLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_state[6])==1:
									state_ebLT.SetAttValue("SigState","RED")
								else:
									state_ebLT.SetAttValue("SigState","RED")

								#Phase 6 Config Update
								if int(binary_string_state[18])==1:
									state_wbt.SetAttValue("SigState","GREEN")
								elif int(binary_string_state[10])==1:
									state_wbt.SetAttValue("SigState","AMBER")
								elif int(binary_string_state[2])==1:
									state_wbt.SetAttValue("SigState","RED")
								else:
									state_wbt.SetAttValue("SigState","RED")
									
								#Phase 8 Config Update
								if int(binary_string_state[16])==1:
									state_sbL.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_state[8])==1:
									state_sbL.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_state[0])==1:
									state_sbL.SetAttValue("SigState","RED")
									
								else:
									state_sbL.SetAttValue("SigState","RED")
								


							# Print Signal States
							EBLT_number =2
							WBT_number =6
							SBL_number =8
							
								
							State_of_EBLT_state = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_WBT_state = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(WBT_number).AttValue('SigState')
							State_of_SBL_state = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(SBL_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_state ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_state ))
							print ('Actual state of SignalHead(%d) is: %s' % (SBL_number,State_of_SBL_state ))
							signal_json_state={'4794': '%s|%s|%s'%(State_of_EBLT_state, State_of_WBT_state, State_of_SBL_state)}
							json_list_signals.append(signal_json_state)

						if (flag_techparkway>0):
							if flag_rbc_techparkway == 1:
								print ('Switching TechParkway to RBC '+str(i))
								techparkway_ebLT.SetAttValue("ContrByCOM", False)
								techparkway_nbL.SetAttValue("ContrByCOM", False)
								techparkway_nbt.SetAttValue("ContrByCOM", False) 
								techparkway_wbL.SetAttValue("ContrByCOM", False)
								techparkway_wbt1.SetAttValue("ContrByCOM", False)
								techparkway_sbL.SetAttValue("ContrByCOM", False)
								techparkway_sbt1.SetAttValue("ContrByCOM", False)

							else:											   
								print ('in here - TECH PARKWAY '+str(i))
								# check if it needs signal status change
								print ("TECH PARKWAY enter")
								print (hex_string_techparkway)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_techparkway[22])==1:
									techparkway_wbt1.SetAttValue("SigState","GREEN")
								elif int(binary_string_techparkway[14])==1:
									techparkway_wbt1.SetAttValue("SigState","AMBER")
								elif int(binary_string_techparkway[6])==1:
									techparkway_wbt1.SetAttValue("SigState","RED")
								else:
									techparkway_wbt1.SetAttValue("SigState","RED")

								#Phase 3 Config Update
								if int(binary_string_techparkway[21])==1:
									techparkway_sbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_techparkway[13])==1:
									techparkway_sbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_techparkway[5])==1:
									techparkway_sbL.SetAttValue("SigState","RED")
								else:
									techparkway_sbL.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_techparkway[20])==1:
									techparkway_nbt.SetAttValue("SigState","GREEN")
								elif int(binary_string_techparkway[12])==1:
									techparkway_nbt.SetAttValue("SigState","AMBER")
								elif int(binary_string_techparkway[4])==1:
									techparkway_nbt.SetAttValue("SigState","RED")
								else:
									techparkway_nbt.SetAttValue("SigState","RED")
									
								#Phase 5 Config Update
								if int(binary_string_techparkway[19])==1:
									techparkway_wbL.SetAttValue("SigState","GREEN")  
								elif int(binary_string_techparkway[11])==1:
									techparkway_wbL.SetAttValue("SigState","AMBER")   
								elif int(binary_string_techparkway[3])==1:
									techparkway_wbL.SetAttValue("SigState","RED")  
								else:
									techparkway_wbL.SetAttValue("SigState","RED")
									
								#Phase 6 Config Update
								if int(binary_string_techparkway[18])==1:
									techparkway_ebLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_techparkway[10])==1:
									techparkway_ebLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_techparkway[2])==1:
									techparkway_ebLT.SetAttValue("SigState","RED")
								else:
									techparkway_ebLT.SetAttValue("SigState","RED")   
								
								#Phase 7 Config Update
								if int(binary_string_techparkway[17])==1:
									techparkway_nbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_techparkway[9])==1:
									techparkway_nbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_techparkway[1])==1:
									techparkway_nbL.SetAttValue("SigState","RED")
								else:
									techparkway_nbL.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_techparkway[16])==1:
									techparkway_sbt1.SetAttValue("SigState","GREEN")
								elif int(binary_string_techparkway[8])==1:
									techparkway_sbt1.SetAttValue("SigState","AMBER")
								elif int(binary_string_techparkway[0])==1:
									techparkway_sbt1.SetAttValue("SigState","RED")
								else:
									techparkway_sbt1.SetAttValue("SigState","RED")

							# Print Signal States
							EBLT_number =6
							WBL_number =5
							WBT_number =2
							SBL_number =3
							NBL_number =7
							NBT_number =4
							SBT_number =8
							
							State_of_EBLT_techparkway = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_WBL_techparkway = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(WBL_number).AttValue('SigState')
							State_of_WBT_techparkway = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(WBT_number).AttValue('SigState')
							State_of_SBL_techparkway = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(SBL_number).AttValue('SigState')
							State_of_NBL_techparkway = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(NBL_number).AttValue('SigState')
							State_of_NBT_techparkway = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(NBT_number).AttValue('SigState')
							State_of_SBT_techparkway = Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(SBT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_techparkway))
							print ('Actual state of SignalHead(%d) is: %s' % (WBL_number,State_of_WBL_techparkway))
							print ('Actual state of SignalHead(%d) is: %s' % (SBL_number,State_of_SBL_techparkway))
							print ('Actual state of SignalHead(%d) is: %s' % (NBL_number,State_of_NBL_techparkway))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_techparkway))
							print ('Actual state of SignalHead(%d) is: %s' % (NBT_number,State_of_NBT_techparkway))
							print ('Actual state of SignalHead(%d) is: %s' % (SBT_number,State_of_SBT_techparkway))
							signal_json_techparkway={'4795': '%s|%s|%s|%s|%s|%s|%s'%(State_of_WBT_techparkway, State_of_SBL_techparkway, State_of_NBT_techparkway, State_of_WBL_techparkway, State_of_EBLT_techparkway, State_of_NBL_techparkway, State_of_SBT_techparkway)}
							json_list_signals.append(signal_json_techparkway)

						if (flag_techwood>0):
							if flag_rbc_techwood == 1:
								print ('Switching Techwood to RBC '+str(i)) 
								techwood_ebL.SetAttValue("ContrByCOM", False)
								techwood_nbt.SetAttValue("ContrByCOM", False)
								techwood_wbL.SetAttValue("ContrByCOM", False) 
								techwood_wbt1.SetAttValue("ContrByCOM", False)
								techwood_sbL.SetAttValue("ContrByCOM", False)
								techwood_sbt1.SetAttValue("ContrByCOM", False)

							else:						 
								print ('in here - TECHWOOD '+str(i))
								# check if it needs signal status change
								print ("TECHWOOD enter")
								print (hex_string_techwood)
								#print (sig_ttime)

								#Phase 1 Config Update
								if int(binary_string_techwood[23])==1:
									techwood_ebL.SetAttValue("SigState","GREEN")
								elif int(binary_string_techwood[15])==1:
									techwood_ebL.SetAttValue("SigState","AMBER")
								elif int(binary_string_techwood[7])==1:
									techwood_ebL.SetAttValue("SigState","RED")
								else:
									techwood_ebL.SetAttValue("SigState","RED")

								#Phase 2 Config Update
								if int(binary_string_techwood[22])==1:
									techwood_wbt1.SetAttValue("SigState","GREEN")
								elif int(binary_string_techwood[14])==1:
									techwood_wbt1.SetAttValue("SigState","AMBER")
								elif int(binary_string_techwood[6])==1:
									techwood_wbt1.SetAttValue("SigState","RED")
								else:
									techwood_wbt1.SetAttValue("SigState","RED")

								#Phase 3 Config Update
								if int(binary_string_techwood[21])==1:
									techwood_sbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_techwood[13])==1:
									techwood_sbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_techwood[5])==1:
									techwood_sbL.SetAttValue("SigState","RED")
								else:
									techwood_sbL.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_techwood[20])==1:
									techwood_nbt.SetAttValue("SigState","GREEN")
								elif int(binary_string_techwood[12])==1:
									techwood_nbt.SetAttValue("SigState","AMBER")
								elif int(binary_string_techwood[4])==1:
									techwood_nbt.SetAttValue("SigState","RED")
								else:
									techwood_nbt.SetAttValue("SigState","RED")
									
								#Phase 5 Config Update
								if int(binary_string_techwood[19])==1:
									techwood_wbL.SetAttValue("SigState","GREEN")  
								elif int(binary_string_techwood[11])==1:
									techwood_wbL.SetAttValue("SigState","AMBER")   
								elif int(binary_string_techwood[3])==1:
									techwood_wbL.SetAttValue("SigState","RED")  
								else:
									techwood_wbL.SetAttValue("SigState","RED")
									
								#Phase 6 Config Update
								if int(binary_string_techwood[18])==1:
									techwood_ebt1.SetAttValue("SigState","GREEN")
								elif int(binary_string_techwood[10])==1:
									techwood_ebt1.SetAttValue("SigState","AMBER")
								elif int(binary_string_techwood[2])==1:
									techwood_ebt1.SetAttValue("SigState","RED")
								else:
									techwood_ebt1.SetAttValue("SigState","RED")   
								
								#Phase 7 Config Update
								if int(binary_string_techwood[17])==1:
									techwood_nbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_techwood[9])==1:
									techwood_nbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_techwood[1])==1:
									techwood_nbLT.SetAttValue("SigState","RED")
								else:
									techwood_nbLT.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_techwood[16])==1:
									techwood_sbt1.SetAttValue("SigState","GREEN")
								elif int(binary_string_techwood[8])==1:
									techwood_sbt1.SetAttValue("SigState","AMBER")
								elif int(binary_string_techwood[0])==1:
									techwood_sbt1.SetAttValue("SigState","RED")
								else:
									techwood_sbt1.SetAttValue("SigState","RED")
							
								
							#print i

							# Print Signal States
							EBL_number=1
							WBT_number=2
							SBL_number=3
							NBT_number=4
							WBL_number=5
							EBT_number=6
							NBLT_number=7
							SBT_number=8
							
								
							State_of_EBL_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(EBL_number).AttValue('SigState')
							State_of_WBT_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(WBT_number).AttValue('SigState')
							State_of_SBL_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(SBL_number).AttValue('SigState')
							State_of_NBT_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(NBT_number).AttValue('SigState')
							State_of_WBL_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(WBL_number).AttValue('SigState')
							State_of_EBT_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(EBT_number).AttValue('SigState')
							State_of_NBLT_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(NBLT_number).AttValue('SigState')
							State_of_SBT_techwood = Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(SBT_number).AttValue('SigState')
						

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_EBL_techwood ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_techwood ))
							print ('Actual state of SignalHead(%d) is: %s' % (SBL_number,State_of_SBL_techwood ))
							print ('Actual state of SignalHead(%d) is: %s' % (NBT_number,State_of_NBT_techwood ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBL_number,State_of_WBL_techwood ))
							print ('Actual state of SignalHead(%d) is: %s' % (EBT_number,State_of_EBT_techwood ))
							print ('Actual state of SignalHead(%d) is: %s' % (EBL_number,State_of_NBLT_techwood))
							print ('Actual state of SignalHead(%d) is: %s' % (SBT_number,State_of_SBT_techwood))
							signal_json_techwood={'4796': '%s|%s|%s|%s|%s|%s|%s|%s'%(State_of_EBL_techwood, State_of_WBT_techwood, State_of_SBL_techwood, State_of_NBT_techwood, State_of_WBL_techwood, State_of_EBT_techwood, State_of_NBLT_techwood, State_of_SBT_techwood)}
							json_list_signals.append(signal_json_techwood)

						if (flag_connector>0):
							if flag_rbc_connector == 1:
								print ('Switching Connector to RBC '+str(i))
								i75_ebLT.SetAttValue("ContrByCOM", False)
								i75_wbt1.SetAttValue("ContrByCOM", False)
								i75_sbL.SetAttValue("ContrByCOM", False) 
							else:												 
								print ('in here - CONNECTOR '+str(i))
								# check if it needs signal status change
								print ("CONNECTOR enter")
								print (hex_string_connector)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_connector[22])==1:
									i75_ebLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_connector[14])==1:
									i75_ebLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_connector[6])==1:
									i75_ebLT.SetAttValue("SigState","RED")
								else:
									i75_ebLT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_connector[20])==1:
									i75_sbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_connector[12])==1:
									i75_sbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_connector[4])==1:
									i75_sbL.SetAttValue("SigState","RED")
								else:
									i75_sbL.SetAttValue("SigState","RED")
									
								#Phase 6 Config Update
								if int(binary_string_connector[18])==1:
									i75_wbt1.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_connector[10])==1:
									i75_wbt1.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_connector[2])==1:
									i75_wbt1.SetAttValue("SigState","RED")
									
								else:
									i75_wbt1.SetAttValue("SigState","RED")
								
							#print i	
							
							

							# Print Signal States
							EBLT_number =2
							WBT_number =6
							SBL_number =4
								
							State_of_EBLT_i75 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_WBT_i75 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(WBT_number).AttValue('SigState')
							State_of_SBL_i75 = Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(SBL_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_i75 ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_i75 ))
							print ('Actual state of SignalHead(%d) is: %s' % (SBL_number,State_of_SBL_i75 ))
							signal_json_i75={'4797':'%s|%s|%s'%(State_of_EBLT_i75, State_of_SBL_i75, State_of_WBT_i75)}
							json_list_signals.append(signal_json_i75)


						if (flag_spring>0):
							if flag_rbc_spring == 1:
								print ('Switching Spring to RBC '+str(i))
								spring_ebt.SetAttValue("ContrByCOM", False)
								spring_wbL.SetAttValue("ContrByCOM", False)
								spring_wbt.SetAttValue("ContrByCOM", False)
								spring_sbLT.SetAttValue("ContrByCOM", False) 
							else:						
								print ('in here - SPRING '+str(i))
								# check if it needs signal status change
								print ("SPRING enter STRINGGFG")
								print (binary_string_spring[18])
								print (hex_string_spring)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_spring[22])==1:
									spring_sbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_spring[14])==1:
									spring_sbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_spring[6])==1:
									spring_sbLT.SetAttValue("SigState","RED")
								else:
									spring_sbLT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_spring[20])==1:
									spring_wbt.SetAttValue("SigState","GREEN")
								elif int(binary_string_spring[12])==1:
									spring_wbt.SetAttValue("SigState","AMBER")
								elif int(binary_string_spring[4])==1:
									spring_wbt.SetAttValue("SigState","RED")
								else:
									spring_wbt.SetAttValue("SigState","RED")
									
								#Phase 7 Config Update
								if int(binary_string_spring[17])==1:
									spring_wbL.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_spring[9])==1:
									spring_wbL.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_spring[1])==1:
									spring_wbL.SetAttValue("SigState","RED")
									
								else:
									spring_wbL.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_spring[16])==1:
									spring_ebt.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_spring[8])==1:
									spring_ebt.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_spring[0])==1:
									spring_ebt.SetAttValue("SigState","RED")
									
								else:
									spring_ebt.SetAttValue("SigState","RED")
									
								#print i	
								
							

							# Print Signal States
							SBLT_number =2
							WBT_number =4
							WBL_number =7
							EBT_number =8
								
							State_of_SBLT_Spring = Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(SBLT_number).AttValue('SigState')
							State_of_WBT_Spring = Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(WBT_number).AttValue('SigState')
							State_of_WBL_Spring = Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(WBL_number).AttValue('SigState')
							State_of_EBT_Spring = Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(EBT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (SBLT_number,State_of_SBLT_Spring ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_Spring ))
							print ('Actual state of SignalHead(%d) is: %s' % (WBL_number,State_of_WBL_Spring ))
							print ('Actual state of SignalHead(%d) is: %s' % (EBT_number,State_of_EBT_Spring ))
							signal_json_Spring={'4798':'%s|%s|%s|%s'%(State_of_SBLT_Spring, State_of_WBT_Spring, State_of_WBL_Spring, State_of_EBT_Spring)}
							json_list_signals.append(signal_json_Spring)


						if (flag_wpeachtree>0):
							if flag_rbc_wpeachtree == 1:
								print ('Switching West Peachtree to RBC '+str(i))
								westpeachtree_ebL.SetAttValue("ContrByCOM", False)
								westpeachtree_ebt.SetAttValue("ContrByCOM", False)
								westpeachtree_nbLT.SetAttValue("ContrByCOM", False)
								westpeachtree_wbt.SetAttValue("ContrByCOM", False)  
							else:						
								print ('in here - WEST PEACHTREE '+str(i))
								# check if it needs signal status change
								print ("WEST PEACHTREE enter")
								print (hex_string_wpeachtree)
								#print (sig_ttime)
								
								#Phase 3 Config Update
								if int(binary_string_wpeachtree[21])==1:
									westpeachtree_ebL.SetAttValue("SigState","GREEN")
								elif int(binary_string_wpeachtree[13])==1:
									westpeachtree_ebL.SetAttValue("SigState","AMBER")
								elif int(binary_string_wpeachtree[5])==1:
									westpeachtree_ebL.SetAttValue("SigState","RED")
								else:
									westpeachtree_ebL.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_wpeachtree[20])==1:
									westpeachtree_wbt.SetAttValue("SigState","GREEN")
								elif int(binary_string_wpeachtree[12])==1:
									westpeachtree_wbt.SetAttValue("SigState","AMBER")
								elif int(binary_string_wpeachtree[4])==1:
									westpeachtree_wbt.SetAttValue("SigState","RED")
								else:
									westpeachtree_wbt.SetAttValue("SigState","RED")
									
								#Phase 6 Config Update
								if int(binary_string_wpeachtree[18])==1:
									westpeachtree_nbLT.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_wpeachtree[10])==1:
									westpeachtree_nbLT.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_wpeachtree[2])==1:
									westpeachtree_nbLT.SetAttValue("SigState","RED")
									
								else:
									westpeachtree_nbLT.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_wpeachtree[16])==1:
									westpeachtree_ebt.SetAttValue("SigState","GREEN")
									
								elif int(binary_string_wpeachtree[8])==1:
									westpeachtree_ebt.SetAttValue("SigState","AMBER")
									
								elif int(binary_string_wpeachtree[0])==1:
									westpeachtree_ebt.SetAttValue("SigState","RED")
									
								else:
									westpeachtree_ebt.SetAttValue("SigState","RED")
									
								#print i	
							
							

							# Print Signal States
							EBL_number =3
							WBT_number =4
							NBLT_number =6
							EBT_number =8
								
							State_of_NBLT_wpeachtree = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(NBLT_number).AttValue('SigState')
							State_of_WBT_wpeachtree = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(WBT_number).AttValue('SigState')
							State_of_EBL_wpeachtree = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(EBL_number).AttValue('SigState')
							State_of_EBT_wpeachtree = Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(EBT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_NBLT_wpeachtree))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_wpeachtree))
							print ('Actual state of SignalHead(%d) is: %s' % (EBL_number,State_of_EBL_wpeachtree))
							print ('Actual state of SignalHead(%d) is: %s' % (EBT_number,State_of_EBT_wpeachtree))
							signal_json_wpeachtree={'4799':'%s|%s|%s|%s'%(State_of_EBL_wpeachtree, State_of_WBT_wpeachtree, State_of_NBLT_wpeachtree, State_of_EBT_wpeachtree)}
							json_list_signals.append(signal_json_wpeachtree)


						if (flag_peachtree>0):
							if flag_rbc_peachtree == 1:
								print ('Switching Peachtree to RBC '+str(i))
								peachtree_ebLT.SetAttValue("ContrByCOM", False)
								peachtree_wbLT.SetAttValue("ContrByCOM", False)
								peachtree_nbLT.SetAttValue("ContrByCOM", False)
								peachtree_sbLT.SetAttValue("ContrByCOM", False)  

							else:						
								print ('in here - PEACHTREE '+str(i))
								# check if it needs signal status change
								print ("PEACHTREE enter")
								print (hex_string_peachtree)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_peachtree[22])==1:
									peachtree_ebLT.SetAttValue("SigState","GREEN")
									peachtree_wbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_peachtree[14])==1:
									peachtree_ebLT.SetAttValue("SigState","AMBER")
									peachtree_wbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_peachtree[6])==1:
									peachtree_ebLT.SetAttValue("SigState","RED")
									peachtree_wbLT.SetAttValue("SigState","RED")
								else:
									peachtree_ebLT.SetAttValue("SigState","RED")
									peachtree_wbLT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_peachtree[20])==1:
									peachtree_nbLT.SetAttValue("SigState","GREEN")
									peachtree_sbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_peachtree[12])==1:
									peachtree_nbLT.SetAttValue("SigState","AMBER")
									peachtree_sbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_peachtree[4])==1:
									peachtree_nbLT.SetAttValue("SigState","RED")
									peachtree_sbLT.SetAttValue("SigState","RED")
								else:
									peachtree_nbLT.SetAttValue("SigState","RED")
									peachtree_sbLT.SetAttValue("SigState","RED")
								   

							# Print Signal States
							EBLT_number =2
							WBLT_number =2
							NBLT_number =4
							SBLT_number =4
								
							State_of_EBLT_peachtree = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_WBLT_peachtree = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(WBLT_number).AttValue('SigState')
							State_of_SBLT_peachtree = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(SBLT_number).AttValue('SigState')
							State_of_NBLT_peachtree = Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(NBLT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_NBLT_peachtree))
							print ('Actual state of SignalHead(%d) is: %s' % (WBLT_number,State_of_WBLT_peachtree ))
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_peachtree ))
							print ('Actual state of SignalHead(%d) is: %s' % (SBLT_number,State_of_SBLT_peachtree ))
							signal_json_peachtree={'4800':'%s|%s'%(State_of_EBLT_peachtree, State_of_NBLT_peachtree)}
							json_list_signals.append(signal_json_peachtree)


						if (flag_juniper>0):
							if flag_rbc_juniper == 1:
								juniper_ebt.SetAttValue("ContrByCOM", False)
								juniper_wbL.SetAttValue("ContrByCOM", False)
								juniper_wbt.SetAttValue("ContrByCOM", False)
								juniper_sbLT.SetAttValue("ContrByCOM", False) 
								print ('Switching Peachtree to RBC '+str(i)) 
							else:						
								print ('in here - JUNIPER '+str(i))
								# check if it needs signal status change
								print ("JUNIPER enter")
								print (hex_string_juniper)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_juniper[22])==1:
									juniper_wbt.SetAttValue("SigState","GREEN")
								elif int(binary_string_juniper[14])==1:
									juniper_wbt.SetAttValue("SigState","AMBER")
								elif int(binary_string_juniper[6])==1:
									juniper_wbt.SetAttValue("SigState","RED")
								else:
									juniper_wbt.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_juniper[20])==1:
									juniper_sbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_juniper[12])==1:
									juniper_sbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_juniper[4])==1:
									juniper_sbLT.SetAttValue("SigState","RED")
								else:
									juniper_sbLT.SetAttValue("SigState","RED")

								#Phase 5 Config Update
								if int(binary_string_juniper[19])==1:
									juniper_wbL.SetAttValue("SigState","GREEN")
								elif int(binary_string_juniper[11])==1:
									juniper_wbL.SetAttValue("SigState","AMBER")
								elif int(binary_string_juniper[3])==1:
									juniper_wbL.SetAttValue("SigState","RED")
								else:
									juniper_wbL.SetAttValue("SigState","RED")

								#Phase 6 Config Update
								if int(binary_string_juniper[18])==1:
									juniper_ebt.SetAttValue("SigState","GREEN")
								elif int(binary_string_juniper[10])==1:
									juniper_ebt.SetAttValue("SigState","AMBER")
								elif int(binary_string_juniper[2])==1:
									juniper_ebt.SetAttValue("SigState","RED")
								else:
									juniper_ebt.SetAttValue("SigState","RED")
									   

							# Print Signal States
							WBT_number =2
							SBLT_number =4
							WBL_number =5
							EBT_number =6
								
							State_of_WBT_juniper = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(WBT_number).AttValue('SigState')
							State_of_SBLT_juniper = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(SBLT_number).AttValue('SigState')
							State_of_WBL_juniper = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(WBL_number).AttValue('SigState')
							State_of_EBT_juniper = Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(EBT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (SBLT_number,State_of_SBLT_juniper))
							print ('Actual state of SignalHead(%d) is: %s' % (WBL_number,State_of_WBL_juniper))
							print ('Actual state of SignalHead(%d) is: %s' % (EBT_number,State_of_EBT_juniper))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_juniper))
							signal_json_juniper={'4801':'%s|%s|%s|%s'%(State_of_WBT_juniper, State_of_SBLT_juniper, State_of_WBL_juniper, State_of_EBT_juniper)}
							json_list_signals.append(signal_json_juniper)



						if (flag_piedmont>0):
							if flag_rbc_piedmont == 1:
								print ('Switching Piedmont to RBC '+str(i))
								piedmont_ebL.SetAttValue("ContrByCOM", False)
								piedmont_ebT.SetAttValue("ContrByCOM", False)
								piedmont_wbT.SetAttValue("ContrByCOM", False)
								piedmont_nbLT.SetAttValue("ContrByCOM", False) 
							else:						
								print ('in here - PIEDMONT '+str(i))
								# check if it needs signal status change
								print ("PIEDMONT enter")
								print (hex_string_piedmont)
								#print (sig_ttime)
								
								#Phase 1 Config Update
								if int(binary_string_piedmont[23])==1:
									piedmont_ebL.SetAttValue("SigState","GREEN")
								elif int(binary_string_piedmont[15])==1:
									piedmont_ebL.SetAttValue("SigState","AMBER")
								elif int(binary_string_piedmont[7])==1:
									piedmont_ebL.SetAttValue("SigState","RED")
								else:
									piedmont_ebL.SetAttValue("SigState","RED")
									
								#Phase 2 Config Update
								if int(binary_string_piedmont[22])==1:
									piedmont_wbT.SetAttValue("SigState","GREEN")
								elif int(binary_string_piedmont[14])==1:
									piedmont_wbT.SetAttValue("SigState","AMBER")
								elif int(binary_string_piedmont[6])==1:
									piedmont_wbT.SetAttValue("SigState","RED")
								else:
									piedmont_wbT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_piedmont[20])==1:
									piedmont_nbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_piedmont[12])==1:
									piedmont_nbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_piedmont[4])==1:
									piedmont_nbLT.SetAttValue("SigState","RED")
								else:
									piedmont_nbLT.SetAttValue("SigState","RED")

								
								#Phase 6 Config Update
								if int(binary_string_piedmont[18])==1:
									piedmont_ebT.SetAttValue("SigState","GREEN")
								elif int(binary_string_piedmont[10])==1:
									piedmont_ebT.SetAttValue("SigState","AMBER")
								elif int(binary_string_piedmont[2])==1:
									piedmont_ebT.SetAttValue("SigState","RED")
								else:
									piedmont_ebT.SetAttValue("SigState","RED")
									   

							# Print Signal States
							EBL_number =1
							EBT_number =6
							NBLT_number =4
							WBT_number =2
							
								
							State_of_EBT_piedmont = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(EBT_number).AttValue('SigState')
							State_of_NBLT_piedmont = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(NBLT_number).AttValue('SigState')
							State_of_EBL_piedmont = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(EBL_number).AttValue('SigState')
							State_of_WBT_piedmont = Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(WBT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_NBLT_piedmont))
							print ('Actual state of SignalHead(%d) is: %s' % (EBL_number,State_of_EBL_piedmont))
							print ('Actual state of SignalHead(%d) is: %s' % (EBT_number,State_of_EBT_piedmont))
							print ('Actual state of SignalHead(%d) is: %s' % (WBT_number,State_of_WBT_piedmont))
							signal_json_piedmont={'4802':'%s|%s|%s|%s'%(State_of_EBL_piedmont, State_of_WBT_piedmont, State_of_NBLT_piedmont, State_of_EBT_piedmont)}
							json_list_signals.append(signal_json_piedmont)

						if (flag_centralpark>0):
							if flag_rbc_centralpark == 1:
								print ('Switching Central Park to RBC '+str(i))
								centralpark_ebLT.SetAttValue("ContrByCOM", False)
								centralpark_sbLT.SetAttValue("ContrByCOM", False)
								centralpark_nbLT.SetAttValue("ContrByCOM", False)
								centralpark_wbLT.SetAttValue("ContrByCOM", False)  
							else:						
								print ('in here - CENTRAL PARK '+str(i))
								# check if it needs signal status change
								print ("CENTRAL PARK enter")
								print (hex_string_centralpark)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_centralpark[22])==1:
									centralpark_wbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_centralpark[14])==1:
									centralpark_wbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_centralpark[6])==1:
									centralpark_wbLT.SetAttValue("SigState","RED")
								else:
									centralpark_wbLT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_centralpark[20])==1:
									centralpark_nbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_centralpark[12])==1:
									centralpark_nbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_centralpark[4])==1:
									centralpark_nbLT.SetAttValue("SigState","RED")
								else:
									centralpark_nbLT.SetAttValue("SigState","RED")
								
								#Phase 6 Config Update
								if int(binary_string_centralpark[18])==1:
									centralpark_ebLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_centralpark[10])==1:
									centralpark_ebLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_centralpark[2])==1:
									centralpark_ebLT.SetAttValue("SigState","RED")
								else:
									centralpark_ebLT.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_centralpark[16])==1:
									centralpark_sbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_centralpark[8])==1:
									centralpark_sbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_centralpark[0])==1:
									centralpark_sbLT.SetAttValue("SigState","RED")
								else:
									centralpark_sbLT.SetAttValue("SigState","RED")
									   

							# Print Signal States
							WBLT_number =2
							EBLT_number =6
							NBLT_number =4
							SBLT_number =8
							
								
							State_of_EBLT_centralpark = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_NBLT_centralpark = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(NBLT_number).AttValue('SigState')
							State_of_SBLT_centralpark = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(SBLT_number).AttValue('SigState')
							State_of_WBLT_centralpark = Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(WBLT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_NBLT_centralpark))
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_centralpark))
							print ('Actual state of SignalHead(%d) is: %s' % (WBLT_number,State_of_WBLT_centralpark))
							print ('Actual state of SignalHead(%d) is: %s' % (SBLT_number,State_of_SBLT_centralpark))
							signal_json_centralpark={'7322':'%s|%s|%s|%s'%(State_of_WBLT_centralpark, State_of_NBLT_centralpark, State_of_EBLT_centralpark, State_of_SBLT_centralpark)}
							json_list_signals.append(signal_json_centralpark)



						if (flag_hunt>0):
							if flag_rbc_hunt == 1:
								print ('Switching Hunt to RBC '+str(i))
								hunt_ebLT.SetAttValue("ContrByCOM", False)
								hunt_wbLT.SetAttValue("ContrByCOM", False)
								hunt_sbLT.SetAttValue("ContrByCOM", False)
								hunt_nbLT.SetAttValue("ContrByCOM", False)  
							else:							 
								print ('in here - HUNT '+str(i))
								# check if it needs signal status change
								print ("HUNT enter")
								print (hex_string_hunt)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_hunt[22])==1:
									hunt_ebLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_hunt[14])==1:
									hunt_ebLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_hunt[6])==1:
									hunt_ebLT.SetAttValue("SigState","RED")
								else:
									hunt_ebLT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_hunt[20])==1:
									hunt_nbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_hunt[12])==1:
									hunt_nbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_hunt[4])==1:
									hunt_nbLT.SetAttValue("SigState","RED")
								else:
									hunt_nbLT.SetAttValue("SigState","RED")
								
								#Phase 6 Config Update
								if int(binary_string_hunt[18])==1:
									hunt_wbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_hunt[10])==1:
									hunt_wbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_hunt[2])==1:
									hunt_wbLT.SetAttValue("SigState","RED")
								else:
									hunt_wbLT.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_hunt[16])==1:
									hunt_sbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_hunt[8])==1:
									hunt_sbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_hunt[0])==1:
									hunt_sbLT.SetAttValue("SigState","RED")
								else:
									hunt_sbLT.SetAttValue("SigState","RED")
									   

							# Print Signal States
							WBLT_number =6
							EBLT_number =2
							NBLT_number =4
							SBLT_number =8
							
								
							State_of_EBLT_hunt = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_NBLT_hunt = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(NBLT_number).AttValue('SigState')
							State_of_SBLT_hunt = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(SBLT_number).AttValue('SigState')
							State_of_WBLT_hunt = Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(WBLT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_NBLT_hunt))
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_hunt))
							print ('Actual state of SignalHead(%d) is: %s' % (WBLT_number,State_of_WBLT_hunt))
							print ('Actual state of SignalHead(%d) is: %s' % (SBLT_number,State_of_SBLT_hunt))
							signal_json_hunt={'4804':'%s|%s|%s|%s'%(State_of_EBLT_hunt, State_of_NBLT_hunt, State_of_WBLT_hunt, State_of_SBLT_hunt)}
							json_list_signals.append(signal_json_hunt)

						if (flag_parkway>0):
							if flag_rbc_parkway == 1:
								print ('Switching Parkway to RBC '+str(i))
								parkway_ebLT.SetAttValue("ContrByCOM", False)
								parkway_wbLT.SetAttValue("ContrByCOM", False)
								parkway_sbLT.SetAttValue("ContrByCOM", False)
								parkway_nbLT.SetAttValue("ContrByCOM", False)  
							else:						
								print ('in here - PARKWAY '+str(i))
								# check if it needs signal status change
								print ("PARKWAY enter")
								print (hex_string_parkway)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_parkway[22])==1:
									parkway_ebLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_parkway[14])==1:
									parkway_ebLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_parkway[6])==1:
									parkway_ebLT.SetAttValue("SigState","RED")
								else:
									parkway_ebLT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_parkway[20])==1:
									parkway_nbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_parkway[12])==1:
									parkway_nbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_parkway[4])==1:
									parkway_nbLT.SetAttValue("SigState","RED")
								else:
									parkway_nbLT.SetAttValue("SigState","RED")
								
								#Phase 6 Config Update
								if int(binary_string_parkway[18])==1:
									parkway_wbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_parkway[10])==1:
									parkway_wbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_parkway[2])==1:
									parkway_wbLT.SetAttValue("SigState","RED")
								else:
									parkway_wbLT.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_parkway[16])==1:
									parkway_sbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_parkway[8])==1:
									parkway_sbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_parkway[0])==1:
									parkway_sbLT.SetAttValue("SigState","RED")
								else:
									parkway_sbLT.SetAttValue("SigState","RED")
							   

							# Print Signal States
							WBLT_number =6
							EBLT_number =2
							NBLT_number =4
							SBLT_number =8
							
								
							State_of_EBLT_parkway = Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_NBLT_parkway = Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(NBLT_number).AttValue('SigState')
							State_of_SBLT_parkway = Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(SBLT_number).AttValue('SigState')
							State_of_WBLT_parkway = Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(WBLT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (SBLT_number,State_of_SBLT_parkway))
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_parkway))
							print ('Actual state of SignalHead(%d) is: %s' % (WBLT_number,State_of_WBLT_parkway))
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_NBLT_parkway))
							signal_json_parkway={'4805':'%s|%s|%s|%s'%(State_of_EBLT_parkway, State_of_NBLT_parkway, State_of_WBLT_parkway, State_of_SBLT_parkway)}
							json_list_signals.append(signal_json_parkway)
		#

						if (flag_boulevard>0):
							if flag_rbc_boulevard == 1:
								print ('Switching Boulevard to RBC '+str(i))
								boulevard_ebLT.SetAttValue("ContrByCOM", False)
								boulevard_wbLT.SetAttValue("ContrByCOM", False)
								boulevard_sbLT.SetAttValue("ContrByCOM", False)
								boulevard_nbLT.SetAttValue("ContrByCOM", False) 
							else:						
								print ('in here - BOULEVARD '+str(i))
								# check if it needs signal status change
								print ("BOULEVARD enter")
								print (hex_string_boulevard)
								#print (sig_ttime)
								
								#Phase 2 Config Update
								if int(binary_string_boulevard[22])==1:
									boulevard_ebLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_boulevard[14])==1:
									boulevard_ebLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_boulevard[6])==1:
									boulevard_ebLT.SetAttValue("SigState","RED")
								else:
									boulevard_ebLT.SetAttValue("SigState","RED")

								#Phase 4 Config Update
								if int(binary_string_boulevard[20])==1:
									boulevard_nbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_boulevard[12])==1:
									boulevard_nbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_boulevard[4])==1:
									boulevard_nbLT.SetAttValue("SigState","RED")
								else:
									boulevard_nbLT.SetAttValue("SigState","RED")
								
								#Phase 6 Config Update
								if int(binary_string_boulevard[18])==1:
									boulevard_wbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_boulevard[10])==1:
									boulevard_wbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_boulevard[2])==1:
									boulevard_wbLT.SetAttValue("SigState","RED")
								else:
									boulevard_wbLT.SetAttValue("SigState","RED")

								#Phase 8 Config Update
								if int(binary_string_boulevard[16])==1:
									boulevard_sbLT.SetAttValue("SigState","GREEN")
								elif int(binary_string_boulevard[8])==1:
									boulevard_sbLT.SetAttValue("SigState","AMBER")
								elif int(binary_string_boulevard[0])==1:
									boulevard_sbLT.SetAttValue("SigState","RED")
								else:
									boulevard_sbLT.SetAttValue("SigState","RED")
									   

							# Print Signal States
							WBLT_number =6
							EBLT_number =2
							NBLT_number =4
							SBLT_number =8
							
								
							State_of_EBLT_boulevard = Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(EBLT_number).AttValue('SigState')
							State_of_NBLT_boulevard = Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(NBLT_number).AttValue('SigState')
							State_of_SBLT_boulevard = Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(SBLT_number).AttValue('SigState')
							State_of_WBLT_boulevard = Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(WBLT_number).AttValue('SigState')

							print (Vissim.Simulation.SimulationSecond)
							print ('Actual state of SignalHead(%d) is: %s' % (SBLT_number,State_of_SBLT_boulevard))
							print ('Actual state of SignalHead(%d) is: %s' % (EBLT_number,State_of_EBLT_boulevard))
							print ('Actual state of SignalHead(%d) is: %s' % (NBLT_number,State_of_NBLT_boulevard))
							print ('Actual state of SignalHead(%d) is: %s' % (WBLT_number,State_of_WBLT_boulevard))
		##				  
							signal_json_boulevard={'4806':'%s|%s|%s|%s'%(State_of_EBLT_boulevard, State_of_NBLT_boulevard, State_of_WBLT_boulevard, State_of_SBLT_boulevard)}
							json_list_signals.append(signal_json_boulevard)
		#
					all_veh_attributes = Vissim.Net.Vehicles.GetMultipleAttributes(('SimSec' , 'StartTm','No','CoordFront','CoordRear', 'Speed', 'Acceleration', 'VehType', 'Width','Length', 'Lane', 'Hdwy' ))
					for cnt in range(len(all_veh_attributes)):
						cnt_json={'records':'%.2f|%.2f|%s|%s|%s|%.2f|%.2f|%s|%.2f|%.2f|%s|%.2f' % (all_veh_attributes[cnt][0], all_veh_attributes[cnt][1], all_veh_attributes[cnt][2], all_veh_attributes[cnt][3], all_veh_attributes[cnt][4], all_veh_attributes[cnt][5], all_veh_attributes[cnt][6], all_veh_attributes[cnt][7], all_veh_attributes[cnt][8], all_veh_attributes[cnt][9], all_veh_attributes[cnt][10], all_veh_attributes[cnt][11])}
						json_list.append(cnt_json)

					# Signal_json sent in the order of   
					p_traj = json_list
					p_sigs = json_list_signals
				
					#if(i%10==0):
					#requests.post('http://localhost:8000/records', json=json_list)
						#mydata={'SimSec': '%.2f | %.2f | %s | %s | %s | %.2f | %.2f | %s  |  %.2f  | %.2f  | %s |  %.2f\n' % (all_veh_attributes[cnt][0], all_veh_attributes[cnt][1], all_veh_attributes[cnt][2], all_veh_attributes[cnt][3], all_veh_attributes[cnt][4], all_veh_attributes[cnt][5], all_veh_attributes[cnt][6], all_veh_attributes[cnt][7], all_veh_attributes[cnt][8], all_veh_attributes[cnt][9], all_veh_attributes[cnt][10], all_veh_attributes[cnt][11])})
					try:
						#requests.post('http://'+ip_address_post+':8000/records', json=json_list, timeout=0.1)
						requests.post('http://'+ip_address_post+':8000/records', json=p_traj, timeout=0.1)
						del p_traj
						gc.collect()
						del json_list
						gc.collect()
					 
					except requests.exceptions.ReadTimeout:
						pass

					try:
						#requests.post('http://'+ip_address_post+':5000/signals', json=json_list_signals, timeout=0.1)
						requests.post('http://'+ip_address_post+':5000/signals', json=p_sigs, timeout=0.1)
						#del json_list_signals
						del p_sigs
						gc.collect()
						del json_list_signals
						gc.collect
					   
					except requests.exceptions.ReadTimeout:
						pass
						
					
					
					
					json_list=[]
					json_list_signals=[]

					i = i+1
					print ('DiD This')
					print (i)
						
						
				else:
					k1=0
					for k1 in range(0,9):
						all_veh_attributes = Vissim.Net.Vehicles.GetMultipleAttributes(('SimSec' , 'StartTm','No','CoordFront','CoordRear', 'Speed', 'Acceleration', 'VehType', 'Width','Length', 'Lane', 'Hdwy' ))
						# for cnt in range(len(all_veh_attributes)):
						#	cnt_json={'d':'%.2f|%.2f|%s|%s|%s|%.2f|%.2f|%s|%.2f|%.2f|%s|%.2f' % (all_veh_attributes[cnt][0], all_veh_attributes[cnt][1], all_veh_attributes[cnt][2], all_veh_attributes[cnt][3], all_veh_attributes[cnt][4], all_veh_attributes[cnt][5], all_veh_attributes[cnt][6], all_veh_attributes[cnt][7], all_veh_attributes[cnt][8], all_veh_attributes[cnt][9], all_veh_attributes[cnt][10], all_veh_attributes[cnt][11])}
						#	json_list.append(cnt_json)
						print ('SIM SECOND BEFORE  '+str(Vissim.Simulation.SimulationSecond))
						Vissim.Simulation.RunSingleStep()
						all_veh_attributes = Vissim.Net.Vehicles.GetMultipleAttributes(('SimSec' , 'StartTm','No','CoordFront','CoordRear', 'Speed', 'Acceleration', 'VehType', 'Width','Length', 'Lane', 'Hdwy' ))
						for cnt in range(len(all_veh_attributes)):
							cnt_json={'records':'%.2f|%.2f|%s|%s|%s|%.2f|%.2f|%s|%.2f|%.2f|%s|%.2f' % (all_veh_attributes[cnt][0], all_veh_attributes[cnt][1], all_veh_attributes[cnt][2], all_veh_attributes[cnt][3], all_veh_attributes[cnt][4], all_veh_attributes[cnt][5], all_veh_attributes[cnt][6], all_veh_attributes[cnt][7], all_veh_attributes[cnt][8], all_veh_attributes[cnt][9], all_veh_attributes[cnt][10], all_veh_attributes[cnt][11])}
							json_list.append(cnt_json)
						
						i = i+1				
						print ('SIM SECOND AFTER  '+str(Vissim.Simulation.SimulationSecond))
						
						print (str(i)+'  RUN STEP')
					   
						print (i)
					print ("this HERE "+str(i))

			print (i)
			Vissim.Simulation.Stop()
			#Vissim = None
			time.sleep(10)
			stop_time = time.time()
			sim_start_flag = 1