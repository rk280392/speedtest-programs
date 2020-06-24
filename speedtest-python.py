#!/usr/bin/python3

import subprocess
import json
import mysql.connector
import datetime

mydb = mysql.connector.connect(option_files='pass.conf')

mycursor = mydb.cursor()
currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

speedt = subprocess.Popen(['./speedtest.py', '--json'] ,stdout=subprocess.PIPE, universal_newlines=True)
output = speedt.communicate()[0]

myArray = json.loads(output)

speedtestDownloadSpeed = myArray['download'];
speedtestUploadSpeed = myArray['upload'];
myPublicIP = myArray['client']['ip'];
peerServer = myArray['server']['sponsor'] + " " +  (myArray['server']['name']) + " " + (myArray['server']['country'])


sql = "INSERT INTO speedtest (TimeStamp, PublicIp, Peers, UploadSpeed, DownloadSpeed) Values(%s,%s,%s,%s,%s)"
vals = (currentTime,myPublicIP,peerServer,speedtestUploadSpeed,speedtestDownloadSpeed)

mycursor.execute(sql,vals)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
