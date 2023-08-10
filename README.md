# speedtest-log
This is a script that runs speedtest using python at regular intervals on a linux system and output to a log file and/or to google sheets using IFTTT.

This information was thrown together for my enjoyment for personal use. 
This has been tested on a Linux system already.  Use at your own risk.

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
- IFTTT_Event_Name and IFTTT_Key need to be updated appropriatly
- Both IFTTT and Local Log can be disabled just update these variables and set appropriately to either true or false.
  - Use_IFTTT = True
  - Use_Local_Log = True
- Log_Path folder needs to be updated and verify that the folder exists

## NOTES
- If the script is going to be run as root, the python packages need to be installed under the root user
- Log_File will be created if it is not present, as long as permissions are properly set
- This works best when run as a cronjob.


# If anyone wants to contribute please reach out
