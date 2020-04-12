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

	global_sales_by_platform = df.groupby('Platform', as_index = True).agg({'Global_Sales':'sum'})
	return(df)

def return_bar_plot(df,variable):
	if variable == 'plataforma':
	    x_title='Platform'
	else:
	    x_title='Genre'
	
	trace = go.Bar(
	            x = df.index,
	            y = df.Global_Sales.values,
	            text=df.Global_Sales,
	            texttemplate='%{text:.2s}',
	            textposition='outside',
	        )
	fig = go.Figure(data = [trace])

	fig.update_layout(
		plot_bgcolor = '#b5fbff',
		margin = {'l':0,'b':0.1,'t':80,'r':0},
	    width = 1000,
	    title={
	        'text': "Ventas globales por "+variable,
	        'y':0.9,
	        'x':0.5,
	        'xanchor': 'center',
	        'yanchor': 'top'},
	    xaxis_title=x_title,
	    yaxis_title="Global Sales",
	)

	return(fig)

def return_scatter_plot(df):
	trace = go.Scatter(x = df.index,
	                   y = df.Global_Sales.values,
	                  mode = 'lines')

	fig = go.Figure([trace])

	fig.update_layout(
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

def return_pie_plot(df):
	
	fig = px.pie(df, values=df.Global_Sales.values, names=df.index, title='Ventas globales por género')
	
	return(fig)

def return_name_plot(df):
	x=df.Name
	fig = go.Figure()
	fig.add_trace(go.Scatter(x =x,
	                         y = df.NA_Sales.values,
	                         line=dict(color='peru', width=3),
	                         name='NA_Sales'))
	fig.add_trace(go.Scatter(x=x, y=df.EU_Sales.values,
	                         line=dict(color='indigo', width=3),
	                         name='EU_Sales'))
	fig.add_trace(go.Scatter(x=x, y=df.JP_Sales.values,
	                         line=dict(color='firebrick', width=3),
	                         name='JP_Sales'))
	fig.add_trace(go.Scatter(x=x, y=df.Other_Sales.values,
	                         line=dict(color='lime', width=3),
	                         name='Other_Sales'))
	fig.update_layout(
	    title={
	        'text': "Ventas por Top 10 videojuegos",
	        'y':0.9,
	        'x':0.5,
	        'xanchor': 'center',
	        'yanchor': 'top'},
	    xaxis_title="Videogames",
	)	
	
	return(fig)