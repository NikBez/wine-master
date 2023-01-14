import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import get_year_word, get_struct_data_from_exel
import argparse

FOUNDATION_YEAR = 1920

def main():

    parser = argparse.ArgumentParser(description="Скрипт создает страницу сайта и подгружает в нее ассортимент из файла wines.xlsx")
    parser.add_argument('-p', '--path', default='wines.xlsx', help="Путь к файлу с каталогом")
    args = parser.parse_args()

    try:
        catalog = get_struct_data_from_exel(args)
    except IOError:
        print('File not found')
        sys.exit()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    year = datetime.datetime.now().year - FOUNDATION_YEAR
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
