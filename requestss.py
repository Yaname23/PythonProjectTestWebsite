#библиотека requests

import requests
import json
"""Тип запроса GET используется, чтобы запросить данные, 
хранящиеся на сервере. Библиотека requests позволяет отправить такой запрос следующим
 образом: res = requests.get(url, headers=headers, params=params)"""

status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
if 'application/json' in res.headers['Content-Type']:
    res.json()
else:
    res.text
print(res.status_code)
print(res.text)

"""Тип запроса POST
Используется для отправки любых данных на сервер для их обработки или сохранения в базу данных.
шаблон: res = requests.post(url, headers=headers, data=data)
Где: url и header — уже известные нам параметры.

data — это данные, отправляемые на сервер в теле запроса. Передаются в формате словаря 
data = {‘key1’: ‘value1’, ‘key2’: ‘value2’}.

В res также возвращается результат выполнения запроса с кодом состояния и ответной
 информацией, как и в GET-запросе."""

"""Тип запроса DELETE
Используется для удаления какого-либо объекта данных на сервере.
 Для этого в качестве параметров запроса также обязательно передаётся url-адрес,
  на который делается запрос. В зависимости от того, как сервер читает входящий запрос, 
  соответственно передаются и остальные параметры.

res = requests.delete(url, **kwargs)"""


"""
Тип запроса PUT
Используется для изменения данных на сервере. В качестве параметров также принимает url и данные data для внесения изменений. 

По своей сути очень похож на POST-запрос.

res = requests.put(url, data=data)
"""





