import pandas as pd
import requests
from datetime import datetime
import time

latitude = []
longitude = []
timestamp = []
message = []
_time_ = []

for i in range(1, 21):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    response.raise_for_status()
    latitude.append(data['iss_position']['latitude'])
    longitude.append(data['iss_position']['longitude'])
    timestamp.append(data['timestamp'])
    message.append(data['message'])
    _time_.append(current_time)
    time.sleep(1)

df = pd.DataFrame({"Time": _time_, "Latitude": latitude, "Longitude": longitude, "Timestamp": timestamp, "Response": message})
df.to_csv("Space_Station_Location.csv", index=False)
print("CSV dataset created")

database = pd.read_csv("Space_Station_Location.csv")
print(database)
