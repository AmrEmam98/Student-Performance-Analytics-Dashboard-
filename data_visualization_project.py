# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import graphs
from graphs import Graphs
from text_style_constants  import *
df=pd.read_csv("StudentsPerformance.csv")
graphs= Graphs(df)

sidebar = html.Div(
    [
        html.H2('Parameters', style=TEXT_STYLE),
        html.Hr()
       #controls
    ],
    style=SIDEBAR_STYLE,
)
###############################
content_first_row = dbc.Row([
    
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Histogram Parameter', className='card-title', style=CARD_TEXT_STYLE),
                       
                         dcc.Dropdown(
                             id='hist_x',
                             options=[{'label':str(i),'value':str(i)} for i in df.columns[-3:]], value="math score")
                    ]
                ),
            ]

        ),
        md=6
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Bar Chart Parameter', className='card-title', style=CARD_TEXT_STYLE),
                        dcc.Dropdown(
                             id='bar_x',
                             options=[{'label':str(i),'value':str(i)} for i in df.columns[:-3]],value='test preparation course')
                    ]
                ),
            ]

        ),
        md=6
    ),
   
])


content_second_row = dbc.Row(
    [
       
        dbc.Col(
            dcc.Graph(id='hist',figure=graphs.histo("reading score")), md=6
        ),
        dbc.Col(
            dcc.Graph(id='bar-chart',figure=graphs.bar_chart_with_avg_scores('race/ethnicity')), md=6
        )
    ]
)



content_third_row = dbc.Row(
    [    
     
     
     
     dbc.Col([
              
         
          dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Pie Chart Parameter'], className='card-title',
                                style=CARD_TEXT_STYLE),
                         dcc.Dropdown(
                             id='pie',
                             options=[{'label':str(i),'value':str(i)} for i in df.columns[:-3]], value= 'gender')
                       
                        
                       
                    ]
                )
            ]
        ),
         
         
         
         
            dcc.Graph(id='pie-chart',figure=graphs.pieChart('parental level of education'))
       
         
         
         
         
         
         ],md=4),
     dbc.Col([
         
       dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Scatter plot Parameters', className='card-title', style=CARD_TEXT_STYLE),
                       
                    dbc.Row([
                        
                       dbc.Col(dcc.Dropdown(
                             id='scatter-x-axis',
                             options=[{'label':str(i),'value':str(i)} for i in df.columns[-3:]]),md=6),
                       dbc.Col(
                            
                           
                           dcc.Dropdown(
                             id='scatter-y-axis',
                             options=[{'label':str(i),'value':str(i)} for i in df.columns[-3:]]),md=6
                           
                           )]
                       )
                    ]
                ),
            ]
        ),
        md=12
    ),
        dbc.Col(
            
            dcc.Graph(id='scatter', figure=graphs.scatter_plot(x_column='reading score',y_column='writing score')), md=12,
            
      
  
       )],md=8),
             
        
        
        
    ]
)
















###############################
content = html.Div(
    [
        html.H2('Students Performance Analytics Dashboard ', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        
    ],
    style=CONTENT_STYLE
)


   

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([content])






@app.callback(
     
    
  
    Output('scatter', 'figure'),
    
    Input('scatter-x-axis', 'value'),
    Input('scatter-y-axis', 'value')
    
    #State('my-slider', 'value'),State('demo-dropdown', 'value'),
    
    )
def update_scatter(scattx,scatty):
    
    fig=graphs.scatter_plot(x_column=scattx, y_column=scatty)
    

    return fig

@app.callback(
    Output('bar-chart', 'figure'),Input('bar_x', 'value'))
def update_bar(bar):
   
    fig=graphs.bar_chart_with_avg_scores(bar)
    return fig
@app.callback(
      Output('pie-chart', 'figure'),Input('pie', 'value'))
def update_pie(pie):
    
    fig=graphs.pieChart(pie)
    return fig

@app.callback(
    Output('hist', 'figure'), Input('hist_x', 'value'))
def update_hist(hist):
    fig=graphs.histo(hist)
    return fig


app.run_server()