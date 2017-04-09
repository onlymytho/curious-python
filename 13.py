# 참고 : http://pearl.cs.pusan.ac.kr/~wiki/images/4/46/TR14-09-PBK-b.pdf

# -*- coding: utf-8 -*-
from konlpy.tag import Kkma
from konlpy.utils import pprint
import JsonHandler

t = JsonHandler.JsonHandler.OpenFile('testers_tickets/testers_tickets 2017-04-04 09-41-20.583485.txt')
kkma = Kkma()
print (kkma.nouns(t))
