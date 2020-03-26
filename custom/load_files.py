import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def build_plot(region_id, regional_frame, national_frame):
    fig1 = go.Figure()
    fig1 = make_subplots(rows=1, cols=1)
    fig1.append_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['deceduti'],
                    name="Deceduti"),
                    row=1, col=1)
    fig1.append_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['dimessi_guariti'],
                    name="Guariti"),
                    row=1, col=1)
    fig1.append_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['totale_attualmente_positivi'],
                    name="Positivi attualmente"),
                    row=1, col=1)
    fig1.append_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['nuovi_attualmente_positivi'],
                    name="Nuovi positivi"),
                    row=1, col=1)
    fig1.update_layout(legend_orientation="h")
    
    fig2 = go.Figure()
    fig2 = make_subplots(rows=1, cols=1)
    fig2.append_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['ratio_positivi_tamponi'],
                    name="% regionale"),
                    row=1, col=1)
    fig2.append_trace(go.Scatter(
                    x=national_frame['data'],
                    y=national_frame['ratio_positivi_tamponi'],
                    name="% nazionale"),
                    row=1, col=1)
    fig2.update_layout(legend_orientation="h")
    
    out1 = fig1.to_html(include_plotlyjs=False, full_html=False)
    out2 = fig2.to_html(include_plotlyjs=False, full_html=False)
    return {'graph1': out1, 'graph2': out2}