from db import read_sql
from db import Postgres
import requests
import pandas as pd
import datetime

def get_data():
    
    url = ('https://gnews.io/api/v3/'
        'top-news?'
        'country=za&'
        'token=6726f404d83418548d0d6795159943c0')
    try:
        response = requests.get(url)
        feedback = [response.json()["timestamp"], "Total Results:", response.json()['articleCount'], datetime.datetime.now()]
    except:
        return 0, None, ["fail", "Total Results:", 0,  datetime.datetime.now()]
    data = pd.DataFrame(response.json()["articles"])
    data['source'] = data['source'].apply(lambda info: info['name'])
    return 1, data, feedback

def upload_data(dat, conn_to):
    dat.to_sql("gnews", con = conn_to, if_exists = "append", index = False, schema = "news-api")


def main():
    psql = Postgres()
    conn = psql.connect()
    status, data, log = get_data()
    if status == 1:
        upload_data(data, conn)
    log = pd.DataFrame([log])
    log.columns = ["code", "status", "total", "datetime"]
    log.drop(["status", "total"], axis=1, inplace=True)
    log.to_sql("gnews_log", con = conn, if_exists     = "append", index = False, schema = "news-api")
    conn.close()


if __name__ == "__main__":
    main()