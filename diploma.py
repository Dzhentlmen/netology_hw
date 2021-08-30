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
token = ''

class VkPhoto:
  URL = 'https://api.vk.com/method/'
  def __init__(self, token, version, input_screen_name, input_count, input_token, input_path):
    self.params = {
        'access_token': token,
        'v': version    
    }
    self.input_screen_name = input_screen_name
    self.input_count = input_count
    self.input_token = input_token
    self.input_path = input_path

  def GetID(self):
    #Получение owner_id с помощью имени пользователя
    #Getting owner_id using the user name
    url = self.URL + 'utils.resolveScreenName'
    groups_params = {
      'screen_name': self.input_screen_name,
    }
    response = requests.get(url, params = {**self.params, **groups_params})
    user_id = response.json()['response']['object_id']
    return user_id

  def PhotosInfo(self):
    #Получение фотографий с аккаунта ВК
    #Getting photos from the VK account
    url = self.URL + 'photos.getAll'
    groups_params = {
      'count': self.input_count,
      'owner_id': VkPhoto.GetID(self),
      'extended': 1,
    }
    #Создание списков и словарей
    #Creating lists and dictionaries
    list_json = []
    dict_url_likes = {}
    #Запрос на сайт и ввод информации в словари и списки
    #Request to the site and enter information in dictionaries and lists
    response = requests.get(url, params = {**self.params, **groups_params})
    download = response.json()['response']['items'][:]
    for i in download:
      dict_url_likes[i['sizes'][:][-1]['url']] = i['likes']['count']
      list_json.append({'file_name': i['likes']['count']})
    return [dict_url_likes, list_json]

  def YandexDiskUpload (self):
    # Индикатор выполнения
    # Progress Bar
    bar = Bar('Загрузка фотографий на Я.Диск...', max = len(VkPhoto.PhotosInfo(self)[0].values()), suffix = '%(percent)d%%', fill = '█')
    for img_url, likes in VkPhoto.PhotosInfo(self)[0].items():
      #Загрузка на Я.Диск
      #Uploading to Yandex.Disk
      url = 'https://cloud-api.yandex.net/'
      headers = {
        'accept': 'application/json',
        'Authorization': f'OAuth {self.input_token}'
      }
      requests.put(url + 'v1/disk/resources', headers = headers, params = {'path': self.input_path})
      requests.post(url + 'v1/disk/resources/upload', headers = headers, params = {'path': self.input_path + '/' + str(likes), 'url': img_url})
      bar.next()
    # Запись логов о загрузке на Я.Диск в файл log.json
    # Logging about the upload to a Yandex.Disk in file "log.json"
    with open('log.json', 'a') as file:
      file.write(now.strftime("%d-%m-%Y %H:%M") + ': ' + str(VkPhoto.PhotosInfo(self)[1]))
      file.write('\n')
    bar.finish()
    return print('Готово! Фотография(-ии) загружены')

vk_user = VkPhoto(token, '5.131', input('Введите имя пользователя: '), input('Введите количество фотографий: '), input('Введите токен от Я.Диск: '), input_path = str(input('Введите название папки, в которой Вы хотите сохранить фотографии: ')))
vk_user.YandexDiskUpload()
