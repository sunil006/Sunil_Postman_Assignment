# -*- coding: utf-8 -*-
import scrapy
import json
import psycopg2
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')
from local import connection

class AnimeGhibliSpider(scrapy.Spider):
	name = 'Anime_Ghibli'
	allowed_domains = ['https://ghibliapi.herokuapp.com/films']
	start_urls = ['https://ghibliapi.herokuapp.com/films/']

	def parse(self, response):
		res=response.text
		res=json.loads(res)
		_id=[]
		title=[]
		director=[]
		producer=[]
		
		for i in range(0,len(res)):
			_id.append(res[i]['id'])
			title.append(res[i]['title'])
			director.append(res[i]['director'])
			producer.append(res[i]['producer'])


		data = zip(_id,title,director,producer)

		for item in data:
			scraped_info={

				'Id' : item[0],
				'Title' : item[1],
				'Director' : item[2],
				'Producer' : item[3],
			}


			yield scraped_info


		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Anime_Ghibli(id,title, director, producer) VALUES (%s,%s,%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (_id[d], title[d], director[d],producer[d] )
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


