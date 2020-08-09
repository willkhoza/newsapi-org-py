from db import read_sql
from db import Postgres
import requests
import pandas as pd

def get_data():
    url = ('http://newsapi.org/v2/top-headlines?'
       'country=za&'
       'apiKey=17d9dbba945d4b1e8b1ed978c7d41867')
    response = requests.get(url)
    print(response.json()["status"], "\nTotal Results:", response.json()['totalResults'])
    data = pd.DataFrame(response.json()["articles"])
    data['source'] = data['source'].apply(lambda info: info['name'])
    return data

def upload_data(dat, conn_to):
    dat.to_sql("articles", con = conn_to, if_exists = "replace", index = "False", schema = "news-api")

if __name__ == "__main__":
    psql = Postgres()
    conn = psql.connect()
    data = get_data()
    upload_data(data, conn)