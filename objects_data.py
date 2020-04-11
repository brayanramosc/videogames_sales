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

def return_bar_plot(df):
	fig = go.Figure(data=[go.Bar(
            x=df.index, y=df.Global_Sales,
            text=df.Global_Sales,
            texttemplate='%{text:.2s}',
            textposition='outside',
        )])
	fig.update_layout(
	        title_text = 'Global sales for Genre',
	        showlegend = False,
	        geo = dict(
	            landcolor = 'rgb(217, 217, 217)',
	        ),
	        margin = {'l':0,'b':0.1,'r':0},
	        height =  250,
	    )
	return(fig)

def return_scatter_plot(df):
	trace = go.Scatter(x = df.index,
	                   y = df.Global_Sales.values,
	                  mode = 'lines') #'markers' muestra los puntos y 'lines' las lineas -> mode = 'markers+lines'

	fig = go.Figure([trace])

	fig.update_layout(
	    width = 1000,
	    title = 'Titulo aleatorio',
	)	
	return(fig)