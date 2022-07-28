# Импортируем модуль connectdb и класса Postgres
from myclass.connectdb import Postgres
#

#
# def fillTable():
#     # Заполняем таблицы
#     l = Postgres('localhost', 'language_db', 'test', 'test')
#     file = File(pathfile)
#     # Бежим по файлу
#     for key, value in file.read().items():
#         # заполняем таблицу language
#         l.executeRequest(f"insert into language (name) values ('{key}');")
#         # Узнаем последний (максимальный) id
#         id = l.executeRequest(f"select max(id) from language;")
#         # Конвертируем данные в словарь
#         id_str = ''.join(l.convertResult(id).get(0))
#         # Заполняем таблицу release
#         l.executeRequest(f"insert into release (id_lang, year) values ({int(id_str)},'{int(value)}');")
# #
# def filltablejson():
#     #
#     cars_db = Postgres('localhost', 'cars_db', 'test', 'test')
#     file = File(pathjson)
#     result = file.readJson()
#     #
#     for key ,value in result['list'].items():
#         print('*', key)
#         # заполняем таблицу brand
#         cars_db.executeRequest(f"insert into brand (name) values ('{key}');")
#         # Узнаем последний (максимальный) id
#         id = cars_db.executeRequest(f"select max(id) from brand;")
#         # Конвертируем данные в словарь
#         id_str = ''.join(cars_db.convertResult(id).get(0))
#         for item in value:
#             #print(' -',item)
#             # Заполняем таблицу model
#             cars_db.executeRequest(f"insert into model (id_brand, name) values ({int(id_str)},'{item}');")
# #

#
def dataset1():
    # Экземпляр класса
    cars_db = Postgres('localhost', 'cars_db', 'test', 'test')
    # Запрос
    request = cars_db.executeRequest('select brand.name, model.name from brand '
                                     'join model on model.id_brand = brand.id;')
    # преобразовываем структуру данных запроса в словарь
    request_convert = cars_db.convertResult(request)
    dictresult = {}
    for key, value in request_convert.items():
        if value[0].strip() not in dictresult:
            dictresult[value[0].strip()] = []
            dictresult[value[0].strip()].append(value[1])
        else:
            dictresult[value[0].strip()].append(value[1])
    print(dictresult)
    return dictresult
    #cars_db.deleteRows('brand')

#

if __name__ == '__main__':
    pass
    #dataset1()
