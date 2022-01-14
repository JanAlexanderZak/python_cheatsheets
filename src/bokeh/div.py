from bokeh.models import Div
from bokeh.io import output_file, show


def div_():
    div = Div(text="<b>Hello world!</b>", style={'font-size': '200%', 'color': 'black'})

    output_file('./output/div.html')
    show(div)


if __name__ == '__main__':
    div_()


