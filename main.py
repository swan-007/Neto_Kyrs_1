
import requests
import json
import yadisk

file_information = {}

class vk:
    file_info = {}
    silka = []
    def __init__(self,user_id,token, version='5.131'):
        self.token = token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}


    def _get_pho(self):

        url = 'https://api.vk.com/method/photos.get'
        para = {'owner_id': self.id,
                'album_id': 'profile',
                'rev': 1,
                'extended': 1,
                'count': 1,
                'photo_sizes': 1
                }
        respons = requests.get(url, params={**self.params, **para})
        x = respons.json()
        f= x['response']['items'][0]['sizes']#[-1]['url']
        for i in f:
            if i['type'] == 'z':
                vk.silka.append(i['url'])
                file_information["size"] = i['type']
        file = vk.silka[0]
        like = x['response']['items'][0]['likes']['count']
        date = x['response']['items'][0]['date']
        vk.file_info = {'file':file,
                        'like':like,
                        'date':date}


class yandex:
    name_d = []
    def __init__(self, token: str):
        self.token = token

    def check(self):
        path = "DZ_9"
        y = yadisk.YaDisk(token= self.token)
        t = vk.file_info['like']
        qq = str(t)
        r = '/' + qq + '.jpeg'
        check = y.exists(path + r)
        if  check == True:
            name = str(vk.file_info['like']) + str(vk.file_info['date'])
            yandex.name_d.append(name)

        else:
            name = vk.file_info['like']
            yandex.name_d.append(name)




    def zag(self):
        y = yadisk.YaDisk(token=self.token)
        url = vk.file_info['file']
        name = str(yandex.name_d[0]) + '.jpeg'
        path = 'DZ_9/' + name
        y.upload_url(url, path)
        file_information["file_name"] = name

fi_to = open('rr.txt', 'r')

if __name__ == '__main__':
    user_id = input('Введите id пользователя VK - ')
    token = input('Введите токен VK - ')
    stv = vk(user_id, token)
    stv._get_pho()
    yy = yandex(input('Введите токен яндекса-'))
    yy.check()
    yy.zag()
    j = json.dumps(file_information)

    print(j)













