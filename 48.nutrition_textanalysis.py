from konlpy.tag import Kkma
from konlpy.utils import pprint
from datetime import datetime
import time
import csv
import Record as r

kkma = Kkma()
# pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
# pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
# result = kkma.nouns(u"""비타민 A는 시각과 상피세포가 분화하는 과정에 관여한다. 면역반응, 성장 등에 필수적인 요소이며 항암작용이 있는 것으로 알려져 있다.
# 칼슘과 인의 흡수를 촉진시키며 조직 중의 인산을 칼슘과 결합시켜 뼈에 침착되게 해 골격형성과 치아건강에 중요한 역할을 한다. 비타민 D는 혈중 칼슘 농도를 조절하여 칼슘 항상성을 유지한다. 혈액의 칼슘 농도가 감소하면 부갑상선 호르몬이 분비되어 신장에서 칼슘의 재흡수와 활성형 비타민 D2의 형성을 촉진한다. 활성형 비타민 D2는 소장점막세포에서 칼슘과 인의 흡수를 촉진시켜 혈액 내 칼슘 농도를 증가시키며 뼈에 저장되어 있는 칼슘이 혈액으로 용해되어 나오는 것을 촉진시킨다. 칼슘 농도가 일정 수준보다 증가하면 갑상선에서 칼시토닌이 분비되어 뼈로 칼슘을 이동시켜 혈중 칼슘 농도를 일정하게 유지한다."""))

pprint (kkma.nouns(u"호올스가 별로 맛이 없었다. 그럼 어떤 호올스가 맛있을까?"))

# a = datetime.now()
# f = open('data/sugaryesplease/syp-nutrition-textanalysis-'+' '+str(datetime.now())+'.csv','w', newline='')
# csvWriter = csv.writer(f)
# csvWriter.writerow([
#     'question_id',
#     'option_count',
#     'option_id'
#     ])
#
# csvWriter.writerow(question_set)
