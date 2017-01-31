# 초보자를 위한 파이썬 300제 https://wikidocs.net/book/922

# 012 구분자를 사용한 출력
#
# print() 함수를 사용하여 다음과 같이 출력하라. (힌트: sep 인자 사용)
#
# 실행 예:
# naver;kakao;sk;samsung

# print ("naver"sep"kakao")


# 014 문자열 슬라이싱
#
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하라.
#
# >>> license_plate = "24가 2210"
# 실행 예:
# 2210
#
# license_plate = "24가 2210"
# print ("license_plate")


nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    print (nums.pop())
