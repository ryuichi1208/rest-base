from urllib import request
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080


def call_http_request(req):
    try:
        with request.urlopen(req) as response:
            print(response.code, response.reason)
            print(response.headers)
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e.code, e.reason)
        print(e.read().decode('utf-8'))


def call_list_user(limit=10, offset=0):
    url = 'http://%s:%s/api/users?limit=%d&offset=%d' % (SERVER_HOST, SERVER_PORT, limit, offset)
    call_http_request(url)


def call_post_user(name, age):
    payload = {
        'name': name,
        'age': age
    }
    data = json.dumps(payload).encode('utf-8')

    url = 'http://%s:%s/api/users' % (SERVER_HOST, SERVER_PORT)
    headers = {'Content-Type': 'application/json'}
    req = request.Request(url, data=data, method='POST', headers=headers)
    call_http_request(req)


def call_get_user(id):
    url = 'http://%s:%s/api/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    call_http_request(url)


def call_put_user(id, name, age):
    payload = {
        'name': name,
        'age': age
    }
    data = json.dumps(payload).encode('utf-8')

    url = 'http://%s:%s/api/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    headers = {'Content-Type': 'application/json'}
    req = request.Request(url, data=data, method='PUT', headers=headers)
    call_http_request(req)


def call_delete_user(id):
    url = 'http://%s:%s/api/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    req = request.Request(url, method='DELETE')
    call_http_request(req)
