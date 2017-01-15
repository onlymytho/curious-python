#baskin-robbins-31-game

#Rule
#숫자를 여러 개 연속으로 말할 때는 숫자와 숫자를 띄어쓰기로 구분함

#To-Do
#숫자 말고 이상한 걸 말했을 때, 숫자를 말하라고 말해줘야 함
#숫자를 연속적으로 입력했는지 체크해야 함
#숫자를 3개까지만 말했는지 체크해야 함

import shlex
from random import randint

def get_first_num(number):
    input_num = []
    prev_first_num = 0

    input_num = shlex.split(str(number))
    prev_first_num = input_num[0]
    return int(prev_first_num)

def get_last_num(number):
    input_num = []
    prev_last_num = 0

    input_num = shlex.split(str(number))
    prev_last_num = input_num[-1]
    return int(prev_last_num)

def continue_play(number, validation_num):

    prev_first_num = get_first_num(number)
    prev_last_num = get_last_num(number)

    validation_num = int(validation_num)

    if (prev_first_num-1) != validation_num:
        number = input("제가 말한 숫자 다음부터 말해야 돼요!\n제가 마지막으로 말한 숫자는 " + str(validation_num) + "입니다. " + str(validation_num+1) + "부터 다시 말해주세요.\n----------------------------------")
        continue_play(number, validation_num)
    elif (prev_first_num-1) == validation_num:
        if int(prev_last_num) < 31:
            pick_next_num(int(prev_last_num))
        elif int(prev_last_num) == 31:
            print ("게임이 끝났습니다. 제가 이겼네요 :)\n")
            condition = input("다시 시작하시려면 아무 키나 눌러주세요.\n종료하시려면 Mac OS 기준으로 Control + D를 입력해주세요.\n----------------------------------")
            start(condition)
        elif (int(prev_last_num) + 1) > 31:
            number = input("뭔가 이상한데... 이런 숫자가 나올 리가 없어요;; 다시 입력해주실래요?\n----------------------------------")
            continue_play(number)


def pick_init_num():
    print ("그럼 제가 먼저 시작하겠습니다 :)")
    my_nums = []
    for n in range(1, randint(2,4)):
        print (n)
        my_nums.append(n)
    number = input("다음 숫자를 말씀해주세요\n----------------------------------")

    continue_play(number, my_nums[-1])


def pick_next_num(prev_last_num):
    my_nums = []
    if (prev_last_num+1) < 31:
        for n in range(1, randint(2,4)):
            print (prev_last_num+1)
            my_nums.append(prev_last_num+1)
            prev_last_num = prev_last_num+1
        number = input("다음 숫자를 말씀해주세요\n----------------------------------")
        continue_play(number, my_nums[-1])
    elif (prev_last_num + 1) == 31:
        condition = input("제가 졌네요ㅜㅜ 생각보다 잘 하시는군요. 한 판 더 하실래요? (Y/N)\n----------------------------------")
        start(condition)
    elif (prev_last_num + 1) > 31:
        number = input("뭔가 이상한데... 이런 숫자가 나올 리가 없어요;; 다시 입력해주실래요?\n----------------------------------")
        continue_play(number)

def initiative(condition):
    if condition in ('Y', 'y'):
        number = input("첫 번째 숫자를 말씀해주세요.\n----------------------------------")
        prev_last_num = get_last_num(number)
        pick_next_num(int(prev_last_num))
    elif condition in ('N', 'n'):
        pick_init_num()
    else :
        condition = input("Y 혹은 N을 입력해주세요.\n----------------------------------")
        initiative(condition)

def start(condition):
    if condition in ('Y', 'y'):
        condition = input("먼저 진행하시겠습니까? (Y/N)\n----------------------------------")
        initiative(condition)
    elif condition in ('N', 'n'):
        input("게임을 하기 싫어하다니...ㅜㅜ\n\n재시작\t: 아무 키나 눌러주세요.\n종료\t: (Mac OS 기준) Control + D를 입력해주세요.\n----------------------------------")
        init()
    else :
        condition = input("Y 혹은 N을 입력해주세요.\n----------------------------------")
        start(condition)


def init():
    condition = input("베스킨라빈스 31 게임입니다. 시작하시겠습니까? (Y/N)\n----------------------------------")
    start(condition)


init()



#
#
#
#
#
#
#
#
#
#
#
#
#
#
