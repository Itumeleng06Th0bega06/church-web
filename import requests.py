﻿import requests
import time
while True:
         response = requests.get("https://shekinahblazeoi.streamlit.app/")
         print(f"Pinged app at {time.ctime()}, Status Code: {response.status_code}")
         time.sleep(600)  # Ping every 10 minutes
