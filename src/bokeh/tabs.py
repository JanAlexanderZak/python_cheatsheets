from bokeh.plotting import figure
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import row
from bokeh.io import output_file, show


def tabs_():
    x = [2, 3, 4, 5, 6]
    y = [7, 6, 8, 9, 10]
    tools = 'pan, box_zoom, box_select, lasso_select'

    p1 = figure(plot_width=400, tools=tools, title='first', )
    p1.circle(x, y, size=10, )

    p2 = figure(plot_width=400, tools=tools, title='second', )
    p2.circle(y, x, size=10, )

    p3 = figure(plot_width=400, tools=tools, title='third', )
    p3.circle(y, x, size=5, )

    # Create tabs
    first = Panel(child=row(p1, p2), title='first')
    second = Panel(child=row(p3), title='second')

    tabs = Tabs(tabs=[first, second])
    output_file('./output/tabs.html')
    show(tabs)


if __name__ == '__main__':
    tabs_()
