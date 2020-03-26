import tornado.template as template
import html

def fill_template(filename, graph1, graph2, region):
    loader = template.Loader("COVID-19/docs/html")
    out = loader.load(filename).generate(graph1=graph1, graph2=graph2, region=region)
    
    return html.unescape(str(out.decode('utf-8')))
