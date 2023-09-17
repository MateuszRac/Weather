#!/usr/bin/env python3

import requests
import json

# URL of the API
url = "https://danepubliczne.imgw.pl/api/data/synop/"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the JSON data
        print(json.dumps(data, indent=4))
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")