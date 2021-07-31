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


title = html.Div(
    className="ds4a-body",
    children=[
        dbc.Row(dbc.Col(html.H1("Zonas Vibra Ibagué"), width={"size": 6, "offset": 3}, style={"background-color": "#167AC6", "color":"#fff", "display": "flex", "justify-content":"center"}))
    ],
    id="title",
)
