import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

import plotly.express as px
from data_loader import DataLoader

def build_plot(region_id, regional_frame, national_frame):
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['deceduti'],
                    mode='lines+markers',
                    name="Deceduti"))
    fig1.add_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['dimessi_guariti'],
                    mode='lines+markers',
                    name="Guariti"))
    fig1.add_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['totale_attualmente_positivi'],
                    mode='lines+markers',
                    name="Positivi attualmente"))
    fig1.add_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['nuovi_attualmente_positivi'],
                    mode='lines+markers',
                    name="Nuovi positivi"))
    fig1.update_layout(legend_orientation="h")
    
    fig2 = go.Figure()
   
    fig2.add_trace(go.Scatter(
                    x=regional_frame['data'],
                    y=regional_frame['ratio_positivi_tamponi'],
                    mode='lines+markers',
                    name="% regionale"))
    fig2.add_trace(go.Scatter(
                    x=national_frame['data'],
                    y=national_frame['ratio_positivi_tamponi'],
                    mode='lines+markers',
                    name="% nazionale"))
    fig2.update_layout(legend_orientation="h")
    
    out1 = fig1.to_html(include_plotlyjs=False, full_html=False)
    out2 = fig2.to_html(include_plotlyjs=False, full_html=False)

    fig2.write_html('temp.html',full_html=False, auto_open=True)
    return {'graph1': out1, 'graph2': out2}