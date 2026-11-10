# api call in python

import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)

if response.status_code == 200:
    print('data: ', response.json())
else :
    print('data not found')


