#!/usr/bin/env python3

import requests
import json
import pandas as pd
import plotly.express as px

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.7',
    'Connection': 'keep-alive',
    'Referer': 'https://hydro.imgw.pl/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'id': '251230120',
}

response = requests.get('https://hydro.imgw.pl/api/station/meteo/', params=params, headers=headers)

j = json.loads(response.text)

name = j['name']
df = pd.DataFrame.from_dict(j['airTemperatureRecords'])
df['value'] = pd.to_numeric(df["value"])
df['date'] = pd.to_datetime(df["date"])

fig = px.line(df, x='date', y='value', title='Interactive Line Chart')
fig.write_html('/var/www/html/line_plot.html', auto_open=True)