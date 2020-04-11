import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import objects_interface as oi
import objects_data as od
import pandas as pd

from dash.dependencies import Output,Input,State


app = dash.Dash(__name__)

df = od.return_data()
df_opt = pd.DataFrame(df.groupby(['Platform']).agg({'Platform':'unique'}).apply(lambda x:x['Platform'][0],axis =1),columns= ['Platform'])
options_dropdown = [{'label':id_1,'value':id_2} for id_1,id_2 in zip(df_opt.index,df_opt.Platform)]


df1 = df.groupby('Platform', as_index = True).agg({'Global_Sales':'sum'})
df2 = df.groupby('Genre', as_index = True).agg({'Global_Sales':'sum'})
#df_JPN = df[df.iso_alpha == 'JPN']
#df_CHN = df[df.iso_alpha == 'CHN']
#df_country = od.return_data()

header = oi.return_header()
main = oi.return_main(df1,df2,options_dropdown)

app.layout = html.Div([header, main])
#app.layout = html.Div([header])

@app.callback(Output(component_id = 'graph_updating_container', component_property = 'children'),
				[Input(component_id = 'wid_select_platform', component_property = 'value')])

def update_trace(platform_select):
	print(platform_select)
	df_sample = df[df.Platform == platform_select]
	global_sales_by_specific_platform = df_sample.groupby('Year', as_index = True).agg({'Global_Sales':'sum'})
	graph = dcc.Graph(figure = od.return_scatter_plot(global_sales_by_specific_platform))
	return(html.Div([graph], id = 'graph_cases_content'))

if __name__ == "__main__":
    app.run_server(debug=True)