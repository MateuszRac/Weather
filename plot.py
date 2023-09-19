#!/usr/bin/env python3

import pandas as pd
import plotly.express as px

# Sample DataFrame
data = {
    'Year': [2010, 2011, 2012, 2013, 2014],
    'Value': [15, 18, 24, 21, 28]
}

df = pd.DataFrame(data)

# Create an interactive line chart using Plotly Express
fig = px.line(df, x='Year', y='Value', title='Interactive Line Chart')

# Export the plot as an HTML file
fig.write_html('/var/www/html/line_plot.html', auto_open=True)