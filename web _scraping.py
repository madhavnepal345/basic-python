import requests

search = input("what do you want search ?#>>> ")
url = "https://en.wikipedia.org/wiki/"

url = url + search
print("retrieving data from sources. ",url)

response = requests.get(url)
print(response.text)