# -*- coding: utf-8 -*-

import os
import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Golden Stock Dashboard'),
    dcc.Interval(id='interval-component', interval=5*60*1000, n_intervals=0),
    html.Div(id='latest-data'),
    dcc.Graph(id='historical-plot'),
])

@app.callback(Output('latest-data', 'children'), Input('interval-component', 'n_intervals'))
def update_latest_data(_):
    data = pd.read_csv('/home/ec2-user/dashboard_project/gold.csv')
    latest = data.tail(1)
    latest_timestamp = latest['timestamp'].values[0]
    latest_price = latest['price'].values[0]
    highest_price = data['price'].max()
    volatility = data['price'].std()
    daily_yield = (data['price'].tail(1).values[0] - data['price'].head(1).values[0]) / data['price'].head(1).values[0]

    return [html.P(f'Latest Timestamp :{latest_timestamp}'),
        html.P(f'Latest Price: {latest_price}'),
        html.P(f'Highest Price: {highest_price}'),
        html.P(f'Volatility: {volatility}'),
        html.P(f'Daily Yield: {daily_yield * 100:.2f}%'),
    ]

@app.callback(Output('historical-plot', 'figure'), Input('interval-component', 'n_intervals'))
def update_historical_plot(_):
    data = pd.read_csv('/home/ec2-user/dashboard_project/gold.csv')
    return go.Figure(
        data=[go.Scatter(x=data['timestamp'], y=data['price'], mode='lines+markers')],
        layout=go.Layout(title='Historical Price Plot', xaxis=dict(title='Timestamp'), yaxis=dict(title='Price'))
    )

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
