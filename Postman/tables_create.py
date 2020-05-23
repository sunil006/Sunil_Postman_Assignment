import psycopg2
from local import connection
def create_tables():

	#connection = psycopg2.connect(user='sunil',password='Sunil@1913',host='localhost',port="5432",database='postman')

	cursor = connection.cursor()


	#db= '''CREATE database sunilkumar''';

	#cursor.execute(db)
	cursor.execute("DROP TABLE IF EXISTS Animal_cat_facts")
	cursor.execute("DROP TABLE IF EXISTS Animal_cats")
	cursor.execute("DROP TABLE IF EXISTS Animal_HTTPcat")
	cursor.execute("DROP TABLE IF EXISTS Anime_Ghibli")
	cursor.execute("DROP TABLE IF EXISTS Anime_Jikan")
	cursor.execute("DROP TABLE IF EXISTS Art_Copperhewit")
	cursor.execute("DROP TABLE IF EXISTS Art_Harvardmus")
	cursor.execute("DROP TABLE IF EXISTS Envi_OpenAQ")
	cursor.execute("DROP TABLE IF EXISTS Fin_AlphaVintage")
	connection.commit()

	table1 = '''CREATE TABLE Animal_cat_facts(id text,text text,type text,upvotes text)'''
	cursor.execute(table1)


	table2 = '''CREATE TABLE Animal_cats(id text,name text, origin text, affection_level text)'''
	cursor.execute(table2)

	table3 = '''CREATE TABLE Animal_HTTPcat(para text,Image text)'''
	cursor.execute(table3)

	table4 = '''CREATE TABLE Anime_Ghibli(id text,title text, director text, producer text)'''
	cursor.execute(table4)


	table5 = '''CREATE TABLE Anime_Jikan(Episode_id text,title text, Aired text, Recap text)'''
	cursor.execute(table5)

	table6 = '''CREATE TABLE Art_Copperhewit(id text,title text, url text, start_date text,end_date text)'''
	cursor.execute(table6)

	table7 = '''CREATE TABLE Art_Harvardmus(id text,objevtcount text, lastupdate text, name text)'''
	cursor.execute(table7)

	table8 = '''CREATE TABLE Envi_OpenAQ(country text,Name text, City text, Locations text,Count text)'''
	cursor.execute(table8)

	table9 = '''CREATE TABLE Fin_AlphaVintage(Date text,High text, Open text, Low text,Close text)'''
	cursor.execute(table9)

	print("All Tables created successfully!!!")

	connection.commit()
	



