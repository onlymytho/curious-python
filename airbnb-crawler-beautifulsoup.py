# 1898570 방에서 400에러 뜨는 거 잡기
# 방이 존재하는 범위로 돌렸는데, 가끔씩 데이터를 못 불러오는 경우에 대해 해결하기.
# csv export까지 하는 프로그램으로 제작하기

from bs4 import BeautifulSoup
import urllib.request
import html5lib
from datetime import datetime
import time
import csv
HOST = 'https://www.airbnb.co.kr/rooms/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
       }


rooms = []

room_id = []
listing_names = []
review_counts = []

range_from = 1135581
range_to = 1135584


def run() :
    n = 0

    a = datetime.now()
    f = open('airbnb_listings/airbnb_listings '+' '+str(datetime.now())+'.csv','w', newline='')
    csvWriter = csv.writer(f)

    for i in range(range_from, range_to):
        request = urllib.request.Request(HOST+str(i),None,headers) #The assembled request
        time.sleep(2)
        data = urllib.request.urlopen(request).read()

        soup = BeautifulSoup(data, 'lxml')
        body = soup.find('body')
        listing_name = body.find('div', id='listing_name')
        review_count = body.find_all('div', string="후기")
        #일단 None 문제를 떠나서... 반드시 reactid=60 에 후기가 있지 않았다... `후기`라는 단어가 들어간 태그를 찾는 방식으로 바꿔야 할 듯
        if review_count != None:
            review_count = review_count[0].string[3:6]
        else:
            review_count = 'null'
        print (review_count)
        print ("\n* Room_id = "+str(i)+ "\nOriginal listing_name :" + str(listing_name))

        # Append room_id
        room_id.append(i)

        # Append listing_names
        if listing_name == None:
            null = 'null'
            listing_names.append(null)
            print ("Listing_name = "+ str(null))
        else:
            listing_names.append(listing_name.string)
            print ("Listing_name = "+ str(listing_name.string))

        # Append review_count
        review_counts.append(review_count)
        print ("review_count = "+ str(review_count) + "\n---------------------------\n")

        rooms.append([room_id[n], listing_names[n], review_counts[n]])
        csvWriter.writerow(rooms[n])
        n = n+1

    print (str(room_id) + "," + str(listing_names))
    b = datetime.now()
    c = b - a
    print(c)

    f.close()


run()
