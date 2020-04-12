import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import objects_data as od
import numpy as np

#Header
def return_header():
	header=html.Div(children=[
		html.Img(src="/assets/Logo_UdeA.png", id='logo_udea'),
		html.Img(src="/assets/Logo_semillero.png", id='logo_semillero'),
		html.Div(html.H2(['Videogames sales']),className='title_header'),
		html.Div(className='clear')
	],className='header')
	return(header)


#Main -> Cuerpo de la página
def return_main(df1, df2, df3, options_dropdown_publisher):
	main = html.Div(children = [
		html.Div(children=[
			html.Div(html.P('This dataset contains a list of video games with sales greater than 100,000 copies (1980-2020).\LF'

							'Fields include:'

							'Rank - Ranking of overall sales.'
							'Name - The games name.'
							'Platform - Platform of the games release (i.e. PC,PS4, etc.).'
							'Year - Year of the games release.'
							'Genre - Genre of the game.'
							'Publisher - Publisher of the game.'
							'NA_Sales - Sales in North America (in millions).'
							'EU_Sales - Sales in Europe (in millions).'
							'JP_Sales - Sales in Japan (in millions).'
							'Other_Sales - Sales in the rest of the world (in millions).'
							'Global_Sales - Total worldwide sales.'),id='text'),
			html.Div(className='clear')
		],className='text_container'),

		html.Div(children=[
			html.Div(children=[
				html.Div([dcc.Graph(className = 'graph_container', figure = od.return_bar_plot(df1, 'plataforma'))]),	
				html.Div(className='clear')
			],className='container_L_top'),

			html.Div(children=[
				html.Div([dcc.Graph(className = 'graph_container', figure = od.return_bar_plot(df2, 'genero'))]),	
				html.Div(className='clear')
			],className='container_R_top'),

			html.Div(children=[
				html.Div([
			    	dcc.Dropdown(
					    options=options_dropdown_publisher,
			    		#labelClassName = 'label_rbutton',
					    value='Nintendo',
					    id = 'wid_select_publisher_1'
					), 
			    ], className = 'dropdown_buttons'),

			    html.Div([
			    	html.Div(className='clear')
			    ],id = 'graph_updating_publisher_1'),

				html.Div(className='clear')

			],className='container_L_bot'),

			html.Div(children=[
				html.Div([
			    	dcc.Dropdown(
					    options=options_dropdown_publisher,
			    		#labelClassName = 'label_rbutton',
					    value='Nintendo',
					    id = 'wid_select_publisher_2'
					), 
			    ], className = 'dropdown_buttons'),

			    html.Div([
			    	html.Div(className='clear')
			    ],id = 'graph_updating_publisher_2'),

				html.Div(className='clear')
			],className='container_R_bot'),

			html.Div(className='clear')
		],className='container_graphs'),

		html.Div(children=[
			html.Div([dcc.Graph(className = 'graph_container', figure = od.return_name_plot(df3))]),	
				html.Div(className='clear')
		],className='graph_container_bot'),

		html.Div(className='clear')

	], className = 'main')
	return(main)