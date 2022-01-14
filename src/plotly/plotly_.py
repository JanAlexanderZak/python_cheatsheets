import plotly.express as px
# https://plotly.com/python/animations/

# Social data: Generosity, Social Support
fig_2 = px.scatter(
    df, x="Social Support", y="Happiness Score", animation_frame="Year", animation_group="Country", symbol="Continent",
    size="Generosity", color="Continent", hover_name="Country",
    log_y=False, log_x=False, size_max=30,
    title="Social data: Support, Generosity (on hover) and over Happiness", opacity=0.7,
    height=600, range_y=[-0.15, 10], range_x=[-0.015, 1.5], )
fig_2.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
fig_1['data'][0]['showlegend'] = True
fig_2.write_html("../html_plots/plot_2_.html")
fig_2.write_image("../static/plot_2.svg")
fig_2.show()

# Gapminder 4D plot
df = px.data.gapminder()
fig = px.scatter(
    df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
    size="pop", color="continent", hover_name="country",
    log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90])
fig.show()

df = px.data.stocks(indexed=True)
fig = px.line(df, facet_col="company", facet_col_wrap=2)
fig.add_hline(y=1, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline",
              annotation_position="bottom right")

fig.add_vrect(x0="2018-09-24", x1="2018-12-18", col=1,
              annotation_text="decline", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
fig.show()


# Geografical plot
cols_dd = [
    "Happiness Score", "Happiness Rank", "Social Support", "Life Expectancy",
    "Freedom", "Corruption", "Generosity", "GDP per Capita", ]
visible = np.array(cols_dd)

traces, buttons = [], []
for value in cols_dd:
    traces.append(go.Choropleth(
        locationmode='country names',
        locations=df['Country'],
        colorscale=px.colors.sequential.Blues,
        hoverinfo='location+z',
        z=df[value].astype(float),
        colorbar_title=value,
        visible=True if value == cols_dd[0] else False))
    buttons.append(dict(label=value,
                        method="update",
                        args=[{
                            "visible": list(visible == value), },
                              {
                                  "title": f"Interactive geo-map. Selected data: <b>{value}</b>", }]))
    updatemenus = [{
        "active": 0,
        "buttons": buttons, }]

fig = go.Figure(
    data=traces,
    layout=dict(updatemenus=updatemenus))
first_title = cols_dd[0]
fig.update_layout(title=f"<b>{first_title}</b>", title_x=0.5)
fig.write_html("../html_plots/geo_map_.html")
fig.write_image("../static/geo_map.svg")
fig.show()

"""
fig = px.choropleth(df, locationmode='country names', locations=df["Country"],
                    color="Generosity",
                    hover_name="Country",
                    hover_data=[df['Corruption'], df['GDP per Capita']],
                    color_continuous_scale=px.colors.sequential.deep, title="PLOT", height=600)
fig.show()
fig.write_image("../static/geo_map_2.svg")
exit()
"""
