from config import regioni
from config import path
from load_files import load_data_plot

for region in regioni:
    load_data_plot(path, region)