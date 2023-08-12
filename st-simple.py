import speedtest
import requests
import time
import datetime
import os
import csv
from decimal import *
from pathlib import Path
import numpy as np

# establish if how the script will be used
Use_IFTTT = True
Use_Local_Log = True

# establish Log variables
Log_Path = "/var/log/internetspeedcheck/"                       # path to the log file
Log_File = time.strftime("log%Y.csv")                           # log file and log file name pattern.  logYYYY.csv
Log_Full_Filename = Log_Path + Log_File                         # log file name and path

# establish ifttt variables
IFTTT_Event_Name = "IFTTT-EVENT-NAME"
IFTTT_Key = "ZZZZZZZZZZZZZZZZZZZZZZ"

def main():

    # Perform the speedtest and set the variables
    st = speedtest.Speedtest()
    servername = st.get_best_server()
    Download_Speed = st.download() / 1024 / 1024                # Convert to Mbps
    Upload_Speed = st.upload() / 1024 / 1024                    # Convert to Mbps
    Ping = st.results.ping

    #if Use_IFTTT variable is true
    if Use_IFTTT:

        # Upload to google sheets thru ifttt
        payload = {'value1': Download_Speed, 'value2': Upload_Speed, 'value3': Ping}
        url = f"https://maker.ifttt.com/trigger/{IFTTT_Event_Name}/with/key/{IFTTT_Key}"
        response = requests.post(url, data=payload)
        #print(servername)

    now = datetime.datetime.now()

    # Set fields
    fields=[now,Download_Speed,Upload_Speed,Ping]

    # if Use_Local_Log variable is true
    if Use_Local_Log:

        path = Path(Log_Full_Filename)

            # if file does not exist
        if not path.is_file():

                # create new file as f
            with open(Log_Full_Filename, 'x', newline='') as csvfile:

                #Set up and write the header
                fieldnames = ['Date_Time', 'Download_Speed', 'Upload_Speed', 'Ping']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()

        # use existing file as c
        with open(Log_Full_Filename, 'a') as c:

            # write fields to c
            writer = csv.writer(c, delimiter='\t',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fields)


if __name__ == '__main__':
    main()
