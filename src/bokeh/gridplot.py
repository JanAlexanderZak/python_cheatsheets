from bokeh.plotting import figure
from bokeh.layouts import gridplot
from bokeh.io import output_file, show


def gridplot_():
    x = [2, 3, 4, 5, 6]
    y = [8, 6, 5, 2, 3]

    tools = 'pan, box_zoom, box_select, lasso_select'
    p1 = figure(plot_width=400, tools=tools)
    p1.circle(x, y, size=10,)

    p2 = figure(plot_width=400, tools=tools)
    p2.circle(y, x, size=10,)

    p3 = figure(plot_width=400, tools=tools)
    p3.circle(y, x, size=5,)

    layout = gridplot(
        [[None, p1], [p2, p3]],
        toolbar_location=None)
    """
    layout = gridplot([p1, p2, p3], ncols=2,
                      toolbar_location=None)
    """
    output_file('./output/gridplot.html')
    show(layout)


if __name__ == '__main__':
    gridplot_()
