import speedtest
import requests
import time
import datetime
import os
from decimal import *
from pathlib import Path
import subprocess

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

    # Setup and run speedtest and output to output1
    proc1 = subprocess.Popen(["/usr/local/bin/speedtest","--csv","--secure"],stdout=subprocess.PIPE)
    output1 = proc1.stdout.read();
    proc1.kill()

    #if Use_IFTTT variable is truej0
    if Use_IFTTT:

        # Upload to google sheets thru ifttt
        payload = {'value1': output1}
        url = f"https://maker.ifttt.com/trigger/{IFTTT_Event_Name}/with/key/{IFTTT_Key}"
        response = requests.post(url, data=payload)

    #Set to variable for now date and time
    now = datetime.datetime.now()

    # if Use_Local_Log variable is true
    if Use_Local_Log:

        path = Path(Log_Full_Filename)

        # if file does not exist
        if not path.is_file():

                # create new file as New_File
            with open(Log_Full_Filename, 'wb') as New_File:

                #Set up and write the header
                proc2 = subprocess.Popen(["/usr/local/bin/speedtest","--csv-header","--secure"],stdout=subprocess.PIPE)
                output2 = proc2.stdout.read();
                proc2.kill()
                New_File.write(output2)

        # use existing file as Existing_File
        with open(Log_Full_Filename, 'ab') as Existing_File:

            # write data to c
            Existing_File.write(output1)


if __name__ == '__main__':
    main()
