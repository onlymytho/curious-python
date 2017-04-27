from datetime import datetime

# 시간 기록 클래스. r.start()와 r.end()를 활용. 여러 개의 시간 기록들을 이용할 경우, 기록인자.r.start()와 기록인자.r.end() 이용
    # 특정 기록인자 없이 그저 기록


def start():
    global t
    t = datetime.now()
    return t

def end():
    end = datetime.now()
    d = end - t
    print ("Duration : " + str(d))
