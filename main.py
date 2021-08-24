import requests
from pprint import pprint

#https://yandex.ru/dev/disk/poligon
TOKEN = 'AQAAAAA0PqSxAADLW0QNkVCS60kIkwupvRZDqUk'

API_BASE_URL = 'https://cloud-api.yandex.net/'

headers = {
  'accept': 'application/json',
  'Authorization': f'OAuth {TOKEN}'
}

# response = requests.get(API_BASE_URL + 'v1/disk', headers = headers)
# #v1/disk/resources/files
# files_list_response = requests.get(API_BASE_URL + 'v1/disk/resources/files', headers = headers)
# files = files_list_response.json()['items']
# photo = files[0]
# photo_response = requests.get(photo['file'])
# with open('photo.jpeg', 'wb') as img:
#   img.write(photo_response.content)
# pprint(files_list_response.json())
# pprint(response)
# pprint(response.json())


# #Загрузка файла в папку на Яндекс.диск
# # 1-й запрос - получение ссылки для загрузки файла
# r = requests.get(API_BASE_URL + 'v1/disk/resources/upload', params = {'path': 'py44/photo.jpeg'}, headers = headers)
# pprint(r.status_code)
# pprint(r.json())

# # 2-й запрос - загрузка файла на диск по полученной ссылке
# upload_url = r.json()['href']
# r = requests.put(upload_url, headers = headers, files = {'file': open('photo.jpeg', 'rb')})

# #Альтернативный вариант
# img_url = 'https://aptos.ru/upload/iblock/db8/db8bcd551b81ed18bf88c2070d53d9dd.png'
# requests.post(API_BASE_URL + 'v1/disk/resources/upload', headers = headers, params = {'path': 'py44/img1.png', 'url': img_url})



# #Скачать самый популярный видос с Reddit:
# headers = {'user-agent': 'netology-py44'}
# response = requests.get('https://www.reddit.com/r/gifs/top.json?t=day', params = {'t': 'day'}, headers = headers)
# pprint(response.json())


##Задание 1
#1. Сделать запрос API_BAS_URL +/name
# В ответе id
#2. Делаем запрос id/
# В ответе статы
##Задание 2
#1-й запрос - получение ссылки для загрузки файла
#2-й запрос - загрузка файла на диск по полученной ссылке
#Файл нужно принять из пользовательского ввода


#Homework
#Task 1
import requests
from pprint import pprint
#метод /search/name
#API: 2619421814940190

TOKEN = '2619421814940190'
API_BASE_URL = 'https://superheroapi.com/api/2619421814940190/'

print('**********ЗАДАНИЕ №1**********')
maximum = 0
list_names = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {}
for name in list_names:
  response = requests.get(API_BASE_URL + 'search/' + name)
  intelligence = response.json()['results'][0]['powerstats']['intelligence']
  intelligence_dict[name] = intelligence
  print(f'Имя персонажа -> {name}')
  print(f'Уровень интеллекта -> {intelligence}')
for key, value in intelligence_dict.items():
  if int(value) > maximum:
    maximum = int(value)
print(f'Максимальный уровень интеллекта среди данных персонажей -> {maximum}')

#Task 2
print('**********ЗАДАНИЕ №2**********')
import os
import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
      self.token = token

    def upload(self, file_path: str):
      API_BASE_URL = 'https://cloud-api.yandex.net/'
      headers = {
        'accept': 'application/json',
        'Authorization': f'OAuth {TOKEN}'
      }
      #1-й запрос - получение ссылки для загрузки файла
      r = requests.get(API_BASE_URL + 'v1/disk/resources/upload', params = {'path': 'py43/' + str(name)}, headers = headers)
      # pprint(r.json())
      #2-й запрос - загрузка файла на диск по полученной ссылке
      upload_url = r.json()['href']
      r = requests.put(upload_url, headers = headers, files = {'file': open(str(name), 'rb')})

if __name__ == '__main__':
  path = os.path.abspath(str(input('Введите имя файла: ')))
  name = os.path.basename(path)
  TOKEN = input('Введите Ваш токен: ')

  uploader = YaUploader(TOKEN)
  result = uploader.upload(path)

# #Task3
print('**********ЗАДАНИЕ №3**********')
import requests
from pprint import pprint

API_BASE_URL = 'https://api.stackexchange.com/2.3/questions?fromdate=1628380800&todate=1628553600&order=desc&sort=activity&tagged=python&site=stackoverflow'
response = requests.get(API_BASE_URL)
print(response.status_code)
items_list = response.json()['items']
for i in items_list:
  print(i['title'])
















