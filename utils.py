from collections import defaultdict

from pandas import read_excel


# Функция возвращает правильное слово в зависимости от года, который в нее передается
def get_year_word(year):
    if year.endswith(('11', '12', '13', '14')):
        return 'лет'
    elif year.endswith('1'):
        return 'год'
    elif year.endswith(('2', '3', '4')):
        return 'года'
    else:
        return 'лет'

# Функция считывает данные из exel таблицы и возвращает вложенную структуру
def get_struct_data_from_exel():
    items_structure = defaultdict(list)

    items_from_exel = read_excel(io='wines.xlsx',
                                 sheet_name='wines',
                                 usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'],
                                 na_values='Сорт неизвестен',
                                 keep_default_na=False,
                                 )
    wines = items_from_exel.to_dict(orient="records")

    for wine in wines:
        items_structure[wine['Категория']].append({'Название': wine['Название'],
                                                   'Сорт': wine['Сорт'],
                                                   'Цена': wine['Цена'],
                                                   'Картинка': wine['Картинка'],
                                                   'Акция': wine['Акция']
                                                   })
    return items_structure
