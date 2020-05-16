from load_files import build_plot
from data_loader import DataLoader
from html_template_gen import fill_template
import html

dl = DataLoader()
national_data = dl.get_national_data()
regional_data = dl.get_regional_data()