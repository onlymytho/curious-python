#경마 프로그램


horses = []

horse_names = ['jason', 'mark', 'zohn', 'royce']
horse_birthyears = ['1990', '1998', '2010', '2007']
horse_careers = []

game = []
betting = []
result = []

for i in range(len(game)):
    game[i] = [betting, result]
    for i in range(len(horse_names)):
        betting.append()
        result.append()

# game = [game_num][types(betting, result)][horse_num]
#
# example :
# game = [1][betting][1] = -500 : 1번 게임에서 1번마에 500원 베팅
# game = [1][betting][2] = -400 : 1번 게임에서 1번마에 400원 베팅
# game = [1][betting][3] = 0 : 1번 게임에서 1번마에 0원 베팅
# game = [1][result][1] = 2500 : 1번 게임에서 1번마를 통해 2500원 수익. (즉, 2000원 이익)
# game = [1][result][2] = 400 : 1번 게임에서 1번마를 통해 400원 수익. (즉, 0원 이익)


if len(horses) != len(horse_names):
    for n in range(len(horse_names) - len(horses)):
        horses.append('')
        horse_careers.append('')

for n in range(len(horse_names)):
    horses[n] = {
        'name' : horse_names[n],
        'birthyear' : horse_birthyears[n],
        # ,
        # 'career' : sum(win),
        # 'velocity' : avg(velocity)
        }
def show_horse_list():
    print ("우리 경마장 말들을 구경하려 오셨군요.")
    for n in range(len(horses)):
        print (horses[n])
    print ("---------------------------------")

def betting_start(condition):
    condition


def betting_start(condition):
    if condition in ('Y', 'y'):
        condition = input("베팅하시겠습니까? (Y/N)\n----------------------------------")
        initiative(condition)
    elif condition in ('N', 'n'):
        input("게임을 하기 싫어하다니...ㅜㅜ\n\n재시작\t: 아무 키나 눌러주세요.\n종료\t: (Mac OS 기준) Control + D를 입력해주세요.\n----------------------------------")
        init()
    else :
        condition = input("Y 혹은 N을 입력해주세요.\n----------------------------------")
        start(condition)


def betting(game_num, horse_num, money):
    game[game_num][0][horse_num] = -money

def game_start(game_num) :
    # if game[game_num] is true :
    #     append
    print("Game #", game_num, " : 베팅 가능한 말은 ..")
    print ("---------------------------------")
    for n in range(len(horses)):
        print(n+1,"번마: ", horse_names[n])
    print ("---------------------------------")
    betting_start()
    print ("베팅 방법은 'horse_number, money'를 적고 Enter를 입력하면 됩니다.")
    print ("---------------------------------")

show_horse_list()
game_start(1)

#
# career = []
#
# game_num = 0
#
# def betting(game, horse):
#
# def game(game_num):
#     print("Game #" + game_num + " : 원하는 말에게 베팅해주세요.")
#     print("-------------------------\n1번마 : " + horse(1) +)
#
# def start():
#     print("경마 게임에 오신 것을 환영합니다.\n-----------------------------")
#     print("/list : 말 목록 보기\n/start : 게임 시작하기")
