# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import geopandas


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Recall app
from app import app




# LOAD THE DIFFERENT FILES
from lib import title, sidebar, censo_maps, location_maps, stats, slider1

# LOAD DATA
DATA_DIR = "data"
df_path = os.path.join(DATA_DIR, "ubicacion_zonasvibra.csv")
df = pd.read_csv(df_path)
geo_path=os.path.join(DATA_DIR, "MGN_ANM_MANZANA_IBAGUE.geojson")
ibague_mzn = geopandas.read_file(geo_path, driver="GeoJson")
ibague_mzn['porc_con_internet']=(ibague_mzn['TP19_INTE1']/ibague_mzn['TVIVIENDA'])*100
lats=df["Latitud"] 
lons=df["Longitud"]
h_name=df['ZONAS VIBRA']
DATA_DIR = "data"
df_path = os.path.join(DATA_DIR, "ubicacion_zonasvibra.csv")
df = pd.read_csv(df_path)
df_con_path=os.path.join(DATA_DIR, "Conexiones_Zonas.csv")
df_con=pd.read_csv(df_con_path)

###########################################################
#
#           APP LAYOUT:
#
###########################################################

app.layout = html.Div(children=
    [
        title.title,
        sidebar.sidebar,
        location_maps.location
        
        
    ],
    className="ds4a-app",  
    id='app-layout',
)

###############################################
#
#           APP INTERACTIVITY:
#
###############################################


###############################################
# Change type of map in estadisticas
##############################################

@app.callback(
    Output('graph-with-slider', 'figure'),[
    Input('type-map', 'value')])
def update_figure(tipo):
    
    if tipo==0:
            

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
            fig.update_layout(mapbox_style="carto-positron")
            fig.update_layout(transition_duration=500)
            fig['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
            
    else:
            fig = px.choropleth_mapbox(ibague_mzn, geojson=ibague_mzn.geometry, 
                    locations=ibague_mzn.index, color="porc_con_internet",
                    height=460,
                   color_continuous_scale="Greens",
                    labels={'porc_con_internet':'%'},
                     mapbox_style='carto-positron'
                   )
            fig.add_scattermapbox( lat=lats, 
                                       lon=lons, 
                                       mode = 'markers', 
                                       hovertext=h_name, marker_size=12,
                                       marker_color='#167AC6', hoverlabel={ })
            fig.update_layout(mapbox_zoom = 12, 
                               height=460,
                               mapbox_center = {"lat": 4.435800, "lon": -75.199009}) 
            fig.update_layout(transition_duration=500)
            fig['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
           
   

    return fig

###############################################################
# Change pages from sidebar
#################################################################

@app.callback(Output('app-layout','children'),[
              Input('btn-nclicks-1', 'n_clicks'),
              Input('btn-nclicks-2', 'n_clicks'),
              Input('btn-nclicks-3', 'n_clicks')])
def displayClick(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-nclicks-1' in changed_id:
        page_show = html.Div(
            [
                title.title,
                sidebar.sidebar,
                location_maps.location],
            className="ds4a-app",
        )
    elif 'btn-nclicks-2' in changed_id:
        page_show = html.Div(
            [
                title.title,
                sidebar.sidebar,
                censo_maps.heat_map],
            className="ds4a-app",
        )
    elif 'btn-nclicks-3' in changed_id:
        page_show = html.Div(
            [
                title.title,
                sidebar.sidebar,
                html.H1('EN CONSTRUCCIÓN', 
                        style = {'color': '#167AC6',                                  
                                 'justify':'center'},className="ds4a-body"), 
                ],
            className="ds4a-app",
        )
    else:
        page_show = html.Div(
            [
                title.title,
                sidebar.sidebar,
                location_maps.location],
            className="ds4a-app",
        )
        
    return page_show


#############################################################
# LINE PLOT : change month
#############################################################


#############################################################
# MAP : Add interactions here
#############################################################

# MAP date interaction




# MAP click interaction


#@app.callback(
#    Output("state_dropdown", "value"),
#    [Input("US_map", "clickData")],
#    [State("state_dropdown", "value")],
#)
#def click_saver(clickData, state):
#    if clickData is None:
#        raise PreventUpdate

    # print(clickData)

#    state.append(clickData["points"][0]["location"])

#    return state


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8060", debug=True)
