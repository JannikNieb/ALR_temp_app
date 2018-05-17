from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.plotting import figure, output_file, show

from flask import Flask, render_template, flash
from datetime import datetime, date


app = Flask(__name__)
# receiving data


# processing data


# visualize data in a graph

def create_graph():
    print(datetime.now())
    data_x = [1, 2, 3]
    data_y = [3, 34, 3]

    p = figure(plot_width=400, plot_height=400)

    p.line(data_x, data_y, line_width=2)
    p.circle(data_x, data_y, fill_color="white", size=8)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(p)
    return render_template("index.html", script=script, div=div, js_resources=js_resources, css_resources=css_resources)\


@app.route('/')
def execute():
    render_template = create_graph()
    return render_template


if __name__ == "__main__":
    app.run(port=5000, debug=True)
