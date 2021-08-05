import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State 
import plotly.graph_objs as go 
import plotly.express as px 
import numpy as np
import pandas as pd 


#add external stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#initialize Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

#data
df = pd.read_csv('zomato.csv', encoding="ISO-8859-1")

#country iso with counts
col_label = "country_code"
col_values = "count"

v = df[col_label].value_counts()
new = pd.DataFrame({
    col_label: v.index, 
    col_values: v.values
})

hexcode = 0
borders = [hexcode for x in range(len(new))],
map = dcc.Graph(
    id = '8',
    figure = {
        'data': [{
            'locations': new['country_code'],
            'z': new['count'], 
            'colorscale': 'Earth',
            'reversescale': True, 
            'hover-name': new['final_country'],
            'type': 'choropleth'
        }], 
        'layout': {'title': dict(
            text = 'Restaurant Frequency by Location',
            font = dict(size =20, color='white')
        ),
        'paper_bgcolor': '#111111',
        'plot_bgcolor': '#111111',
        'height': 800,
        'geo': dict(bgcolor= 'rgba(0,0,0,0)')}
    }
)


df2 = pd.DataFrame(
    df.groupby(by='Restaurant Name')['Votes'].mean()
)
df2 =df2.reset_index() 
df2 = sort_values(['Votes'], ascending=False)

df3 = df2.head(10)
bar1 = dcc.Graph(id = 'bar1',
            figure = {
                'data': [go.Bar(x=df3['Restaurant Name'],
                y = df3['Votes'])],
                'layout': {
                    'title': dict(
                        text = 'Top Restaurant in India',
                        font = dict(size=20, color = 'white')
                    ),
                    'paper_bgcolor': '#111111',
                    'plot_bgcolor': '#111111',
                    'height': 600,
                    'line': dict(
                        color = 'white',
                        width = 4,
                        dash = 'dash',
                    ),
                    'xaxis': dict(tickfont = dict(
                        color = 'white'
                    ), showgrid=False,
                    title = 'Number of Votes', color = 'white')
                }
            })