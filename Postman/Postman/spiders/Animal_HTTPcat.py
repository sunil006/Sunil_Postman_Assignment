# -*- coding: utf-8 -*-
import scrapy
import psycopg2
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')
from local import connection

class AnimalHttpcatSpider(scrapy.Spider):
	name = 'Animal_HTTPcat'
	allowed_domains = ['https://http.cat/']
	start_urls = ['https://http.cat//']

	def parse(self, response):

		para=response.css("p::text").extract()
		Img=response.css("a::attr(href)").extract()
			
		para=para[2:59]
		Img=Img[2:59]

		data=zip(para,Img)

		for item in data:
			scraped_info = {
				'Img' : item[1],
				'para' : item[0],
			}

			yield scraped_info



		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Animal_HTTPcat(Para, Image) VALUES (%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (para[d], Img[d])
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


