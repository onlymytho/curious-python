# -*- coding:utf-8 -*-
from datetime import datetime
import urllib
import time
from JsonHandler import JsonHandler
import Record as r
import pprint as p
import io

# auth 파일에서 slack_app_token 받아오기
import sys
sys.path.insert(0, "/Users/onlymytho/python")
import auth

slack_token = auth.slack_app_token

def setURL(method):
    token_as_param = 'token='+slack_token
    url = method + token_as_param
    return url

def get_channel_list(args='name', channel_id=None):
    # Refer to this doc : https://api.slack.com/methods/channels.list
    # It returns the names of channel list as Dict type.
    # args are in [all, name, id]
    method = 'https://slack.com/api/channels.list?'
    url = setURL(method)
    channel_dict = JsonHandler.URLParserJsonDict(url)
    channel_info = []

    for channels in channel_dict['channels']:
        if args is 'name':
            channel_name = channels.get('name')
            channel_info.append(channel_name)
        elif args is 'all':
            channel_info.append(channels)
        elif args is 'id':
            if type(channel_id) is str:
                if channels.get('id') is channel_id :
                    channel_info.append(channel_id)
                else :
                    pass
            else:
                channel_id = channels.get('id')
                channel_info.append(channel_id)
    return channel_info

def get_user_list(args='name'):
    # Refer to this doc : https://api.slack.com/methods/users.list
    # It returns the names of user list as Dict type.
    method = 'https://slack.com/api/users.list?'
    url = setURL(method)
    user_dict = JsonHandler.URLParserJsonDict(url)
    user_info = []
    for user in user_dict['members']:
        if user.get('is_bot'):
            pass
        else:
            if args is 'name':
                user_name = user.get('name')
                user_names.append(user_name)
            elif args is 'id':
                user_id = user = user.get('id')
                user_info.append(user_id)
            elif args is 'all':
                user_info = user
    return user_info

def get_channel_history(channel):
    # Refer to this doc : https://api.slack.com/methods/channel.history
    # It returns the messages of channel as Dict type.
    method = 'https://slack.com/api/channels.history?'
    if channel is 'all':
        channel_id_list = get_channel_list(args='id')
        channel_and_message_list = {}
        for channel_id in channel_id_list:
            url = setURL(method) + '&channel=' + channel_id
            channel_messages_dict = JsonHandler.URLParserJson(url)
            channel_and_message_list[channel_id] = channel_messages_dict
        channel_messages_dict = channel_and_message_list
    elif type(channel) is str:
        url = setURL(method) + '&channel=' + channel
        channel_messages_dict = JsonHandler.URLParserJsonDict(url)
    else:
        print ("Insert channel_id or 'all' as parameter of get_channel_history(channel) method.")

    return channel_messages_dict



class run: # 돌려봤거나 돌려볼만한 실행 함수들 모아두는 곳. 위 메서드들을 활용한 것들. 여기 있는 것만 잘 활용해서 돌려도 웬만한 값들은 구하는 느낌
    # A채널에 B유저의 메시지 모두 가져오기
    def bring_all_messages_from_user_at_channel():
        r.start()
        user1_messages = []
        user2_messages = []
        channel_messages = get_channel_history('C04DUH6FT')
        for message in channel_messages['messages']:
            if message['user'] == 'U0A9D7GUQ': #새미님
                user1_messages.append(message)
            elif message['user'] == 'U02FDEHUP':
                user2_messages.append(message)
            else:
                pass
        print ("\n\n\n\n\nMESSAGES FROM SAEMI_KIM")
        p.pprint (user1_messages)
        print ("\n\n\n\n\nMESSAGES FROM SURYEON_KIM")
        p.pprint (user2_messages)
        r.end()
    

    # 모든 유저 목록 가져오기
    def bring_all_user_id():
        p.pprint(get_user_list('id'))

# 실제로 돌아가는 부분
if __name__ == '__main__' :
    run.bring_all_messages_from_user_at_channel()


# with open('data/slack.vteam/all_messages.json', 'w') as f:
#     f.write(str(a))
