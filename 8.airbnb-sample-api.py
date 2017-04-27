# -*- coding: utf-8 -*-

import requests
import json
import csv
import io
from datetime import datetime
import JsonHandler
import pprint as p
import numpy
import Record as r

# auth 파일에서 airbnb_my_user_api_key 받아오기
import sys
sys.path.insert(0, "/Users/onlymytho/python")
import auth

my_user_api_key = auth.airbnb_my_user_api_key

end_point_url = 'https://api.airbnb.com/v2/search_results'

class get_listing:
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
            listings = get_listing.getlistings(location, price_max=str(price+price_step), price_min=str(price))
            for l in listings:
                id = l['listing'].get('id')
                if id in ids:
                    pass
                else:
                    ids.append(id)
                    neighbors.append(l)
                    print (l['pricing_quote']['rate'].get('amount_formatted'))
            r.end()
            print (str(price)+'/'+str(price_max))

        return neighbors

class price:
    def get():
        prices = []
        for l in listings:
            prices.append(int(l['pricing_quote']['rate'].get('amount_formatted')[1:]))
        return prices

class title:
    def get():
        titles = []
        for l in listings:
            titles.append(l['listing'].get('name'))
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

class room_type:
    def get():
        room_type = {}
        room_type['entire_home'] = []
        room_type['private_room'] = []
        room_type['else'] = []
        for l in listings:
            rt = l['listing'].get('room_type_category')
            if rt == 'entire_home':
                room_type['entire_home'].append(rt)
            elif rt == 'private_room':
                room_type['private_room'].append(rt)
            else:
                room_type['else'].append(rt)
        return room_type

    def getprice(room_type_param=None):
        room_type = {}
        room_type['entire_home'] = []
        room_type['private_room'] = []
        room_type['else'] = []

        for l in listings:
            rt = l['listing'].get('room_type_category')
            if rt == 'entire_home':
                room_type['entire_home'].append(l)
            elif rt == 'private_room':
                room_type['private_room'].append(l)
            else:
                room_type['else'].append(l)

        prices = {}
        prices['entire_home'] = []
        prices['private_room'] = []
        prices['else'] = []
        for rt in room_type:
            for l in room_type[rt]:
                prices[rt].append(int(l['pricing_quote']['rate'].get('amount_formatted')[1:]))

        if room_type_param is 'entire_home':
            return prices['entire_home']
        elif room_type_param is 'private_room':
            return prices['private_room']
        elif room_type_param is 'else':
            return prices['else']
        else:
            return prices

class super_host:
    def get():
        super_host = []
        for l in listings:
            sh = (l['listing']['primary_host'].get('is_superhost'))
            if sh:
                super_host.append(sh)
            elif not sh:
                pass
        return super_host

class business_travel:
    # is_business_travel_ready을 활용해서 비즈니스 여행객들을 받기에 경쟁력이 있는 지역인지?

class family_preferred:
    # is_family_preferred을 활용해서 비즈니스 여행객들을 받기에 경쟁력이 있는 지역인지?

class cal:
    def sum(dict):
        sum = 0
        for item in dict:
            sum = sum+float(item)
        return sum
    def avg(dict):
        sum = 0
        for item in dict:
            sum = sum+float(item)
        return float(sum/len(dict))
    def med(dict):
        return numpy.median(dict)
    def std(dict):
        return numpy.std(dict)
    def min(dict):
        return numpy.min(dict)
    def max(dict):
        return numpy.max(dict)

class run:
    def analysis_price():
        print ('\n=== PRICE ANALYSIS ===')
        print ("전체 리스팅 개수 : " + str(len(price.get())))
        # print ("전체 가격 목록 : " + str(price.get()))
        print ("AVG = " + str(cal.avg(price.get())))
        print ("MED = " + str(cal.med(price.get())))
        print ("STD = " + str(cal.std(price.get())))
        print ("MIN = " + str(cal.min(price.get())))
        print ("MAX = " + str(cal.max(price.get())))

    def analysis_title():
        # print (nltitles(gettitles()))
        p.pprint (title.cal(title.get(), 'len'))

    def analysis_room_type():
        print ('\n=== ROOM_TYPE ANALYSIS ===')
        print ('entire_home : ' + str(len(room_type.get()['entire_home'])))
        print ('가격 통계')
        print ('\tAVG = ' + str(cal.avg(room_type.getprice(room_type_param='entire_home'))))
        print ('\tMED = ' + str(cal.med(room_type.getprice(room_type_param='entire_home'))))
        print ('\tSTD = ' + str(cal.std(room_type.getprice(room_type_param='entire_home'))))
        print ('\tMIN = ' + str(cal.min(room_type.getprice(room_type_param='entire_home'))))
        print ('\tMAX = ' + str(cal.max(room_type.getprice(room_type_param='entire_home'))))

        print ('private_room : ' + str(len(room_type.get()['private_room'])))
        print ('가격 통계')
        print ('\tAVG = ' + str(cal.avg(room_type.getprice(room_type_param='private_room'))))
        print ('\tMED = ' + str(cal.med(room_type.getprice(room_type_param='private_room'))))
        print ('\tSTD = ' + str(cal.std(room_type.getprice(room_type_param='private_room'))))
        print ('\tMIN = ' + str(cal.min(room_type.getprice(room_type_param='private_room'))))
        print ('\tMAX = ' + str(cal.max(room_type.getprice(room_type_param='private_room'))))

        print ('else : ' + str(len(room_type.get()['else'])))
        print ('가격 통계')
        print ('\tAVG = ' + str(cal.avg(room_type.getprice(room_type_param='else'))))
        print ('\tMED = ' + str(cal.med(room_type.getprice(room_type_param='else'))))
        print ('\tSTD = ' + str(cal.std(room_type.getprice(room_type_param='else'))))
        print ('\tMIN = ' + str(cal.min(room_type.getprice(room_type_param='else'))))
        print ('\tMAX = ' + str(cal.max(room_type.getprice(room_type_param='else'))))


    def analysis_super_host():
        print ('\n== STAR_RATING ANALYSIS ===')
        print ("슈퍼호스트 수 : " + str(len(super_host.get())))
        print ("슈퍼호스트 비율 : " + str(len(super_host.get())/len(price.get())*100) + '%')



listings = get_listing.getneighbors(location='16-7, Seongmisan-ro 3na-gil, Seoul', price_min=1, price_max=200)
# Yeonnam-22
# 16-7, Seongmisan-ro 3na-gil, Seoul

# run.analysis_title()
# run.analysis_price()
run.analysis_price()
run.analysis_room_type()
run.analysis_super_host()
