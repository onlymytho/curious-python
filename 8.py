from bs4 import BeautifulSoup
import urllib.request
import html5lib
from datetime import datetime

HOST = 'https://www.airbnb.co.kr/rooms/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
       }

room_id = []
listing_names = []


def run() :
    a = datetime.now()
    for i in range(1135580, 1135584):
        request = urllib.request.Request(HOST+str(i),None,headers) #The assembled request
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
    print (str(room_id) + "," + str(listing_names))
    b = datetime.now()
    c = b - a
    print(c)
run()
