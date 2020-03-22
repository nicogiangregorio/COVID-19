import glob
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def load_data_plot(path, region):
    results = []
    for fname in glob.glob(path):
        df = pd.read_csv(fname)
        df = df[df['codice_regione'] == region[0]]
        df['ratio_positivi_tamponi'] = round(100 * df['totale_attualmente_positivi'] / df['tamponi'], 2)
        results.append(df)
    frame = pd.concat(results).drop_duplicates()

    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1)
    fig.append_trace(go.Scatter(
                    x=frame['data'],
                    y=frame['deceduti'],
                    name="Deceduti"),
                    row=1, col=1)
    fig.append_trace(go.Scatter(
                    x=frame['data'],
                    y=frame['dimessi_guariti'],
                    name="Guariti e dimessi"),
                    row=1, col=1)
    fig.append_trace(go.Scatter(
                    x=frame['data'],
                    y=frame['totale_attualmente_positivi'],
                    name="Positivi attualmente"),
                    row=1, col=1)
    fig.append_trace(go.Scatter(
                    x=frame['data'],
                    y=frame['ratio_positivi_tamponi'],
                    name="% positivi su tamponi"),
                    row=2, col=1)
    '''
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
                    x=frame['data'],
                    y=frame['ratio_positivi_tamponi'],
                    name="\\% positivi su tamponi",
                    hoverinfo='x + y'))

    '''
    fig.write_html(region[1] + '.html', auto_open=True)
    #fig2.write_html(region[1] + '2.html', auto_open=True)
