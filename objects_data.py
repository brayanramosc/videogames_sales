#Librerías
import pandas as pd
import numpy as np
import os

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

def return_data():
	df = pd.read_csv('./data/vgsales.csv',index_col = 0)
	df.head()

	len(df[pd.isna(df.Year)])
	df = df.dropna()
	df.info()

	global_sales_by_platform = df.groupby('Platform', as_index = True).agg({'Global_Sales':'sum'})
	return(df)

def return_bar_plot(df):
	trace = go.Bar(
	            x = df.index,
	            y = df.Global_Sales.values,
	            text=df.Global_Sales,
	            texttemplate='%{text:.2s}',
	            textposition='outside',
	        )
	fig = go.Figure(data = [trace])

	fig.update_layout(
		paper_bgcolor='rgba(0,0,0,0)',
    	plot_bgcolor='rgba(0,0,0,0)',
		margin = {'l':0,'b':0.1,'t':40,'r':0},
	    width = 1000,
	    title={
	        'text': "Ventas globales por plataforma",
	        'y':0.9,
	        'x':0.5,
	        'xanchor': 'center',
	        'yanchor': 'top'},
	    xaxis_title="Platform",
	    yaxis_title="Global Sales",
	)

	return(fig)

def return_scatter_plot(df):
	trace = go.Scatter(x = df.index,
	                   y = df.Global_Sales.values,
	                  mode = 'markers+lines')

	fig = go.Figure([trace])

	fig.update_layout(
		paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
	    title={
	        'text': "Ventas globales por plataforma",
	        'y':0.9,
	        'x':0.5,
	        'xanchor': 'center',
	        'yanchor': 'top'},
	    xaxis_title="Platform",
	    yaxis_title="Global Sales",
	)	
	return(fig)

def return_pie_plot(df):
	fig = px.pie(df, values=df.Global_Sales.values, names=df.index)
	fig.update_layout(
		paper_bgcolor='rgba(0,0,0,0)',
    	plot_bgcolor='rgba(0,0,0,0)',
	    title={
	        'text': "Ventas globales por género",
	        'y':0.9,
	        'x':0.5,
	        'xanchor': 'center',
	        'yanchor': 'top'},
	)
	return(fig)