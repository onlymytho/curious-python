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

room_id = []
listing_names = []
rooms = []

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


        print ("\n* Room_id = "+str(i)+ "\nOriginal listing_name :" + str(listing_name))

        if listing_name == None:
            null = 'null'
            listing_names.append(null)
            print ("Listing_name = "+ str(null) + "\n---------------------------\n")
        else:
            listing_names.append(listing_name.string)
            print ("Listing_name = "+ str(listing_name.string) + "\n---------------------------\n")

        room_id.append(i)

        rooms.append([room_id[n], listing_names[n]])
        csvWriter.writerow(rooms[n])
        n = n+1

    print (str(room_id) + "," + str(listing_names))
    b = datetime.now()
    c = b - a
    print(c)

    f.close()


run()
