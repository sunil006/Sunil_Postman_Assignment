# -*- coding: utf-8 -*-
import scrapy
import json
import psycopg2
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')
from local import connection

class FinAlphavintageSpider(scrapy.Spider):
	name = 'Fin_AlphaVintage'
	allowed_domains = ['https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=MQ9E6D71WVEG2NVG']
	start_urls = ['https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=MQ9E6D71WVEG2NVG']

	def parse(self, response):
		res=response.text
		res=json.loads(res)
		res=res["Time Series (5min)"]
		Date=[]
		_open=[]
		high=[]
		low=[]
		close=[]

		for x,y in res.items():

			Date.append(x)
			_open.append(y['1. open'])
			high.append(y['2. high'])
			low.append(y['3. low'])
			close.append(y['4. close'])

		data = zip(Date,_open,high,low,close)

		for item in data:
			scraped_info={

				'Date' : item[0],
				'Open' : item[1],
				'High' : item[2],
				'Low' : item[3],
				'Close' : item[4],
			}


			yield scraped_info

		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Fin_AlphaVintage(Date,High, Open, Low,Close) VALUES (%s,%s,%s,%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (Date[d], high[d], _open[d],low[d],close[d] )
				cursor.execute(postgres_insert_query, record_to_insert)

			connection.commit()
			count = cursor.rowcount
			print (count, "Record inserted successfully into mobile table")

		except (Exception, psycopg2.Error) as error :
			if(connection):
				print("Failed to insert record into test2 table", error)

		finally:
		    #closing database connection
			if(connection):
				cursor.close()

				print("PostgreSQL connection is closed")


