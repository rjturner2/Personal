import requests

user_content = input("What topic would you like a definition for?: ")
user_content = user_content.strip().split(" ")
user_content = [name.capitalize() for name in user_content]

URL = "https://en.wikipedia.org/wiki/"

for name in user_content:
	URL += name
	if user_content.index(name) + 1 < len(user_content):
		URL += "_"

response = requests.get(URL)

print(response.json())