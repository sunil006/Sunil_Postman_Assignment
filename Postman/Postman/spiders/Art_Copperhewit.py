# -*- coding: utf-8 -*-
import scrapy
import json
import psycopg2
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')
from local import connection

class ArtCopperhewitSpider(scrapy.Spider):
	name = 'Art_Copperhewit'
	allowed_domains = ['https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.exhibitions.getList&access_token=7c5e3c5249b4a0e5181c0cae503f3f0f']
	start_urls = ['https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.exhibitions.getList&access_token=7c5e3c5249b4a0e5181c0cae503f3f0f']

	def parse(self, response):

		res=response.text
		res=json.loads(res)
		res=res["exhibitions"]
		_id=[]
		title=[]
		url=[]
		start=[]
		end=[]
		
		for i in range(0,len(res)):
			_id.append(res[i]['id'])
			title.append(res[i]['title'])
			url.append(res[i]['url'])
			start.append(res[i]['date_start'])
			end.append(res[i]['date_end'])

		data=zip(_id,title,url,start,end)

		for item in data:
			scraped_info={

				'Id' : item[0],
				'title' : item[1],
				'url' : item[2],
				'start' : item[3],
				'end' : item[4],
			}


			yield scraped_info


		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Art_Copperhewit(id,title, url, start_date,end_date) VALUES (%s,%s,%s,%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (_id[d], title[d], url[d],start[d],end[d] )
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


