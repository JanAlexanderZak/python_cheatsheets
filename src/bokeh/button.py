from bokeh.models import Button, CheckboxGroup, RadioGroup, Toggle
from bokeh.io import curdoc


def on_click():
    print('Hello world!')


# All buttons have different implementations
bt = Button(label='Click me')
toggle = Toggle(label='toggle', button_type='success')
checkbox = CheckboxGroup(labels=['1', '2', '3'])
radio = RadioGroup(labels=['1', '2', '3'])

bt.on_click(on_click)
curdoc().add_root(bt)
