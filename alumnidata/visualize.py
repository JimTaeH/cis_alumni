import plotly.express as px
from plotly.offline import plot

def piechart(data=None, val=None, labels=None):
    fig = px.pie(data, values=val, names=labels)
    pie_plot = plot(fig, output_type="div")

    return pie_plot