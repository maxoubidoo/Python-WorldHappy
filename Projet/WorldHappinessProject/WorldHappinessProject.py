# filename = 'dash-01.py'

#
# Imports
#


import sys
print(sys.version)
import plotly_express as px

import dash

from dash import dcc
from dash import html

import pandas as pd

#
# Data
#

wh2015 = pd.read_csv ("./2015.csv")
wh2016 = pd.read_csv ("./2016.csv")
wh2017 = pd.read_csv ("./2017.csv")
wh2018 = pd.read_csv ("./2018.csv")
wh2019 = pd.read_csv ("./2019.csv")
wh2020 = pd.read_csv ("./2020.csv")

data = wh2015



#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)

    

    fig = px.scatter(data, x="Happiness Score", y="Freedom",
                        color="Region",
                        size="Economy (GDP per Capita)",
                        hover_name="Country") # (4)

    fig2 =  px.histogram(data, x="Happiness Score", 
                        color="Region",
                        nbins = 40)
            
    fig2.update_layout(barmode='stack')
    fig2.update_traces(opacity=1)

    fig3 = px.scatter_geo(data, locations="Country", color="Region",locationmode="country names",
                     hover_name="Country", size="Happiness Score",
                     projection="natural earth")


    app.layout = html.Div(
    children=[

        html.H1(children="Happiness Analytics", style={'textAlign': 'center', 'color': '#7FDBFF'}),
        
        html.P(
            children="Analyze the behavior of world happiness"
            " using linked statistics"
            " between 2015 and 2020",
        ),

    html.Label('Year'),
    dcc.Slider(
        id = 'year_slider',
        min=2015,
        max=2020,
        value=1,
        marks={
        2015: '2015',
        2016: '2016',
        2017: '2017',
        2018: '2018',
        2019: '2019',
        2020: '2020'
    },
    ),



    html.Div(id='slider_year_output'),

    html.Label('Y'),
    dcc.Dropdown(
        id = "Drop_Y",
        options=[
            {'label': 'GDP per Capita', 'value': 'Economy (GDP per Capita)'},
            {'label': 'Family', 'value': 'Family'},
            {'label': 'Life expectancy', 'value': 'Health (Life Expectancy)'},
            {'label': 'Freedom', 'value': 'Freedom'},
            {'label': 'Government trust', 'value': 'Trust (Government Corruption)'},
            {'label': 'Generosity', 'value': 'Generosity'},
            {'label': 'Distopia', 'value': 'Dystopia Residual'}
        ],
        value='Economy (GDP per Capita)'
    ),

    html.Div(id='Drop_Y_output'),

        dcc.Graph(
            id='graph1',
            figure = fig
        ),
        dcc.Graph(
            id='graph2',
            figure = fig2
        ),
        dcc.Graph(
            id='graph3',
            figure = fig3
        ),
        html.Div(children=f'''
                                The graph above shows relationship between life expectancy and
                                GDP per capita for year . Each continent data has its own
                                colour and symbol size is proportionnal to country population.
                                Mouse over for details.

                            '''),    
    ])

    



    #@app.callback(
    #Output(component_id='Drop_Y_output',component_property='children'),
    #Output('dd-output-container', 'children'),
    #Input(component_id='dist-drop', component_property='value'),
    #Input('Drop_Y', 'value')
     # )





    #
    # RUN APP
    #

    app.run_server(debug=True) # (8)
