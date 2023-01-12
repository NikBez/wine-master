import argparse
import sys
from collections import defaultdict

from pandas import read_excel


def get_year_word(year):
    """ Функция возвращает правильное слово в зависимости от года, который в нее передается. """

    if year.endswith(('11', '12', '13', '14')):
        return 'лет'
    elif year.endswith('1'):
        return 'год'
    elif year.endswith(('2', '3', '4')):
        return 'года'
    else:
        return 'лет'


def get_struct_data_from_exel():
    """ Функция считывает данные из exel таблицы и возвращает вложенную структуру. """

    catalog = defaultdict(list)

    parser = argparse.ArgumentParser(description="Скрипт создает страницу сайта и подгружает в нее ассортимент из файла wines.xlsx")
    parser.add_argument('-p', '--path', default='wines.xlsx', help="Путь к файлу с каталогом")
    args = parser.parse_args()

    try:
        from_exel = read_excel(io=args.path,
                               sheet_name='wines',
                               usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'],
                               na_values='Сорт неизвестен',
                               keep_default_na=False,
                               )
    except IOError:
        print('File not found')
        sys.exit()

    wines = from_exel.to_dict(orient="records")

    for wine in wines:
        catalog[wine['Категория']].append({'Название': wine['Название'],
                                           'Сорт': wine['Сорт'],
                                           'Цена': wine['Цена'],
                                           'Картинка': wine['Картинка'],
                                           'Акция': wine['Акция']
                                           })
    return catalog
