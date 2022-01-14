from dash.dependencies import Input, Output
from jupyter_dash import JupyterDash

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

df = px.data.gapminder()
col_options = [dict(label=x, value=x) for x in df['year'].unique()]
# print(col_options)

app = JupyterDash(__name__)

app.layout = html.Div(children=[
    html.H1("Demo: Plotly Express and Dash"),
    dcc.Dropdown(id="year", value=2007, options=col_options),
    dcc.Graph(id="graph", figure={}),
    dcc.Graph(id="graph2", figure={})
])


@app.callback(
    Output('graph', 'figure'),
    [Input('year', 'value')])
def cb(year):
    year = year if year else 2007
    df_year = df.query(f"year == {year}")
    return px.scatter(df_year, x="gdpPercap", y="lifeExp", size="pop", log_x=True, size_max=60, height=400,
                      custom_data=[df_year.index]).update_layout(dragmode="lasso")


@app.callback(
    Output('graph2', 'figure'),
    [Input('year', 'value'), Input('graph', 'selectedData')])
def display_selected_data(year, selectedData):
    year = year if year else 2007
    df_year = df.query(f"year == {year}")
    if selectedData:
        indices = [point["customdata"][0] for point in selectedData["points"]]
        df_year = df_year.loc[indices]
    return px.scatter_geo(df_year, locations="iso_alpha", size="pop", height=400)


app.run_server()

