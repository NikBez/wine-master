import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import get_year_word, get_struct_data_from_exel

YEAR_OF_FOUNDATION = 1920

def main():
    catalog = get_struct_data_from_exel()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    year = datetime.datetime.now().year - YEAR_OF_FOUNDATION
    year_word = get_year_word(str(year))

    context = {
        "year": year,
        "year_word": year_word,
        "catalog": catalog,
    }
    rendered_page = template.render(**context)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
