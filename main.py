import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from utils import get_year_word, get_struct_data_from_exel

items_structure = get_struct_data_from_exel()

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')

year = datetime.datetime.now().year - 1920
year_word = get_year_word(str(year))

context = {
    "year": year,
    "year_word": year_word,
    "items_structure": items_structure,
}
rendered_page = template.render(**context)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
