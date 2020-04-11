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
		html.Img(src="/assets/failed_logo_semillero.png", id='logo_semillero'),
		html.Div(html.H2(['Encabezado']),className='title_header'),
		html.Div(className='clear')
	],className='header')
	return(header)


#Main -> Cuerpo de la página
def return_main(df1, df2, options_dropdown,options_dropdown_publisher):
	main = html.Div(children = [
		html.Div(children=[
			html.Div(html.P('Una persona puede contraer la COVID-19 por contacto con otra que esté'
							'infectada por el virus. La enfermedad puede propagarse de persona a persona' 
							'a través de las gotículas procedentes de la nariz o la boca que salen' 
							'despedidas cuando una persona infectada tose o exhala. Estas gotículas caen' 
							'sobre los objetos y superficies que rodean a la persona, de modo que otras' 
							'personas pueden contraer la COVID-19 si tocan estos objetos o superficies y' 
							'luego se tocan los ojos, la nariz o la boca. También pueden contagiarse si' 
							'inhalan las gotículas que haya esparcido una persona con COVID-19 al toser' 
							'o exhalar. Por eso es importante mantenerse a más de 1 metro (3 pies) de' 
							'distancia de una persona que se encuentre enferma. -Organización Mundial de' 
							'la Salud .Graficas según datos del virus'),id='text'),
			html.Div(className='clear')
		],className='text_container'),

		html.Div(children=[
			html.Div(children=[
				html.Div([dcc.Graph(className = 'graph_container', figure = od.return_bar_plot(df1))]),	
				html.Div(className='clear')
			],className='container_L_top'),

			html.Div(children=[
				html.Div([dcc.Graph(className = 'graph_container', figure = od.return_bar_plot(df2))]),	
				html.Div(className='clear')
			],className='container_R_top'),

			html.Div(children=[
				html.Div([
			    	dcc.Dropdown(
					    options=options_dropdown,
			    		#labelClassName = 'label_rbutton',
					    value='3DS',
					    id = 'wid_select_platform'
					), 
			    ], className = 'dropdown_buttons'),

			    html.Div([
			    	html.Div(className='clear')
			    ],id = 'graph_updating_platform'),

				html.Div(className='clear')

			],className='container_L_bot'),

			html.Div(children=[
				html.Div([
			    	dcc.Dropdown(
					    options=options_dropdown_publisher,
			    		#labelClassName = 'label_rbutton',
					    value='Nintendo',
					    id = 'wid_select_publisher'
					), 
			    ], className = 'dropdown_buttons'),

			    html.Div([
			    	html.Div(className='clear')
			    ],id = 'graph_updating_publisher'),

				html.Div(className='clear')
			],className='container_R_bot'),

			html.Div(className='clear')
		],className='container_graphs'),

		html.Div(className='clear')

	], className = 'main')
	return(main)