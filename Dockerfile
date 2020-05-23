FROM python:3.7.5-slim
RUN python -m pip install \
        parse \
        realpython-reader



## Scraping
RUN pip3 install beautifulsoup4 requests 




## Scrapy
RUN pip3 install lxml Scrapy scrapyjs

RUN pip3 install psycopg2-binary
RUN pip3 install pandas
RUN pip3 install jikanpy

COPY Postman /Postman

WORKDIR /Postman




