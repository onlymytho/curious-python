# -*- coding: utf-8 -*-

import requests
import json
import csv
import io
from datetime import datetime
import JsonHandler
import pprint as p
import numpy
from Slack_API_Connection import r

# auth 파일에서 airbnb_my_user_api_key 받아오기
import sys
sys.path.insert(0, "/Users/onlymytho/python")
import auth

my_user_api_key = auth.airbnb_my_user_api_key

end_point_url = 'https://api.airbnb.com/v2/search_results'

def getlistings(location, locale='ko',
                currency='USD',
                _format='for_search_results_with_minimal_pricing',
                limit='50',
                _offset='0',
                guests='2',
                ib='false',
                min_bathrooms='0',
                min_bedrooms='0',
                min_beds='1',
                min_num_pic_urls='5',
                price_max='1000',
                price_min='0',
                sort='1',
                user_lat='37.560512',
                user_lng='126.908462'):
    r = requests.get(end_point_url +
                     '?client_id='+my_user_api_key+
                     '&locale='+str(locale)+
                     '&currency='+str(currency)+
                     '&_format='+str(_format)+
                     '&_limit='+str(limit)+
                     '&_offset='+str(_offset)+
                     '&guests='+str(guests)+
                     '&ib='+str(ib)+
                     '&location='+str(location)+
                     '&min_bathrooms='+str(min_bathrooms)+
                     '&min_bedrooms='+str(min_bathrooms)+
                     '&min_beds='+str(min_beds)+
                     '&min_num_pic_urls='+str(min_num_pic_urls)+
                     '&price_max=1000'+str(price_max)+
                     '&price_min='+str(price_min)+
                     '&sort='+str(sort)+
                     '&user_lat='+str(user_lat)+
                     '&user_lng='+str(user_lng)
                     )

    print (r)

    datadict = r.json()
    datajson = json.dumps(datadict, indent=4)
    # print (datajson)
    now = datetime.now()
    with io.open('data/airbnb_listings/airbnb_listings'+' '+str(now)+'.json', 'w', encoding='utf-8') as f:
      f.write(datajson)

    listings = JsonHandler.JsonHandler.OpenJsonFileConvertToDict('data/airbnb_listings/airbnb_listings'+' '+str(now)+'.json')['search_results']
    return listings

def getneighbors(location, price_min=1, price_max=500):
    ids = []
    neighbors = []
    price_step = 4
    for price in range(price_min, price_max, price_step):
        r.start()
        listings = getlistings(location, price_max=str(price+price_step), price_min=str(price))
        for listing in listings:
            id = listing['listing'].get('id')
            if id in ids:
                pass
            else:
                ids.append(id)
                neighbors.append(listing)
                print (listing['pricing_quote']['rate'].get('amount_formatted'))
        print (str(price)+'/'+str(price_max)+' : ', r.end())
    return neighbors

class price:
    def get():
        prices = []
        for listing in listings:
            prices.append(int(listing['pricing_quote']['rate'].get('amount_formatted')[1:]))
        return prices

    def cal(dict, method):
        if method is 'sum':
            sum = 0
            for item in dict:
                sum = sum+item
            return sum
        elif method is 'avg':
            sum = 0
            for item in dict:
                sum = sum+item
            return float(sum/len(dict))
        elif method is 'med':
            return numpy.median(dict)
        elif method is 'std':
            return numpy.std(dict)
        elif method is 'min':
            return numpy.min(dict)
        elif method is 'max':
            return numpy.max(dict)

class title:
    def get():
        titles = []
        for listing in listings:
            titles.append(listing['listing'].get('name'))
        return titles

    def cal(dict, method):
        if method is 'len':
            lenth = []
            for item in dict:
                lenth.append(len(item))
            print ("SUM =" + str(numpy.sum(lenth)))
            print ("AVG =" + str(numpy.mean(lenth)))
            print ("MED =" + str(numpy.median(lenth)))
            print ("STD =" + str(numpy.std(lenth)))
            print ("MIN =" + str(numpy.min(lenth)))
            print ("MAX =" + str(numpy.max(lenth)))

class run:
    def analysis_price():
        r.start()
        print ("전체 리스팅 개수 : " + str(len(price.get())))
        print ("전체 가격 목록 : " + str(price.get()))
        print ("SUM = " + str(price.cal(price.get(), 'sum')))
        print ("AVG = " + str(price.cal(price.get(), 'avg')))
        print ("MED = " + str(price.cal(price.get(), 'med')))
        print ("STD = " + str(price.cal(price.get(), 'std')))
        print ("MIN = " + str(price.cal(price.get(), 'min')))
        print ("MAX = " + str(price.cal(price.get(), 'max')))
        r.end()
    def analysis_title():
        # print (nltitles(gettitles()))
        p.pprint (title.cal(title.get(), 'len'))


listings = getneighbors(location='Yeonnam-22-18', price_min=1, price_max=1000)

# run.analysis_title()
run.analysis_price()
