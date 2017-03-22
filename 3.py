#경마 프로그램

class Horse:
    horse_count = 0
    horse = []

    def __init__(self, name, birthyear):
        Horse.horse.append(self)
        self.name = name
        self.birthyear = birthyear
        self.condition = 'A'
        self.career = []
        Horse.horse_count += 1

    def profile(self):
        print ("이름 :", self.name)
        print ("생년 :", self.birthyear)

    def update_history(self, game_num, result):
        self.history = ()
        self.history.game_num = result

    # 말 예시...
    # horse_names = ['jason', 'mark', 'zohn', 'royce']
    # horse_birthyears = ['1990', '1998', '2010', '2007']
    # horse_careers = []


class Game:
    game_num = 1
    game = []

    def __init__(self):
        self = game[game_num]
        game_num += 1

    def init(self):
        self.horse = Horse.horse
        self.betting = []
        # self.betting = [{}, {'john':500, 'mr.lover':3000}, {'mrs.lady':1200}]
        self.result = []
        for i in range(len(self.horse)):
            self.betting.append({})
            self.result.append({})

    def start(self):
        print ("#",game_num,"번 게임에 오신 것을 환영합니다.\n베팅할 말을 선택해주세요.")


    def betting(self, horse_num, money):
        pass
#        self.betting[horse_num].['player_name'] = money
        #여기서 horse_num뿐 아니라 말의 이름을 입력해도 되도록 하고 싶은데... 좀 헷갈리네

# game = []
# betting = []
# result = []
#
# for i in range(len(game)):
#     game[i] = [betting, result]
#     for i in range(Horse.horse_count):
#         betting.append()
#         result.append()

# game = [game_num][types(betting, result)][horse_num]
#
# example :
# game = [1][betting][1] = -500 : 1번 게임에서 1번마에 500원 베팅
# game = [1][betting][2] = -400 : 1번 게임에서 1번마에 400원 베팅
# game = [1][betting][3] = 0 : 1번 게임에서 1번마에 0원 베팅
# game = [1][result][1] = 2500 : 1번 게임에서 1번마를 통해 2500원 수익. (즉, 2000원 이익)
# game = [1][result][2] = 400 : 1번 게임에서 1번마를 통해 400원 수익. (즉, 0원 이익)


class Text:
    class KO:
        global_divider = "---------------------------------"
        global_get_yn_condition = "Y 혹은 N을 입력해주세요."
        global_get_yn_condition_simple = "(Y/N)"

        show_horse_list_init = "우리 경마장 말들을 구경하려 오셨군요."
        show_horse_list_get_option = "원하는 행동을 선택해주세요."

        add_horse_init = "말 등록 : 말 등록을 위해 제가 물어보는 순서대로 차근차근 대답해주시면 됩니다.\n"
        add_horse_get_name = "등록하려는 말의 이름은 무엇인가요?"
        add_horse_get_birthyear = "등록하려는 말이 태어난 년도는 언제인가요?"
        add_horse_check = "입력하신 정보가 맞나요?"
        add_horse_confirm = "말 등록 완료!"
        add_horse_name = "이름"
        add_horse_birthyear = "태어난 해"

        start_welcome = "경마 게임에 오신 것을 환영합니다."
        start_get_option = "원하는 행동을 선택해주세요."
        start_close = "게임을 종료합니다."

# 글로벌 지원언어 관리를 조금 더 쉽게 하고자 이런 시도를 해봤으나... 오류가 떠서 실패 ㅜ
# class Text:
#     # [KO, EN, JP, CH, ...]
#     def update(text_key, local_key, text):
#         if text_key:
#             text_key[local_key] = text
#         else:
#             text_key = {'KO':'', 'EN':'', 'JP':'', 'CH':''}
#             update(text_key, local_key, text)
#
#     update(global_divider, 'KO', "---------------------------------")
#     update(show_horse_list_init, 'KO', "우리 경마장 말들을 구경하려 오셨군요.")
#     update(add_horse_init, 'KO', "말 등록 : 말 등록을 위해 제가 물어보는 순서대로 차근차근 대답해주시면 됩니다.\n")
#     update(add_horse_get_name, 'KO', "등록하려는 말의 이름은 무엇인가요?")
#     update(add_horse_get_birthyear, 'KO', "등록하려는 말이 태어난 년도는 언제인가요?")
#     update(add_horse_check, 'KO', "입력하신 정보가 맞나요?")
#     update(add_horse_confirm, 'KO', "말 등록 완료!")
#     update(add_horse_name, 'KO', "이름")
#     update(add_horse_birthyear, 'KO', "태어난 해")





#####---------- 본격 게임에 활용되는 Function 개발 시작

def show_horse_list():
    print (Text.KO.show_horse_list_init + "\n")
    for i in range(Horse.horse_count):
        print (Horse.horse[i].name, "\t", Horse.horse[i].birthyear, "\t" + Horse.horse[i].condition, "\t") #+ Horse.horse[i].career)
    print (Text.KO.global_divider)

    print("/add : 말 등록하기\n/start : 게임 시작하기"+"\n" + "/back : 돌아가기" + "\n")
    option = input(Text.KO.show_horse_list_get_option + "\n" + Text.KO.global_divider)


    if option in ("/add", "add"):
        add_horse()
    elif option in ("/start", "/Start", "/START", "/sTART", "start"):
        game_start(Game.game_num)
    else:
        start()


def add_horse():
    print (Text.KO.add_horse_init)
    name = input(Text.KO.add_horse_get_name + "\n" + Text.KO.global_divider)
    birthyear = input(Text.KO.add_horse_get_birthyear + "\n" + Text.KO.global_divider)
    condition = input(Text.KO.add_horse_check + Text.KO.global_get_yn_condition_simple + "\n" + Text.KO.add_horse_name + " : " + name + "\n" + Text.KO.add_horse_birthyear + " : " + birthyear + "\n" + Text.KO.global_divider)

    if condition in ('Y', 'y', 'Yes', 'yes'):
        Horse(name, birthyear)
        print (Text.KO.add_horse_confirm + "\n" + Text.KO.add_horse_name + " : " + name + "\n" + Text.KO.add_horse_birthyear + " : " + birthyear + "\n" + Text.KO.global_divider)
        start()
    elif condition in ('N', 'n', 'No', 'no'):
        add_horse()
    else :
        condition = input(Text.KO.global_get_yn_condition+"\n"+Text.ko.global_divider)
        start(condition)
    Horse(name, birthyear)


def betting_start(condition):
    if condition in ('Y', 'y'):
        condition = input("베팅하시겠습니까?" + Text.KO.global_get_yn_condition_simple + "\n" + Text.KO.global_divider)
        initiative(condition)
    elif condition in ('N', 'n'):
        input("게임을 하기 싫어하다니...ㅜㅜ\n\n재시작\t: 아무 키나 눌러주세요.\n종료\t: (Mac OS 기준) Control + D를 입력해주세요.\n----------------------------------")
        init()
    else :
        condition = input(Text.KO.global_get_yn_condition + "\n" + Text.KO.global_divider)
        start(condition)


def betting(game_num, horse_num, money):
    game[game_num][0][horse_num] = -money

def game_start(game_num) :
    # if game[game_num] is true :
    #     append
    print("Game #", game_num, " : 베팅 가능한 말은 ..")
    print (Text.KO.global_divider)
    for n in range(Horse.horse_count):
        print(n+1,"번마: ", Horse.horse[n].name)
    print (Text.KO.global_divider)
    betting_start()
    input ("베팅 방법은 'horse_number, money'를 적고 Enter를 입력하면 됩니다.")
    print (Text.KO.global_divider)



def start():
    print(Text.KO.start_welcome + "\n" + Text.KO.global_divider)
    print("/list : 말 목록 보기\n/add : 말 등록하기\n/start : 게임 시작하기"+"\n")
    option = input(Text.KO.start_get_option + "\n" + Text.KO.global_divider)
    if option in ("/list", "/List", "/LIST", "/lIST", "list"):
        show_horse_list()
    elif option in ("/add", "add"):
        add_horse()
    elif option in ("/start", "/Start", "/START", "/sTART", "start"):
        game_start(Game.game_num)
    else:
        print(Text.KO.start_close)
        exit


Horse('jake', 1928)

start()
# show_horse_list()
# add_horse()
# game_start(1)





# career = []
#
# game_num = 0
#
# def betting(game, horse):
#
# def game(game_num):
#     print("Game #" + game_num + " : 원하는 말에게 베팅해주세요.")
#c     print("-------------------------\n1번마 : " + horse(1) +)
#
