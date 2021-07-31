import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import geojson
import pandas as pd
import folium
import matplotlib
import geopandas



from datetime import datetime as dt
import json
import numpy as np
import os

# Recall app
from app import app

DATA_DIR = "data"
df_path = os.path.join(DATA_DIR, "ubicacion_zonasvibra.csv")
df = pd.read_csv(df_path)
geo_path=os.path.join(DATA_DIR, "MGN_ANM_MANZANA_IBAGUE.geojson")
ibague_mzn = geopandas.read_file(geo_path, driver="GeoJson")
ibague_mzn['porc_con_internet']=(ibague_mzn['TP19_INTE1']/ibague_mzn['TVIVIENDA'])*100
var_path=os.path.join(DATA_DIR, "Variables_Censo.csv")
df_var=pd.read_csv(var_path)


##############################
# Map Layout
##############################

lats=df["Latitud"] 
lons=df["Longitud"]
h_name=df['ZONAS VIBRA']

fig = px.density_mapbox(ibague_mzn, lat="LATITUD", lon="LONGITUD", 
                                     z='porc_con_internet', radius=10, zoom=11, height=460,
                                     color_continuous_scale='RdYlGn',
                                     hover_data={"LATITUD":False,
                                                 "LONGITUD":False,
                                                 "porc_con_internet":True},
                                     labels={'porc_con_internet':'%'},
                                     
                       )


fig.add_scattermapbox( lat=lats, 
                                       lon=lons, mode = 'markers', 
                                       hovertext=h_name, marker_size=12,marker_color='#167AC6', )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(transition_duration=500)
fig['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
heat_map=html.Div(


   [     html.H4('Porcentaje de viviendas con internet', 
                        style = {'color': '#167AC6',                                  
                                 'justify':'center'}),   
        html.Div(dcc.Graph(figure=fig, 
                  id='graph-with-slider'),),
        
        html.Div( [
                    html.H4('Seleccione el tipo de gráfico', 
                        className = 'fix_label', 
                        style = {'color': '#167AC6', 
                                 
                                 'justify':'center'}),
                    html.Div(
                    dcc.Slider(
                            id='type-map',
                            min=0,
                            max=1,
                            step=None,
                            value=0,
                            marks={
                                0: 'Mapa de calor',
                                1: 'Mapa por manzanas',}
                             ),style={'margin-top': '20px'}
                    
                    )
                    
                ], 
                 style={'float':'left','width': '40%', 'padding': '0px 20px 20px 20px', 'margin-top': '20px'}
                            ),
        
                html.Div([html.H4('Seleccione la variable del CNPV 2018', 
                        className = 'fix_label', 
                        style = {'color': '#167AC6', 
                                  
                                 'justify':'center'}),
                dcc.Dropdown(
                    id='type-variable',
                    options=[{'label': i, 'value':i} for i in df_var[df_var['INCLUIR']=='SI']['DESCRIPCIÓN']],
                    value='Porcentaje de unidades con uso vivienda'
                ),
                ], style={'width': '49%', 'float': 'right', 'padding': '0px 20px 20px 20px', 'margin-top': '20px'
                          })        
                   ],
                              

    className="ds4a-body"

)