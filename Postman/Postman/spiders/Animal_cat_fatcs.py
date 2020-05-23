# -*- coding: utf-8 -*-
import scrapy
import json
import psycopg2
from local import connection
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='172.18.0.2',port="5432",database='postman')

class AnimalCatFatcsSpider(scrapy.Spider):
	name = 'Animal_cat_fatcs'
	allowed_domains = ['https://cat-fact.herokuapp.com/facts']
	start_urls = ['https://cat-fact.herokuapp.com/facts/']

	def parse(self, response):

		res=response.text
		res=json.loads(res)
		s=res["all"]
		_id=[]
		text=[]
		_type=[]
		upvotes=[]

		for i in range(0,len(s)):
			_id.append(s[i]['_id'])
			text.append(s[i]['text'])
			_type.append(s[i]['type'])
			upvotes.append(s[i]['upvotes'])

		data = zip(_id,text,_type,upvotes)

		for item in data:
			scraped_info = {
				'id' : item[0],
				'text' : item[1],
				'type' : item[2],
				'upvotes' : item[3],
			}

			yield scraped_info


		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Animal_cat_facts(id,text, type, upvotes) VALUES (%s,%s,%s,%s)"""
			for d in range(0,len(s)):
				record_to_insert = (_id[d], text[d], _type[d],upvotes[d] )
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



