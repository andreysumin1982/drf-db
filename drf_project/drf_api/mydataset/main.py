# Импортируем модуль connectdb
#
#from myclasses.connectdb import Postgres
from drf_api.myclass.connectdb import Postgres
#

#
def dataset1():
    # Экземпляр класса Postgres
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
    return dictresult

#
if __name__ == '__main__':
    pass
    #dataset1()
