import requests
from pprint import pprint
from progress.bar import Bar
#Получение ссылки с аккаунта ВК
token = ''
input_id = str(input('Введите id пользователя: '))
input_count = input('Введите количество фотографий: ')
URL = 'https://api.vk.com/method/'
personal_params = {
  'access_token': token,
  'v': 5.131   
}
groups_url = URL + 'photos.getAll'
groups_params = {
  'count': input_count,
  'owner_id': input_id,
  'extended': 1,
}
list_json = []
dict_url_likes = {}
dict_json = {}
response = requests.get(groups_url, params = {**personal_params, **groups_params})
download = response.json()['response']['items'][:]
for i in download:
  dict_url_likes[i['sizes'][:][-1]['url']] = i['likes']['count']
# pprint(download)

bar = Bar('Загрузка фотографий на Я.Диск...', max = len(dict_url_likes.values()), suffix = '%(percent)d%%', fill = '█')
for img_url, likes in dict_url_likes.items():
  #Загрузка на Я.Диск
  TOKEN = ''
  API_BASE_URL = 'https://cloud-api.yandex.net/'
  headers = {
    'accept': 'application/json',
    'Authorization': f'OAuth {TOKEN}'
  }
  requests.post(API_BASE_URL + 'v1/disk/resources/upload', headers = headers, params = {'path': 'diploma/' + str(likes), 'url': img_url})
  bar.next()
bar.finish()
print('Готово! Фотография(-ии) загружены')
