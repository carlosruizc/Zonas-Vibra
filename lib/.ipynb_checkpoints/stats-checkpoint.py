import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import os

# Recall app
from app import app


##############################################################
# PIE PLOT
###############################################################
DATA_DIR = "data"
usos_path = os.path.join(DATA_DIR, "Usabilidad_Zonas.csv")
df = pd.read_csv(usos_path)
Pie_fig = px.pie(df, values='PROMEDIO', names='USO', title='Uso de las Zonas Vibra')

###############################################################
# LINE PLOT
###############################################################

DATA_DIR = "data"
conections_path = os.path.join(DATA_DIR, "Conexiones_Zonas2021.csv")
df = pd.read_csv(conections_path)



#############################################################
#LINE PLOT : Add sidebar interaction here
#############################################################
Line_fig = px.line(df, x="MES", y="CONEXIONES")
Line_fig.update_layout(
        title="Conexiones por mes", paper_bgcolor="#F8F9F9"
    )

#################################################################################
# Here the layout for the plots to use.
#################################################################################
stats = html.Div(
    [
       
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=Line_fig, id="Line")),
                dbc.Col(dcc.Graph(figure=Pie_fig, id="Scatter")),
            ]
        ),
        
    ],
    className="ds4a-body",
)
