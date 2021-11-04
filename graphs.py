# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:52:53 2021

@author: Amr Emam
"""
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
class Graphs:
    def __init__(self,df):
        self.df=df
        
        
    
    def histo(self,x):
       
        
        fig = px.histogram(self.df, x=x, color='gender',opacity=0.7)
        fig.update_layout(title_text='Distribution of '+x+' by Gender',
                      title_x=0.5, title_font=dict(size=20))
        fig.update_layout(barmode='overlay', xaxis={'categoryorder': 'total descending'})
        fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
    
        return fig
    
    
    def pieChart(self,column_name):
      value_count=self.df[column_name].value_counts(normalize=True)
      fig = px.pie(self.df, values=value_count, names=value_count.index, title='Distribution of {}'.format(column_name.title()))
      return fig
    
    
    def bar_chart_with_avg_scores(self,column_name):
      scores=['math score',	'reading score'	,'writing score']
      groupby_df=self.df.groupby(column_name)[scores].mean().T
      fig = go.Figure(data=[
        go.Bar(name=index, x=groupby_df.columns, y=row) for index, row in groupby_df.iterrows()])
      fig.update_yaxes(title_text="Average Scores", title_font={"size": 14})
      fig.update_xaxes(title_text=column_name, title_font={"size": 14})
    
      fig.update_layout(title_text='Average Exam Scores for '+column_name,
                      title_x=0.5, title_font=dict(size=20))
      return fig
    
    
    def scatter_plot(self,x_column ,y_column,color_column=None):
      fig = px.scatter(self.df, x=x_column, y=y_column, color=color_column,trendline="ols")
      fig.update_layout(title_text='Relationship between '+x_column +' and '+ y_column,
                      title_x=0.5, title_font=dict(size=20))
      fig.data[1].line.color = 'red'
      return fig