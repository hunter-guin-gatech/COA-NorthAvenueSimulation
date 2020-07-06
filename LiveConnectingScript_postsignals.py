from LiveVolumeQuery import *
from LiveSignalQuery import *
from TurnQuery import *
from flask import Flask, flash, render_template
import requests
import urllib
import sys
import time
import json
from flask import request
import glob
from datetime import date

app = Flask(__name__)
app.secret_key = "super secret key"

# @app.route('/LiveSignal/startepoch=<epoch>&simtime=<simtime>')
# def livesig(epoch, simtime):
# 	return str(LiveSignal(float(epoch), float(simtime)))	

# @app.route('/LiveVolume/startepoch=<epoch>&intersection=<intrsc>&approach=<approach>&simtime=<stime>')
# def livevol(epoch, intrsc, approach, stime):
#     return LiveVolume(float(epoch), int(intrsc), approach, float(stime))	

# @app.route('/Turn/startepoch=<epoch>&simtime=<simtime>&intersection=<intrsc>&approach=<approach>')
# def turn(epoch, simtime, intrsc, approach):
# 	return str(getTurn(float(epoch), float(simtime), int(intrsc), approach))	

@app.route('/signals', methods=['POST'])
def result():
    t = time.strftime("%H_%M_%S", time.localtime(time.time()))
    d = date.today().strftime("%d_%m_%Y")
    tifCounter = len(glob.glob1("//ad.gatech.edu/gtfs/COE/CEE/Transpo/smartdata/RealTimeRunTrajectoryFiles_5Sep2019/signalfiles","*.json"))
    filename = "//ad.gatech.edu/gtfs/COE/CEE/Transpo/smartdata/RealTimeRunTrajectoryFiles_5Sep2019/signalfiles/signalfile_"+d+"_"+t+"_"+str(tifCounter)+".json"

    with open(filename, 'w') as outfile:
    	json.dump(request.json, outfile)
    	#json.dumps(str(request.json).replace('"', ''))
    return str(request.json).replace('"', '')
    #del request.json
    


if __name__ =="__main__":
	app.run(debug=True, host= '0.0.0.0')
