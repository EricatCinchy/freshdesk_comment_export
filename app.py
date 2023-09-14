import time
import requests
import os
import re
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def connect_to_api():
    # Make a request to the Freshdesk API
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Task start @', current_time, flush=True)
    FD_URL = os.getenv('FD_URL') + "/api/v2/tickets/" + str(i) + "/conversations"
    FD_USR = os.getenv('FD_USERNAME')
    FD_PWD = os.getenv('FD_PWD')

    response = requests.get(FD_URL, auth=(FD_USR, FD_PWD))
    # Process the response data
    if response.status_code == 200:
        data = response.json()
        # Do something with the data
        print(data)
    else:
        print("Error:", response.status_code)

# Number of times to connect to the API
num_connections = 5

# Connect to the API multiple times in a loop
for i in range(num_connections):
    print("Connection", i+1)
    connect_to_api()
    

def list_all_tickets():
    print(str(i))
    # Make a request to the Freshdesk API
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Task start @', current_time, flush=True)
    FD_URL = os.getenv('FD_URL') + "/api/v2/tickets?page=1"
    FD_USR = os.getenv('FD_USERNAME')
    FD_PWD = os.getenv('FD_PWD')

    response = requests.get(FD_URL, auth=(FD_USR, FD_PWD))
    # Process the response data
    if response.status_code == 200:
        data = response.json()
        # Do something with the data
        print(data)
    else:
        print("Error:", response.status_code)