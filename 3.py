#경마 프로그램


horses = []

horse_names = ['jason', 'mark', 'zohn', 'royce']
horse_birthyears = ['1990', '1998', '2010', '2007']
horse_careers = []

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

show_horse_list()

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
