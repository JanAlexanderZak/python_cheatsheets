from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CategoricalColorMapper, HoverTool
from bokeh.io import output_file, show, curdoc
from bokeh.sampledata.iris import flowers

# Flowers is a pd.df
source = ColumnDataSource(flowers)
mapper = CategoricalColorMapper(
    factors=['setosa', 'virginica', 'versicolor'],
    palette=['red', 'green', 'blue'], )
hover = HoverTool(tooltips=[
    ('species name', '@species'),
    ('petal length', '@petal_length'),
    ('sepal length', '@sepal_length'), ])
tools = [hover, 'pan, box_zoom, box_select, lasso_select']

plot = figure(plot_width=400, tools=tools)
plot.circle(
    'sepal_length',
    'petal_length',
    selection_color='red',
    nonselection_fill_alpha=0.2,
    nonselection_fill_color='grey',
    size=10,
    source=source,
    color={'field': 'species',
           'transform': mapper}
)

output_file('./output/hover.html')
show(plot)

# bokeh serve --show myapp.py
curdoc().add_root(plot)
