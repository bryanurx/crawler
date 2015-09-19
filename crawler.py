import requests

url = 'http://www.rosesluxury.com/'

response = requests.get(url)

print(response.text)
