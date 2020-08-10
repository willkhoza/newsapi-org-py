# newsapi-org-py
Pull news data from newsapi.org using their API in Python. The [official website](https://newsapi.org/s/south-africa-news-api) advertises that:

> Get live top and breaking news headlines from South Africa with our JSON API.

The returned JSON file provides the status, number of articles if the status is success together with another JSON containing the article data. 

The PostgreSQL NewsAPI schema is made up of a single ```articles``` table as shown below

<img src="postgres_newsapi_DBD.svg">