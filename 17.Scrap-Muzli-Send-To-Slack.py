# -*- coding:utf-8 -*-
from slacker import Slacker
from datetime import datetime
import urllib
import time
import JsonHandler

# auth 파일에서 slack_app_token 받아오기
import sys
sys.path.insert(0, "/Users/onlymytho/python")
import auth

slack_token = auth.slack_app_token


def scrap():
    HOST = 'https://api.muz.li/v1/feed/muzli'

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'}


    # Access to url
    print ("Scrapping is started.")
    request = urllib.request.Request(HOST,None,headers) #The assembled request
    data = urllib.request.urlopen(request).read()


    # Parse JSON
    d = JsonHandler.JsonHandler.URLParserJsonDict(url=HOST)
    print ("Calling is finished.")


    # Declare post attribute lists
    title = []
    link = []
    image = []
    virality = []
    clicks = []
    feed = JsonHandler.JsonHandler(d).getValue('feed')


    # Select posts virality is high
    print ("Selecting viraled posts...")

    feed_selected = []

    for i in feed:
        if i['virality'] > 5000 :
            feed_selected.append(i)
        else:
            continue
    print (str(len(feed_selected)) + "posts are selected!")


    # Send to slack
    print ("Ready to send to Slack")
    slack = Slacker(slack_token)

    # Send to slack : 각 요소들에 데이터를 연결
    attachments_dict = dict()
    num = 0
    for i in feed_selected :
        attachments_dict['pretext'] = "This post is *" + str(i['clicks']) +"* clicked and *" + str(i['virality']) +"* viraled"
        attachments_dict['title'] = i['title']
        attachments_dict['title_link'] = i['link']
        attachments_dict['fallback'] = i['title']
        attachments_dict['image_url']= i['image']
#        attachments_dict['text'] = "브라우저에서 웹서버로 패킷 전송 전, 데이터가 하드디스크에 평문 저장되고 있어 이번 취약성 이용한다면 대량의 계정탈취와 개인정보 유출 가능한 상황"
        attachments_dict['mrkdwn_in'] = ["text", "pretext"]  # 마크다운을 적용시킬 인자들을 선택합니다.
        attachments = [attachments_dict]

    # Send to slack : 각 요소들을 합쳐서 하나의 메시지로 전송
        slack.chat.post_message(channel="#newsfeed", text=None, attachments=attachments, as_user=False)
        print ("Post " + str(num) + " is sent.")
        num += 1
    print ("Finished to send to Slack! Check your slack :)")


# {period_seconds}초마다 주기적으로 메시지 보내기
period_seconds = 600

while True:
    print (datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
    if datetime.utcnow().second % period_seconds == 0:
        scrap()
    else:
        continue


# End
