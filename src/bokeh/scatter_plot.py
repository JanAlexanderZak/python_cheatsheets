from bokeh.plotting import figure
from bokeh.io import output_file, show


def scatter_plot():
    x = [2, 3, 4, 5, 6]
    y = [7, 6, 8, 9, 10]
    tools = 'pan, box_zoom, box_select, lasso_select'

    plot = figure(plot_width=400, tools=tools)
    plot.circle(x, y, size=10, )

    output_file('./output/scatter_plot.html')
    show(plot)


if __name__ == '__main__':
    scatter_plot()
