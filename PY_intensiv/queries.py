import requests

def try_local_server(login, password):
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200


def try_local_server_protected(login, password):
    response = requests.post('http://vk.com/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200