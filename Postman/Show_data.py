import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
from local import connection
def Data_from_tables():
	#connection = pg.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')

	table1    = pd.read_sql('select * from Animal_cat_facts LIMIT 5', connection)
	table2    = pd.read_sql('select * from Animal_cats LIMIT 5', connection)
	table3    = pd.read_sql('select * from Animal_HTTPcat LIMIT 5', connection)
	table4    = pd.read_sql('select * from Anime_Ghibli LIMIT 5', connection)
	table5    = pd.read_sql('select * from Anime_Jikan LIMIT 5', connection)
	table6    = pd.read_sql('select * from Art_Copperhewit LIMIT 5', connection)
	table7    = pd.read_sql('select * from Art_Harvardmus LIMIT 5', connection)
	table8    = pd.read_sql('select * from Envi_OpenAQ LIMIT 5', connection)
	table9    = pd.read_sql('select * from Fin_AlphaVintage LIMIT 5', connection)

	print("Table 1\n")
	print(table1)
	print("Table 2\n")
	print(table2)
	print("Table 3\n")
	print(table3)
	print("Table 4\n")
	print(table4)
	print("Table 5\n")
	print(table5)
	print("Table 6\n")
	print(table6)
	print("Table 7\n")
	print(table7)
	print("Table 8\n")
	print(table8)
	print("Table 9\n")
	print(table9)


