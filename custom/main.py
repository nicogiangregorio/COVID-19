from load_files import build_plot
from data_loader import DataLoader
from html_template_gen import fill_template
import html

dl = DataLoader()
national_data = dl.get_national_data()
regional_data = dl.get_regional_data()

for key_region, region_value in regional_data.items():
    plots = build_plot(key_region, region_value, national_data)
    html_out = fill_template("template.html", plots['graph1'], plots['graph2'], region_value['denominazione_regione'].values[0])

    with open('COVID-19/docs/html/' + str(key_region) + ".html", 'w') as out:
        out.write(html_out)