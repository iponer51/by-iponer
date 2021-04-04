
import requests
import time

while True:
    time.sleep(6)
    response = requests.get('https://nick-name.ru/nickname/id1703245/')
    if response.status_code == 200:
        print('Запрос отправлен')
    elif response.status_code == 404:
        print('Запрос небыл отправлен')
