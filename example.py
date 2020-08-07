import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=17d9dbba945d4b1e8b1ed978c7d41867')
response = requests.get(url)
print response.json()

