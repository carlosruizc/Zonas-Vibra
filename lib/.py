import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import geojson
import pandas as pd
import geopandas
import folium
import matplotlib
import collections


from datetime import datetime as dt
import json
import numpy as np
import os

# Recall app
from app import app

DATA_DIR = "assets"




##############################
# Map Layout
##############################
locationmap = html.Div(
    [
        html.H1('Ubicación de Zonas Vibra'),
        html.Iframe(id='map', srcDoc=open('zonas_location.html', 'r').read(), width="100%", height='600')
        
    ],
    className="ds4a-body",
)
