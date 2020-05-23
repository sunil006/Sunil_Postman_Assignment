# -*- coding: utf-8 -*-
import scrapy
import json
import psycopg2
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')
from local import connection


class ArtHarvardmusSpider(scrapy.Spider):
	name = 'Art_Harvardmus'
	allowed_domains = ['https://api.harvardartmuseums.org/culture?apikey=9e4e2160-9ab5-11ea-9caa-375ebb1e00b2']
	start_urls = ['https://api.harvardartmuseums.org/culture?apikey=9e4e2160-9ab5-11ea-9caa-375ebb1e00b2/']

	def parse(self, response):

		res=response.text
		res=json.loads(res)
		res=res["records"]
		_id=[]
		objectcount=[]
		lastupdate=[]
		name=[]
		
		
		for i in range(0,len(res)):
			_id.append(res[i]['id'])
			objectcount.append(res[i]['objectcount'])
			lastupdate.append(res[i]['lastupdate'])
			name.append(res[i]['name'])
			
		data=zip(_id,objectcount,lastupdate,name)

		for item in data:
			scraped_info={

				'Id' : item[0],
				'objectcount' : item[1],
				'lastupdate' : item[2],
				'name' : item[3],
			}


			yield scraped_info




		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Art_Harvardmus(id,objevtcount, lastupdate, name) VALUES (%s,%s,%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (_id[d], objectcount[d], lastupdate[d],name[d] )
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



