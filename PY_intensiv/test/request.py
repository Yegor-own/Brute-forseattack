import requests

urls = ['https://getbootstrap.com/', #1 сайт Bootstrap
        'https://pythontutor.ru/', #2 сайт Питонтьютора
        'https://www.fit.vut.cz/', #3 сайт технического университета в Брно
        'https://www.youtube.com/', #4 сайт Youtube
        'https://web.whatsapp.com/', #5 WatsApp Web
        'https://docs.google.com/forms/d/e/1FAIpQLSd4HMIkHkGLGCBfIxJFv9iAdJdachh8HbxeO7SsRTtEakDOPw/viewform' #6 адрес формы для дз №1
        ]
print('номер сайта: номер запроса: код ответа:')
m = 0
for f in range(len(urls)):
    m += 1
    for i in range(300):
        response = requests.get(urls[f])
        print(m, i, response.status_code)
