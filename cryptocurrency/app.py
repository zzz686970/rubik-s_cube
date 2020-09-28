import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
from datetime import timedelta
from flask import Flask

pd.options.plotting.backend = "plotly"


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = Flask(__name__)
app = dash.Dash(server = server, external_stylesheets=external_stylesheets)
df = pd.read_csv('raw_data.csv')

df['timestamp'] = pd.to_datetime(df['timestamp'])
# group by week_date for all dates
df['week_date'] = df.apply(lambda row: row['timestamp'] - timedelta(days=row['timestamp'].weekday()), axis=1)
## compute 7 day rolling window for closed price
df['7day'] = df[['timestamp', 'close (USD)']].rolling(window=7).mean()

## compute 3 day rolling window for closed price
df['3day'] = df[['timestamp', 'close (USD)']].rolling(window=3).mean()
# fig = px.line(df, x='timestamp',y=['close (USD)', '7day', '3day'], title='BTC Market Time Series Graph')

#
fig = go.Figure()
# Create figure
for col in ['close (USD)','7day','3day']:
    fig.add_trace(go.Scatter(x=df.index, y=df[col].values,
                             name = col,
                             mode = 'lines')
                 )

# one button for each df column
updatemenu= []
buttons=[]
for col in ['close (USD)','7day','3day']:
    buttons.append(dict(method='restyle',
                        label=col,
                        args=[{'y':[df[col].values]}])
                  )

# some adjustments to the updatemenu
updatemenu=[]
your_menu=dict()
updatemenu.append(your_menu)
updatemenu[0]['buttons']=buttons
updatemenu[0]['direction']='down'
updatemenu[0]['showactive']=True

# update layout and show figure
fig.update_layout(
    updatemenus=updatemenu,
    title_text="BTC USD Market Time Series Graph",
    showlegend=True,
    title_x=0.5
    # height=600,
    # width=800,
)

app.layout = html.Div([
    dcc.Graph(
        id='btc-usd-market',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port = 8050)