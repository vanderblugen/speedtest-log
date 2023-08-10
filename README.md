# speedtest-log
Run speedtest using python at regular intervals on a linux system and output to a log file and/or to google sheets.

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
