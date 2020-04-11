import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import objects_data as od
import numpy as np

#Header
def return_header():
	header = html.Div(children=[
		html.Div(children=[
		    html.Img(src = "/assets/Logo_UdeA.png",className='udea'),
		    html.Img(src = "/assets/Logo_semillero.png",className='semillero'),
		    html.Div(className='clear')
		], className = 'img_container'),

		html.Div(html.H2(['Videogames sales']),className='title'),
		html.Div(className='clear')
	], className = 'header')
	return(header)


#Main -> Cuerpo de la página
def return_main(df1, df2, options_dropdown):
	main = html.Div(children = [
		html.Div(children=[
		    html.P(
		    	'Párrafo aleatorio Párrafo aleatorio Párrafo aleatorio'
		    	' Párrafo aleatorio Párrafo aleatorio Párrafo aleatorio'
		    	' Párrafo aleatorio Párrafo aleatorio Párrafo aleatorio'
		    	' Párrafo aleatorio Párrafo aleatorio Párrafo aleatorio'
		    	' Párrafo aleatorio Párrafo aleatorio Párrafo aleatorio'
		    	' Párrafo aleatorio Párrafo aleatorio'
		    	),

		    html.Div(children = [
		    	html.Div([dcc.Graph(className = 'graph_container', figure = od.return_bar_plot(df1))]),
		    	html.Div(className='clear')
		    ],className = 'indicators'),
		 
		], className = 'article'),

		html.Div(children = [
			html.Div([
		    	dcc.Dropdown(
				    options=options_dropdown,
		    		#labelClassName = 'label_rbutton',
				    value='Nintendo',
				    id = 'wid_select_publisher'
				), 

		    ], className = 'radio_buttons'),

		    html.Div([
		    	html.Div(className='clear')
		    ],id = 'graph_updating_container'),

		    html.Div([
		    	html.Div([dcc.Graph(className = 'graph_container', figure = od.return_bar_plot(df2))]),
		    	html.Div(className='clear')
		    ])

		], className = 'left_container')

	], className = 'main')
	return(main)