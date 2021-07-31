# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import json
from datetime import datetime as dt


# Recall app
from app import app


####################################################################################
# Add the Alcaldía logo
####################################################################################

alcaldia_Img = html.Div(
    children=[html.Img(src=app.get_asset_url("logo_administracion.png"), id="alcaldia-image", width="200", height="auto")],
)


####################################################################################
# Add gauge with total zonas
####################################################################################

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 150,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Zonas instaladas", },
    gauge = {'axis': {'range': [None, 200]}, 'bar': {'color': "#008e1f"},}

))

fig['layout'].update(margin=dict(l=0,r=0,b=0,t=0), font=dict(color="#167AC6"), paper_bgcolor='rgba(0, 0, 0, 0)')

sidebar = html.Div(
    [
    alcaldia_Img,
    html.Br(),
    html.Br(),
    html.Button('Estadísticas', 
               id='btn-nclicks-1', 
               n_clicks=0,
                           
               
              ),
    html.Br(),
    html.Br(),
    html.Button('Demografía', id='btn-nclicks-2', n_clicks=0),
    html.Br(),
    html.Br(),
    html.Button('Modelo', id='btn-nclicks-3', n_clicks=0),
    html.Br(),
    html.Div(dcc.Graph(figure=fig, id='gauge-total'))
    
],
    className="ds4a-sidebar",
)
