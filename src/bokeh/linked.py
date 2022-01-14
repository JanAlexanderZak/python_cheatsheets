from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import row
from bokeh.io import output_file, show


def linked():
    source = ColumnDataSource(data={
        'x': [2, 3, 4, 5, 6],
        'y': [8, 6, 5, 2, 3], })

    tools = 'pan, box_zoom, box_select, lasso_select'

    p1 = figure(plot_width=400, tools=tools, title='first',)
    p1.circle(
        source=source,
        size=10,
        color='red',
    )
    p2 = figure(plot_width=400, tools=tools, title='second',)
    p2.circle(
        source=source,
        size=10,
    )
    p3 = figure(plot_width=400, tools=tools, title='third',)
    p3.circle(
        source=source,
        size=5,
    )

    # Link all axes
    p3.x_range = p2.x_range = p1.x_range
    p3.y_range = p2.y_range = p1.y_range

    # Create tabs
    first = Panel(child=row(p1, p2), title='first')
    second = Panel(child=row(p3), title='second')

    tabs = Tabs(tabs=[first, second])
    output_file('./output/linked.html')
    show(tabs)


if __name__ == '__main__':
    linked()
