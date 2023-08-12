# speedtest-log
This is a script that...
  - Runs speedtest using python
  - Can be scheduled to run at regular intervals (IE: cronjob)
  - For use on a Linux system
  - Output to a log file and/or to google sheets using IFTTT.

## Setup
### Verify software is installed
Python needs to be installed
These python packages need to be installed:  speedtest-cli, numpy, and requests

Install these with

```bash
pip install speedtest-cli numpy requests
```
### Verify that IFTTT applet setup properly
- IF THIS as WEBHOOKS
- THEN THAT as Google Sheets (add row to spreadsheet)
- Note your KEY and EVENT TITLE

## Finish Setup
- Copy the python script to your system and update the variables as needed
  -  [st-simple.py](st-simple.py) uploads just download rate, ping rate, and ping.
  -  [st-all.py](st-all.py) uploads all the data that would need to be parsed in google-sheets in CSV format.
- IFTTT_Event_Name and IFTTT_Key need to be updated appropriatly
- Both IFTTT and Local Log can be disabled just update these variables and set appropriately to either true or false.
  - Use_IFTTT = True
  - Use_Local_Log = True
- Log_Path folder needs to be updated and verify that the folder exists
- Log_File will be created in Log_Path if it is not present, as long as permissions are properly set

## NOTES
- If the script is going to be run as root, the python packages need to be installed under the root user
- This information was thrown together for my enjoyment for personal use.
- This has been tested on a Linux system already.
- I am not claiming to know anything about anything.  Use at your own risk.

- Here are some of the places I got the information for this.
    - [https://github.com/sivel/speedtest-cli/wiki](https://github.com/sivel/speedtest-cli/wiki)
    - [https://pypi.org/project/speedtest-cli/](https://pypi.org/project/speedtest-cli/)


# If anyone wants to contribute please reach out
