# -*- coding: utf-8 -*-
import scrapy
import json
import psycopg2
#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')
from local import connection

class EnviOpenaqSpider(scrapy.Spider):
	name = 'Envi_OpenAQ'
	allowed_domains = ['https://api.openaq.org/v1/cities']
	start_urls = ['https://api.openaq.org/v1/cities/']
	
	def parse(self, response):
		res=response.text
		res=json.loads(res)
		res=res["results"]
		country=[]
		name=[]
		city=[]
		locations=[]
		count=[]

		for i in range(0,len(res)):
			country.append(res[i]['country'])
			name.append(res[i]['name'])
			city.append(res[i]['city'])
			locations.append(res[i]['locations'])
			count.append(res[i]['count'])
		data = zip(country,name,city,locations,count)

		for item in data:
			scraped_info={

				'country' : item[0],
				'Name' : item[1],
				'City' : item[2],
				'Locations' : item[3],
				'Count' : item[4],	
		}


			yield scraped_info



		try:
			
			cursor = connection.cursor()
			postgres_insert_query = """ INSERT INTO Envi_OpenAQ(country,Name, City, Locations,Count) VALUES (%s,%s,%s,%s,%s)"""
			for d in range(0,len(res)):
				record_to_insert = (country[d], name[d], city[d],locations[d],count[d] )
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


