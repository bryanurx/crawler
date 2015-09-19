import requests
import re
import sys
from bs4 import BeautifulSoup

cmdline = sys.argv[1]

response = requests.get(cmdline)

soup = BeautifulSoup(response.text, "html.parser")

emails = soup.body.findAll(text=re.compile("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)", re.I))

print(emails)
