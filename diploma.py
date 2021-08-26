#Дата(ДД/ММ/ГГ)
#Date(DD/MM/YY)
import datetime
now = datetime.datetime.now()
#Другие библиотеки
#Other libraries
import requests
from pprint import pprint
from progress.bar import Bar

#Токен программы ВК
#VK Program Token
token = '0cce3a725e6316f5f33bcb6ce1af7133f58e0d1c6aea1268ae56c63b5837e43b74682a33b8f8be4d91c26'

#TOKEN = 'AQAAAAA0PqSxAADLW0QNkVCS60kIkwupvRZDqUk'
#Получение данных от пользователя
#Getting data from the user
input_screen_name = input('Введите имя пользователя: ')
input_count = input('Введите количество фотографий: ')
input_token = input('Введите токен от Я.Диск: ')

#Получение owner_id с помощью имени пользователя
#Getting owner_id using the user name
URL = 'https://api.vk.com/method/'
personal_params = {
  'access_token': token,
  'v': 5.131   
}
groups_url = URL + 'utils.resolveScreenName'
groups_params = {
  'screen_name': input_screen_name,
}
response = requests.get(groups_url, params = {**personal_params, **groups_params})
user_id = response.json()['response']['object_id']


#Получение фотографий с аккаунта ВК
#Getting photos from the VK account
URL = 'https://api.vk.com/method/'
personal_params = {
  'access_token': token,
  'v': 5.131   
}
groups_url = URL + 'photos.getAll'
groups_params = {
  'count': input_count,
  'owner_id': user_id,
  'extended': 1,
}

#Создание списков и словарей
#Creating lists and dictionaries
list_json = []
dict_url_likes = {}

#Запрос на сайт и ввод информации в словари и списки
#Request to the site and enter information in dictionaries and lists
response = requests.get(groups_url, params = {**personal_params, **groups_params})
download = response.json()['response']['items'][:]
for i in download:
  dict_url_likes[i['sizes'][:][-1]['url']] = i['likes']['count']
  list_json.append({'file_name': i['likes']['count']})

#Индикатор выполнения
#Progress Bar
bar = Bar('Загрузка фотографий на Я.Диск...', max = len(dict_url_likes.values()), suffix = '%(percent)d%%', fill = '█')
for img_url, likes in dict_url_likes.items():
  #Загрузка на Я.Диск
  #Uploading to Yandex.Disk
  API_BASE_URL = 'https://cloud-api.yandex.net/'
  headers = {
    'accept': 'application/json',
    'Authorization': f'OAuth {input_token}'
  }
  requests.post(API_BASE_URL + 'v1/disk/resources/upload', headers = headers, params = {'path': 'diploma/' + str(likes), 'url': img_url})

  #Запись логов о загрузке на Я.Диск в файл log.json
  #Logging about the upload to a Yandex.Disk in file "log.json"
  with open('log.json', 'a') as file:
    for dict_file in list_json:
      dict_file['size'] = i['sizes'][:][-1]['type']
    file.write(now.strftime("%d-%m-%Y %H:%M") + ': ' + str(list_json))
    file.write('\n')
  bar.next()
bar.finish()
print('Готово! Фотография(-ии) загружены')
