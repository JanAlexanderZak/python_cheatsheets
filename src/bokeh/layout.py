from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.io import output_file, show


def layout_():
    x = [2, 3, 4, 5, 6]
    y = [8, 6, 5, 2, 3]

    tools = 'pan, box_zoom, box_select, lasso_select'
    p1 = figure(plot_width=400, tools=tools)
    p1.circle(x, y, size=10,)

    p2 = figure(plot_width=400, tools=tools)
    p2.circle(y, x, size=10,)
    p3 = figure(plot_width=400, tools=tools)
    p3.circle(y, x, size=5,)

    layout = row(column(p1, p2), p3)
    output_file('./output/layout.html')
    show(layout)


if __name__ == '__main__':
    layout_()
