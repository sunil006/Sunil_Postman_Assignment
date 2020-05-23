# Sunil_Postman_Assignment

A. Steps run code

  docker-compose run web python ./Postman/All_files.py .
  
  If your machine is Linux, you need to install docker-compose using this link : https://docs.docker.com/compose/install/

From Table I am showning top 5 rows.

B. Schema and Tables 

	table1 = Animal_cat_facts(id text,text text,type text,upvotes text)
	table2 = Animal_cats(id text,name text, origin text, affection_level text)
	table3 = Animal_HTTPcat(para text,Image text)
	table4 =  Anime_Ghibli(id text,title text, director text, producer text)
	table5 = Anime_Jikan(Episode_id text,title text, Aired text, Recap text)
	table6 =  Art_Copperhewit(id text,title text, url text, start_date text,end_date text)
	table7 =  Art_Harvardmus(id text,objevtcount text, lastupdate text, name text)
	table8 =  Envi_OpenAQ(country text,Name text, City text, Locations text,Count text)
	table9 =  Fin_AlphaVintage(Date text,High text, Open text, Low text,Close text)

	No need Recreate them. Creating tables from python script, which is present in All_files.py .

C. Points to achieve

	1. Authorization and Token expiration is done, as some API's are providing key.
	2. Pagination for some API's.
	3. Rate limiting is taken for some API's.

	Number of entries in each table depends on the API data they provide by that website.

D. Points that not achieved

	Didn't crawled all APIs.

E.
	If given more days, I would have crawled all APIs. I have created spider for every API, If there is more time I would have selected another approach for getting data which would have been easy for me.
