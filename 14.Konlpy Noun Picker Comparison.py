# 참고 : http://pearl.cs.pusan.ac.kr/~wiki/images/4/46/TR14-09-PBK-b.pdf

# -*- coding: utf-8 -*-

from konlpy.utils import pprint
from konlpy.tag import Kkma, Twitter, Komoran, Hannanum

from konlpy import tag
from konlpy.corpus import kolaw
from konlpy.utils import pprint

from datetime import datetime

import JsonHandler

sample = "아버지는 짜장면이 싫다고 하셨지"
sample = '댓글 하트를 눌러도 취소가되는 황당한 일이 발생하고 댓글 인기순이랑 최신순 단순화햇다고 생각하지만 오히려 더불편해졌습니다.'#그리고 카드를 볼때 좋아요개수가 몇개인지 댓글이 몇개인지 한번에 볼수없어서 불편합니다.타자칠때도 약간 랙이걸리고요 사진보려면 사진이 좀늦게 나옵니다.좋아할만한 카드들이라면서 추천하는 카드들이 회색네모에서 한참뒤에 사진이나 글이나옵니다.빠른시일내에 고쳐주시면 감사하겟습니다


Kkma = Kkma()
Twitter = Twitter()
Komoran = Komoran()
Hannanum = Hannanum()

tag_list = ['Kkma', 'Twitter', 'Komoran']
tag_var = [Kkma, Twitter, Komoran]

start = 0
finish = 0
duration = 0


def tagging(tagger, text):
    r = []
    try:
        r = getattr(tag, tagger)().pos(text)
    except Exception as e:
        pass
        print ("Uhoh,", e)
    return r

def measure_accuracy(tag, sample):
    # print ('\n%s' % sample)
    r = tagging(tag, sample)
    return r



if __name__=='__main__':

    # Accuracy

    for num in range(0,len(tag_list)):
        accuracy = measure_accuracy(tag_list[num], sample)

        start = datetime.now()
        print ("This is " + tag_list[num] + " ---------------------")

        print (tag_var[num].nouns(sample))
        finish = datetime.now()
        duration = finish-start
        print (duration)
        pprint (accuracy)
        print ("\n")


# t = JsonHandler.JsonHandler.OpenFile('data/testers_tickets/testers_tickets 2017-04-04 09-41-20.583485.txt')

# with open('data/testers_tickets/testers_tickets 2017-04-04 09-41-20.583485.txt', 'r') as f:
#     data = f.read()
