# -*- coding: utf-8 -*-
import scrapy
import json
import psycopg2
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')
from local import connection


class AnimalCatsSpider(scrapy.Spider):
	name = 'Animal_cats'
	allowed_domains = ['https://api.thecatapi.com/v1/breeds?api_key=6d1b84f2-ddb7-4170-89bc-7fc8368fd7bc']
	start_urls = ['https://api.thecatapi.com/v1/breeds?api_key=6d1b84f2-ddb7-4170-89bc-7fc8368fd7bc/']

	def parse(self, response):
		res=response.text
		res=json.loads(res)
		
		_id =[]
		name =[]
		origin = []
		ur = []

		for i in range(0,len(res)):
			_id.append(res[i]["id"])
			name.append(res[i]["name"])
			origin.append(res[i]["origin"])
			ur.append(res[i]["affection_level"])

		data = zip(_id,name,origin,ur)

		for item in data:
			scraped_info ={
				'id' : item[0],
				'name' : item[1],
				'origin' : item[2],
				'affection_level' : item[3],
				}


			yield scraped_info




		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Animal_cats(id,name, origin, affection_level) VALUES (%s,%s,%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (_id[d], name[d], origin[d],ur[d] )
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



