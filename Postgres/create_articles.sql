-- Create the articles table for the data from News-API
-- Lindo Khoza

-- Table: news-api.articles

-- DROP TABLE "news-api".articles;

CREATE TABLE "news-api".articles
(
    "False" bigint,
    source text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default",
    title text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    url text COLLATE pg_catalog."default",
    "urlToImage" text COLLATE pg_catalog."default",
    "publishedAt" text COLLATE pg_catalog."default",
    content text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE "news-api".articles
    OWNER to postgres;
-- Index: ix_news-api_articles_False

-- DROP INDEX "news-api"."ix_news-api_articles_False";

CREATE INDEX "ix_news-api_articles_False"
    ON "news-api".articles USING btree
    ("False" ASC NULLS LAST)
    TABLESPACE pg_default;
