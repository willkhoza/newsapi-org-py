from db import read_sql
from db import Postgres
import requests
import pandas as pd
import datetime

def get_data():
    url = ('http://newsapi.org/v2/top-headlines?'
       'country=za&'
       'apiKey=17d9dbba945d4b1e8b1ed978c7d41867')
    try:
        response = requests.get(url)
        feedback = [response.json()["status"], "Total Results:", response.json()['totalResults'], datetime.datetime.now()]
    except:
        return 0, None, ["fail", "Total Results:", 0,  datetime.datetime.now()]
    data = pd.DataFrame(response.json()["articles"])
    data['source'] = data['source'].apply(lambda info: info['name'])
    return 1, data, feedback

def upload_data(dat, conn_to):
    dat.to_sql("articles", con = conn_to, if_exists = "append", index = False, schema = "news-api")


def main():
    psql = Postgres()
    conn = psql.connect()
    status, data, log = get_data()
    if status == 1:
        upload_data(data, conn)
    log = pd.DataFrame([log])
    log.columns = ["code", "status", "total", "datetime"]
    log.drop(["status", "total"], axis=1, inplace=True)
    log.to_sql("log", con = conn, if_exists     = "append", index = False, schema = "news-api")
    conn.close()


if __name__ == "__main__":
    main()