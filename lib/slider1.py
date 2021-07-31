# Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from app import app


slider1 = html.Div(
    (dcc.Slider(
                    min=0,
                    max=2,
                    step=None,
                    marks={
                        0: 'Municipio',
                        1: 'Comuna',
                        2: 'Zona Vibra',
                        
                    },
                    value=0
            )  
        ),   
    className="ds4a-body",
    
)
