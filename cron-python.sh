#!/bin/bash

echo $(date) >> bash_cron_log.txt
/usr/bin/python3 /vagrant/speedtest-practice/speedtest-python.py >> bash_cron_log.txt  
