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



from datetime import datetime as dt
import json
import numpy as np
import os

# Recall app
from app import app



DATA_DIR = "data"
df_path = os.path.join(DATA_DIR, "ubicacion_zonasvibra.csv")
df = pd.read_csv(df_path)
df_con_path=os.path.join(DATA_DIR, "Conexiones_Zonas.csv")
df_con=pd.read_csv(df_con_path)

fig = px.scatter_mapbox(df, lat="Latitud", lon="Longitud", hover_name="ZONAS VIBRA", hover_data={"Latitud":False, "Longitud":False, "DIRECCION":True}, zoom=11,height=245,)
fig.update_traces(marker=dict(size=10, color='#167AC6'))
fig['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
fig.update_layout(showlegend=False),
fig.update_yaxes(tickfont=dict(size=8),range=[0, 50000000]),
fig.update_layout(mapbox_style="open-street-map", )




df_con['Total']=df_con['ene-21']+df_con['feb-21']+df_con['mar-21']+df_con['abr-21']
df_con = df_con.drop(df_con.columns[[2,3,4,5,6,7,8,9,10,11,12,13,14]], axis=1)
df2=df_con.drop(df_con.columns[[0,1, 6]], axis=1)
df_mes=df2.sum(axis = 0, skipna = True).reset_index()
df_mes = df_mes.rename(columns={'index': 'Mes', 0: 'Conexiones'})

fig1 = px.line(df_mes, x="Mes", y="Conexiones", height=235)
fig1.add_scatter(x=df_mes['Mes'], y=df_mes['Conexiones'],marker_color='#08306b')
fig1['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
fig1.update_layout(transition_duration=800)

DATA_DIR = "data"
usos_path = os.path.join(DATA_DIR, "Usabilidad_Zonas.csv")
df_u = pd.read_csv(usos_path)
Pie_fig=px.pie(df_u, 
                values='PROMEDIO', 
               names='USO',
               height=245,
               hole=0.3,
               color_discrete_sequence= px.colors.sequential.Blues_r,
               )
Pie_fig.update_traces(textposition='inside', textinfo='label', insidetextorientation='radial' )
Pie_fig.update_layout(uniformtext_minsize=9, )
Pie_fig.update_layout(font=dict(
        size=10,
        color="#167AC6"
    ))
Pie_fig['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
Pie_fig.update(
           layout_showlegend=True)


location= html.Div(
    [
        html.Div(
            [
                html.H4('Localización',style = {'color': '#167AC6','justify':'center'}),
                html.Iframe(id='map',srcDoc=open('zonas_location.html', 'r').read(), width="100%", height='500'),
                dcc.Dropdown(
                    id='drop-comunas',
                    options=[
                        {'label':'Todas', 'value':'total'},
                        {'label':'Comuna 1', 'value':'c1'},
                        {'label':'Comuna 2', 'value':'c2'},
                        {'label':'Comuna 3', 'value':'c3'},
                        {'label':'Comuna 4', 'value':'c4'},
                        {'label':'Comuna 5', 'value':'c5'},
                        {'label':'Comuna 6', 'value':'c6'},
                        {'label':'Comuna 7', 'value':'c7'},
                        {'label':'Comuna 8', 'value':'c8'},
                        {'label':'Comuna 9', 'value':'c9'},
                        {'label':'Comuna 10', 'value':'c10'},
                        {'label':'Comuna 11', 'value':'c11'},
                        {'label':'Comuna 12', 'value':'c12'},
                        {'label':'Comuna 13', 'value':'c13'},
                        {'label':'Otras', 'value':'c14'},                        
                    ],
                    value='total'
                )
            ],
            style={'flex-basis':'50%'}
        ),
        html.Div([
            html.Div(
                [
                    html.H5('Conexiones',style = {'color': '#167AC6','justify':'center'}),
                    html.Div([dcc.Graph(figure=fig1,id='month_conections')], style={'height':'245px'}),
                    html.Div(dcc.Slider(
                        id='month-filter',
                        min=0,
                        max=3,
                        value=3,
                        marks={0:'Enero',
                               1:'Febrero',
                               2:'Marzo',
                               3:'Abril',},
                        step=None
                        
                    ))
                ],
                
            ),
            html.Div(
                [
                    html.H5('Usos',style = {'color': '#167AC6','justify':'center'}),
                    html.Div([dcc.Graph(figure=Pie_fig,id='graph-usabilidad')],style={'height':'245px'})
                ],
                
            )],
            
            style={'display':'flex', 'flex-direction':'column', 'flex-basis':'50%', 'margin-left':'10px'}
          )
   ], 
    className="ds4a-body3"
)

@app.callback(Output('month_conections','figure'),
              Input('month-filter', 'value'))
def update_line_fig(month):
    DATA_DIR = "data"
    df_con_path=os.path.join(DATA_DIR, "Conexiones_Zonas.csv")
    df_con=pd.read_csv(df_con_path)
    df_con['Total']=df_con['ene-21']+df_con['feb-21']+df_con['mar-21']+df_con['abr-21']
    df_con = df_con.drop(df_con.columns[[2,3,4,5,6,7,8,9,10,11,12,13,14]], axis=1)
    df2=df_con.drop(df_con.columns[[0,1, 6]], axis=1)
    df_mes=df2.sum(axis = 0, skipna = True).reset_index()
    df_mes = df_mes.rename(columns={'index': 'Mes', 0: 'Conexiones'})
    df_mes=df_mes.iloc[0: month+1]

    fig1 = px.line(df_mes, x="Mes", y="Conexiones", height=235)
    fig1.add_scatter(x=df_mes['Mes'], y=df_mes['Conexiones'],marker_color='#08306b')
    fig1['layout'].update(margin=dict(l=0,r=0,b=0,t=0))
    fig1.update_layout(showlegend=False)
    fig1.update_yaxes(tickfont=dict(size=8),range=[0, 50000000]),
    fig1.update_layout(transition_duration=800)
    
    return fig1