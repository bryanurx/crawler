import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.rosesluxury.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

emails = soup.body.findAll(text=re.compile("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)", re.I))

print(emails)