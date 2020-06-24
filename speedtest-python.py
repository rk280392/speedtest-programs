#!/usr/bin/python3

import subprocess
import json
import mysql.connector
import datetime


currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

speedt = subprocess.Popen(['./speedtest.py', '--json'] ,stdout=subprocess.PIPE, universal_newlines=True)
output  = speedt.communicate()[0]
exitcode = speedt.returncode

if (exitcode == 0):
    myArray = json.loads(output)
    
    speedtestDownloadSpeed = myArray['download'];
    speedtestUploadSpeed = myArray['upload'];
    myPublicIP = myArray['client']['ip'];
    peerServer = myArray['server']['sponsor'] + " " +  (myArray['server']['name']) + " " + (myArray['server']['country'])
    
    try:
        mydb = mysql.connector.connect(option_files='pass.conf')
        mycursor = mydb.cursor()
        sql = "INSERT INTO speedtest (TimeStamp, PublicIp, Peers, UploadSpeed, DownloadSpeed) Values(%s,%s,%s,%s,%s)"
        vals = (currentTime,myPublicIP,peerServer,speedtestUploadSpeed,speedtestDownloadSpeed)
        mycursor.execute(sql,vals)
        mydb.commit()
        mydb.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    
    print(mycursor.rowcount, "record inserted.")
else:
    print("Speedtest couldn't be performed, please check internet connectivity")
