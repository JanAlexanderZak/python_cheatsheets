from bokeh.plotting import figure
from bokeh.models import CategoricalColorMapper, ColumnDataSource
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers


def plot_from_pandas():
    # Flowers is a pd.df
    source = ColumnDataSource(flowers)
    mappper = CategoricalColorMapper(
        factors=['setosa', 'virginica', 'versicolor'],
        palette=['red', 'green', 'blue'], )
    tools = 'pan, box_zoom, box_select, lasso_select'

    plot = figure(plot_width=400, tools=tools)
    plot.circle(
        'sepal_length',
        'petal_length',
        selection_color='red',
        nonselection_fill_alpha=0.2,
        nonselection_fill_color='grey',
        size=10,
        source=source,
        color={
            'field': 'species',
            'transform': mappper, }
    )

    output_file('./output/plot_from_pandas.html')
    show(plot)


if __name__ == '__main__':
    plot_from_pandas()
