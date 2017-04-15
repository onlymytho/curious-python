# -*- coding:utf-8 -*-

import JsonHandler

# publisher	Publisher ID. Your publisher ID is "100233052087887". This is assigned when you register as a publisher.
# v	        Version. Which version of the API you wish to use. All publishers should be using version 2. Currently available versions are 1 and 2. This parameter is required.
# format	Format. Which output format of the API you wish to use. The options are "xml" and "json". If omitted or invalid, the XML format is used.
# callback	Callback. The name of a javascript function to use as a callback to which the results of the search are passed. This only applies when format=json. For security reasons, the callback name is restricted letters, numbers, and the underscore character.
# q	        Query. By default terms are ANDed. To see what is possible, use our advanced search page to perform a search and then check the url for the q value.
# l	        Location. Use a postal code or a "city, state/province/region" combination.
# sort	    Sort by relevance or date. Default is relevance.
# radius	Distance from search location ("as the crow flies"). Default is 25.
# st	    Site type. To show only jobs from job boards use "jobsite". For jobs from direct employer websites use "employer".
# jt	    Job type. Allowed values: "fulltime", "parttime", "contract", "internship", "temporary".
# start	    Start results at this result number, beginning with 0. Default is 0.
# limit	    Maximum number of results returned per query. Default is 10
# fromage	Number of days back to search.
# highlight	Setting this value to 1 will bold terms in the snippet that are also present in q. Default is 0.
# filter	Filter duplicate results. 0 turns off duplicate job filtering. Default is 1.
# latlong	If latlong=1, returns latitude and longitude information for each job result. Default is 0.
# co	    Search within country specified. Default is us See below for a complete list of supported countries.
# chnl	    Channel Name: Group API requests to a specific channel
# userip	The IP number of the end-user to whom the job results will be displayed. This field is required.
# useragent	The User-Agent (browser) of the end-user to whom the job results will be displayed. This can be obtained from the "User-Agent" HTTP request header from the end-user. This field is required.



url = 'http://api.indeed.com/ads/apisearch?publisher=100233052087887&q=java&l=austin%2C+tx&sort=&radius=&st=&jt=&start=&limit=&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2&format=json'
host = 'http://api.indeed.com/ads/apisearch?publisher=100233052087887'
search = '&q=java'
location = '&l=seoul'
sort = '&sort='
radius = '&radius='
st = '&st='
jt = '&jt='
start = '&start='
limit = '&limit='
fromage = '&fromage='
filter = '&filter='
latlong = '&latlong=1'
co = '&co=kr'
chnl = '&chnl='
userip = '&userip=1.2.3.4'
useragent = '&useragent=Mozilla/%2F4.0%28Firefox%29'
v = '&v=2'
format = '&format=json'

url = host+search+location+sort+radius+st+jt+start+limit+fromage+filter+latlong+co+latlong+co+chnl+userip+useragent+v+format

print (url)



# lists = JsonHandler.JsonHandler.URLParserJsonDict(url)
# print (lists)
