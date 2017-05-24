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
from collections import Counter
from threading import Thread
from geopy.distance import vincenty


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
                         '&price_max='+str(price_max)+
                         '&price_min='+str(price_min)+
                         '&sort='+str(sort)+
                         '&user_lat='+str(user_lat)+
                         '&user_lng='+str(user_lng)
                         )

        print (r)

        datadict = r.json()
        datajson = json.dumps(datadict, indent=4)
        # print (datajson)
        # now = datetime.now()
        # with io.open('data/airbnb_listings/airbnb_listings'+' '+str(now)+'.json', 'w', encoding='utf-8') as f:
        #   f.write(datajson)
        #
        # listings = JsonHandler.JsonHandler.OpenJsonFileConvertToDict('data/airbnb_listings/airbnb_listings'+' '+str(now)+'.json')['search_results']
        listings = datadict['search_results']
        return listings

    def getneighbors(location, price_min=1, price_max=500, price_step=4):
        ids = []
        neighbors = []
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
            print (len(neighbors))
                    # print (l['pricing_quote']['rate'].get('amount_formatted'))
            r.end()
            r.end('main_record')
            # print (str(price)+'/'+str(price_max))

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
    # is_business_travel_ready을 활용해서 비즈니스 여행객들을 받기에 경쟁력이 있는 지역인지
    def get():
        business_travel = []
        for l in listings:
            bt = (l['listing'].get('is_business_travel_ready'))
            if bt:
                business_travel.append(bt)
            elif not bt:
                pass
        return business_travel

class family_preferred:
    # is_family_preferred을 활용해서 가족 여행객들을 받기에 경쟁력이 있는 지역인지
    def get():
        family_preferred = []
        for l in listings:
            fp = (l['listing'].get('is_family_preferred'))
            if fp:
                family_preferred.append(fp)
            elif not fp:
                pass
        return family_preferred

class language:
    # extra_host_languages를 받아와서, 어떤 언어의 사용이 경쟁력 있는지 알려줌
    def get():
        extra_host_languages = []
        for l in listings:
            fp = (l['listing'].get('extra_host_languages'))
            for lang in fp:
                extra_host_languages.append(lang)
        return extra_host_languages

class location:
    locations = {}
    diff = []
    my_locations = {}

    def my():
        global locations
        global my_locations
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+search_location)
        rjson = r.json()
        locations = {}
        my_locations = rjson['results'][0]['geometry']['location']

    def get():
        global locations
        for l in listings:
            id = (l['listing'].get('id'))
            lat = (l['listing'].get('lat'))
            lng = (l['listing'].get('lng'))
            locations[str(id)] = {'lat':lat, 'lng':lng}

    def diff():
        global locations
        global diff
        global my_locations
        diff = []
        my_locations = (my_locations['lat'], my_locations['lng'])
        for loc in locations.values():
            loc = (loc['lat'], loc['lng'])
            d = vincenty(my_locations, loc).meters
            diff.append(d)

    def closer(distance):
        global diff
        closer = []
        for d in diff:
            if d < distance:
                closer.append(d)
            else:
                pass
        return closer

    def exec_closer(distance):
        location.my()
        location.get()
        location.diff()
        closer = location.closer(distance)
        return closer


class cal:
    '''연산 클래스. 다른 함수들을 위한 연산에 사용'''
    def sum(dict):
        sum = 0
        for item in dict:
            sum = sum+float(item)
        return sum
    def avg(dict):
        sum = 0
        for item in dict:
            sum = sum+float(item)
        if len(dict) != 0:
            return float(sum/len(dict))
        else:
            return 0
    def med(dict):
        if len(dict) != 0:
            return numpy.median(dict)
        else:
            return 0
    def std(dict):
        if len(dict) != 0:
            return numpy.std(dict)
        else:
            return 0
    def min(dict):
        if len(dict) != 0:
            return numpy.min(dict)
        else:
            return 0
    def max(dict):
        if len(dict) != 0:
            return numpy.max(dict)
        else:
            return 0

class run:
    '''실행만 하면 저절로 돌아가는 run함수들을 모아놓은 클래스. 뭘 해야할지 모르거나, 원하는 것이 있다면 돌려보면 된다.'''
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
        print ('\n=== STAR_RATING ANALYSIS ===')
        print ("슈퍼호스트 수 : " + str(len(super_host.get())))
        print ("슈퍼호스트 비율 : " + str(round(len(super_host.get())/len(price.get())*100, 1)) + '%')

    def analysis_business_travel():
        print ('\n=== BUSINESS_TRAVEL ANALYSIS ===')
        print ("비즈니스 여행객을 위한 리스팅 수 : " + str(len(business_travel.get())))
        print ("비즈니스 여행객을 위한 리스팅 비율 : " + str(round(len(business_travel.get())/len(price.get())*100, 1)) + '%')

    def analysis_family_preferred():
        print ('\n=== FAMILY_PREFERRED ANALYSIS ===')
        print ("가족 여행객을 선호하는 리스팅 수 : " + str(len(family_preferred.get())))
        print ("가족 여행객을 선호하는 리스팅 비율 : " + str(round(len(family_preferred.get())/len(price.get())*100, 1)) + '%')

    def analysis_extra_host_languages():
        print ('\n=== EXTRA_HOST_LANGUAGES ANALYSIS ===')
        print ("호스트 언어 : ")
        keys = list(Counter(language.get()).keys())
        values = list(Counter(language.get()).values())
        for num in range(0, len(keys)):
            print ('\t' + str(keys[num]) + ' : ' + str(values[num]) + ' (' + str(round((values[num]/len(price.get()))*100, 1)) + '%)')

    def analysis_location():
        print ('\n=== LISTINGS_LOCATION ANALYSIS ===')
        print ("10m 이내의 리스팅 개수 : " + str(len(location.exec_closer(10))))
        print ("20m 이내의 리스팅 개수 : " + str(len(location.exec_closer(20))))
        print ("50m 이내의 리스팅 개수 : " + str(len(location.exec_closer(50))))
        print ("100m 이내의 리스팅 개수 : " + str(len(location.exec_closer(100))))
        print ("200m 이내의 리스팅 개수 : " + str(len(location.exec_closer(200))))
        print ("500m 이내의 리스팅 개수 : " + str(len(location.exec_closer(500))))
        print ("1km 이내의 리스팅 개수 : " + str(len(location.exec_closer(1000))))
        print ("1.5km 이내의 리스팅 개수 : " + str(len(location.exec_closer(1500))))
        print ("2km 이내의 리스팅 개수 : " + str(len(location.exec_closer(2000))))
        print ("3km 이내의 리스팅 개수 : " + str(len(location.exec_closer(3000))))
        print ("5km 이내의 리스팅 개수 : " + str(len(location.exec_closer(5000))))
        print ("10km 이내의 리스팅 개수 : " + str(len(location.exec_closer(10000))))
        print ("50km 이내의 리스팅 개수 : " + str(len(location.exec_closer(50000))))




if __name__ == '__main__':
    print ("*** Before Airbnb **********\n주변 에어비엔비를 분석해서 당신의 에어비엔비가 경쟁력을 가질 수 있는지 알려드립니다.")
    search_location = input("검색할 주소를 입력해주세요 : ")

    r.start('main_record')
    incremental_search = {'price_min': [1,3,6,9,12,15,18,21,24,27,30,60,120,210,330,480],
                          'price_max': [3,6,9,12,15,18,21,24,27,30,60,120,210,330,480,1000],
                          'price_step':[1,1,1,1,1,1,1,1,1,1,10,20,30,40,50,100]
                          }

    # -- INCREMENTAL_SEARCH ACCURACY & SPEED TEST --
    #
    # *** TEST *****
    # price_ranges                                                          / price_steps                           : listing_count / processing_time
    # [TEST #A-1] 1,10,200,300,1000                                         / 1,10,30,50                            : 185개 / 75초,
    # [TEST #A-2] 1,20,300,1000                                             / 1,30,100                              : 168개 / 59초,
    # [TEST #A-3] 1,20,200,300,1000                                         / 1,10,30,100                           : 186개 / 85초,
    # [TEST #A-4] 1,5,20,200,300,1000                                       / 1,2,10,30,100                         : 237개 / 64초,
    # [TEST #A-5] 1,5,20,100,200,300,1000                                   / 1,2,10,20,50,100                      : 257개 / 64초,
    # [TEST #A-6] 1,5,20,100,200,300,1000                                   / 1,2,10,20,30,100                      : 254개 / 74초,
    # [TEST #B-1] 1,5,10,20,50,100,200,500,1000                             / 1,1,2,5,10,20,60,100                  : 354개 / 11초,
    # [TEST #B-2] 구간 12개 : 1,5,10,15,20,25,35,50,100,200,500,1000                    / 1,1,1,1,1,2,5,10,20,60,100            : 508개 / 10초,
    # [TEST #B-3] 구간 14개 : 1,5,10,15,20,25,30,35,40,50,100,200,500,1000              / 1,1,1,1,1,1,1,2,5,10,20,60,100        : 618개 / 10초,
    # [TEST #B-4] 구간 16개 : 1,5,10,15,20,25,30,35,40,45,50,100,200,350,500,1000       / 1,1,1,1,1,1,1,1,1,1,10,20,30,30,100   : 686개 / 10초
    # [TEST #B-5] 구간 17개 : 1,3,6,9,12,15,18,21,24,27,30,60,120,210,330,480,1000       / 1,1,1,1,1,1,1,1,1,1,1,10,20,30,40,50,100   : 864개 / 12초 (거리 계산하는데 시간이 좀 걸렸음)
    #
    # *** RESULT *****
    # A
    # [TEST #A-5]의 성적이 가장 좋았음. 정확도가 가장 좋았기 때문
    # processing_time은 인터넷 상태에 따라 계속 달라지는 경향이 있어서, 판단 기준으로 삼기 힘드므로 결과 해석에 대한 정성적인 판단이 필요함.
    # B
    #
    #
    # *** COMMENT *****
    # incremental_search를 도입하기 전, 아래와 같이 한 가지 검색으로만 돌렸을 때는 약 5분 이상 걸렸었음.
    # listings = get_listing.getneighbors(location='연남로 22길', price_min=1, price_max=1000, price_step=4)
    # TEST #A는 쓰레드 적용 전.
    # TEST #B는 쓰레드 적용 후.
    # -- END --

    listings = []
    threads = []
    for n in range(len(incremental_search['price_min'])):
        def getlistingthread():
            global listings
            global search_location
            l = get_listing.getneighbors(
                location=search_location,
                price_min=incremental_search['price_min'][n],
                price_max=incremental_search['price_max'][n],
                price_step=incremental_search['price_step'][n])
            listings = listings + l

        threads.append(Thread(target=getlistingthread))
        threads[n].daemon = True
        threads[n].start()

    for n in range(len(incremental_search['price_min'])):
        threads[n].join()
    # Thread TEST
    # incremental_search의 각 구간들을 활용해서 여러 쓰레드로 돌림.
    # 결과 : 위 [TEST #5]형태로 돌린 결과, '246개 / 17초' 로 완료. 즉, 약 70%이상의 시간 단축. (처음에 비해 95%시간 단축 = 20배 속도 증가)

    # 연남로 3길 22-18
    # 16-7, Seongmisan-ro 3na-gil, Seoul


    # run.analysis_title()
    # run.analysis_price()

    run.analysis_price()
    run.analysis_room_type()
    run.analysis_super_host()
    run.analysis_business_travel()
    run.analysis_family_preferred()
    run.analysis_extra_host_languages()
    run.analysis_location()
    r.end('main_record')
