import requests
name = 'chris27'
url='https://api.github.com/users/{}'
r = requests.get(url.format(name)).json()
print(r)