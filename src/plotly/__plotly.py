import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

monthly_sales = {
    'data': [{'type': 'bar', 'x': ['Jan', 'Feb', 'March'], 'y': [450, 475, 400]}],
     'layout': {'title': {'text': 'Sales for Jan-Mar 2020'}}}

fig = go.Figure(monthly_sales)
#fig.show()

df = pd.DataFrame.from_dict({
    "student_name": ["alex", "alex1", "alex3"],
    "score": [0.8, 0.9, 1],
    "city": ["Berlin", "Munich", "Berlin"], })
print(df)

# Custom colors
fig = px.bar(
    data_frame=df,
    x="student_name", y="score",
    color_discrete_map={
        'Berlin': 'rgb(0, 0, 201)',
        "Munich": "rgb(235, 207, 52)",
    },
    color="city")
fig.show()

# go
# Create a correlation table with pandas
penguin_corr = penguins.corr(method='pearson')

# Set up the correlation plot
fig = go.Figure(go.Heatmap(
  		# Set the appropriate x, y and z values
        z=penguin_corr.values.tolist(),
        x=penguin_corr.columns,
        y=penguin_corr.columns,
  		# Set the color scale,
        colorscale='rdylgn',
  		# Set min and max values
        zmin=-1, zmax=1))

# Show the plot
fig.show()



# legends

# Create the legend
my_legend = {'x': 0.2, 'y': 0.95,
            'bgcolor': 'rgb(60, 240, 201)', 'borderwidth': 5}
# Update the figure
fig.update_layout({'showlegend': True, 'legend': my_legend})



# Annotation
# Create the first annotation
loss_annotation = {'x': 10, 'y': 400, 'showarrow': True, 'arrowhead': 4,
                    'font': {'color': 'black'}, 'text': "Urgent House Repairs"}

# Create the second annotation
gain_annotation = {'x': 18, 'y': 2500, 'showarrow': True, 'arrowhead': 4,
                    'font': {'color': 'black'}, 'text': "New Job!"}

# Add annotations to the figure
fig.update_layout({'annotations': [loss_annotation, gain_annotation]})

# Message annotation
# Get and format today's date
today = datetime.today().strftime('%A')

# Create the message_annotation
message_annotation = {
  # Set the correct coordinates
  'x': 0.5, 'y': 0.95, 'xref': 'paper', 'yref': 'paper',
  # Set format the text and box
  'text': f'Have a Happy {today} :)',
  'font': {'size': 20, 'color': 'white'},
  'bgcolor': 'rgb(237, 64, 200)', 'showarrow': False}

# Update the figure layout and show
fig.update_layout({'annotations': [message_annotation]})



# X axis scale
# Create and show the plot
fig = px.scatter(
  data_frame=bball_data,
  x='PPG',
  y='FGP',
  title='Field Goal Percentage vs. Points Per Game')
fig.show()

# Update the x_axis range
fig.update_layout({'xaxis': {'range': [0, bball_data['PPG'].max() + 5]}})
fig.show()

# Update the y_axis range
fig.update_layout({'yaxis': {'range' : [0, 100]}})


# Subplots
# Create the subplots
fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

# Loop through the industries
row_num = 1
for industry in ['Tech', 'Retail', 'Professional Services']:
    df = revenues[revenues.Industry == industry]
    # Add a histogram using subsetted df
    fig.add_trace(go.Histogram(x=df['Revenue'], name=industry),
    # Position the trace
    row=row_num, col=1)
    row_num +=1


# Buttons
# Create the basic line chart
fig = px.line(data_frame=tesla, x='Date', y='Open', title="Tesla Opening Stock Prices")

# Create the financial buttons
fin_buttons = [
  {'count': 7, 'label': "1WTD", 'step': "day", 'stepmode': "todate"},
  {'count': 6, 'label': "6MTD", 'step': "month", 'stepmode': "todate"},
  {'count': 1, 'label': "YTD", 'step': "year", 'stepmode': "todate"}
]

# Create the date range buttons & show the plot
fig.update_layout({'xaxis': {'rangeselector': {'buttons': fin_buttons}}})
fig.show()

#####

# Create a simple bar chart
fig = px.bar(data_frame=rain, x='Month', y='Rainfall')

# Create the buttons
my_buttons = [{'label': "Bar plot", 'method': "update", 'args': [{"type": "bar"}]},
{'label': "scatterplot", 'method': "update", 'args': [{"type": "scatter", 'mode': 'markers'}]}]

# Add buttons to the plot and show
fig.update_layout({
    'updatemenus': [{
      'type': "buttons",'direction': 'down',
      'x': 1.3,'y': 0.5,
      'showactive': True,'active': 0,
      'buttons': my_buttons}]})
fig.show()



# Create the basic figure
fig = go.Figure()

# Add a trace per metric
fig.add_trace(go.Bar(x=sales["Month"], y=sales["Sales Volume"], name='Sales Volume'))
fig.add_trace(go.Bar(x=sales["Month"], y=sales["Sales Value"], name='Sales Value'))

# Create annotations
value_annotations=[{'text': 'Sept was the best' ,'showarrow': True, 'x': 'September', 'y': 345397 }]
volume_annotations=[{'text': 'Oct was the best', 'showarrow': True, 'x': 'October', 'y': 71900 }]

# Create buttons
my_buttons = [
{'label': "By Sales Value", 'method': "update", 'args': [{}, {"annotations": value_annotations}]},
{'label': "By Sales Volume", 'method': "update", 'args': [{}, {"annotations": volume_annotations}]}
]

# Add the buttons
fig.update_layout({
    'updatemenus':[{
            'type': "buttons",
            'direction': 'down',
            'x': 1.3,'y': 0.5, 'buttons': my_buttons
            }]})
fig.show()


###

# slider

# Create the basic figure
fig = go.Figure()

# Loop through the states
for season in ['Autumn', 'Winter', 'Spring']:
    # Subset the DataFrame
    df = rain_pm[rain_pm.Season == season]
    # Add a trace for each season
    fig.add_trace(go.Bar(x=df["Month"], y=df["Total Rainfall"], name=season))

# Create the slider elements
sliders = [
    {'steps': [
        {'method': 'update', 'label': 'Autumn', 'args': [{'visible': [True, False, False]}]},
        {'method': 'update', 'label': 'Winter', 'args': [{'visible': [False, True, False]}]},
        {'method': 'update', 'label': 'Spring', 'args': [{'visible': [False, False, True]}]}]}]

# Update the figure to add sliders and show
fig.update_layout({'sliders': sliders})

# Show the plot
fig.show()



### dropdown




