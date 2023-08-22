import gspread
import datetime
import time
import speedtest
from pathlib import Path

# Get timestamp and insert data into the sheet
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# connect to google account
gc = gspread.service_account()

# open spreadsheet
sh = gc.open("SpeedTest").sheet1

# run speedtest
st = speedtest.Speedtest(secure=True)
best_server = st.get_best_server()

# convert to Mbps
download_speed = st.download() / 1_000_000

# convert to Mbps
upload_speed = st.upload() / 1_000_000
ping = st.results.ping

data = {
    "timestamp": timestamp,
    "download_speed": download_speed,
    "upload_speed": upload_speed,
    "ping": ping,
    "name": best_server["sponsor"],
    "city": best_server["name"],
    "id": best_server["id"],
    "lat": best_server["lat"],
    "lon": best_server["lon"],
    "host": best_server["host"][:-5],           # set and remove last 5 characters from string
    "km": best_server["d"],
    "mi": float(best_server["d"] * 0.6213712)   # convert from km to mi
}

data_to_insert = []

for key,value in data.items():
    data_to_insert.append(value)

# insert data_to_insert at row 6
sh.insert_row(data_to_insert,6,value_input_option='USER_ENTERED')

# close the gspread session
gc.session.close()
