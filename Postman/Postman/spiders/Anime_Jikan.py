# -*- coding: utf-8 -*-
import scrapy
from jikanpy import Jikan
jikan = Jikan()
import psycopg2
from local import connection
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')


class AnimeJikanSpider(scrapy.Spider):
	name = 'Anime_Jikan'
	allowed_domains = ['https://jikan.moe/']
	start_urls = ['https://jikan.moe//']

	def parse(self, response):

		eps = jikan.anime(457, extension='episodes')
		eps=eps["episodes"]
		title=[]
		ep_id=[]
		aired=[]
		recap=[]
		
		for i in range(0,len(eps)):

			ep_id.append(eps[i]['episode_id'])
			title.append(eps[i]['title'])
			aired.append(eps[i]['aired'])
			recap.append(eps[i]['recap'])

		data = zip(ep_id,title,aired,recap)

		for item in data:
			scraped_info={

				'Ep_id' : item[0],
				'Title' : item[1],
				'Aired' : item[2],
				'Recap' : item[3],
			}


			yield scraped_info



		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Anime_Jikan(Episode_id,title, Aired, Recap) VALUES (%s,%s,%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (ep_id[d], title[d], aired[d],recap[d] )
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


