-- Create the articles table for the data from News-API
-- Lindo Khoza

CREATE TABLE "news-api".articles (
    source text NOT NULL,
    author text,
    title text,
    description text,
    url text,
    urlToImage text,
    publishedAt text,
    content text
);

