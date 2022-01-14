from bokeh.plotting import figure
from bokeh.io import output_file, show

import numpy as np


def line_plot():
    x = np.linspace(0, 5, 1000)
    y = np.sin(x)
    tools = 'pan, box_zoom, box_select, lasso_select'

    plot = figure(plot_width=400, tools=tools)
    plot.line(x, y, line_width=0.5)
    plot.circle(x, y, fill_color="white", size=10, )

    output_file('./output/line_plot.html')
    show(plot)


if __name__ == '__main__':
    line_plot()
