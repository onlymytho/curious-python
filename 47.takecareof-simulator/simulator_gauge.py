from simulator_data import Product, questions
import pprint as p
import inspect
import psycopg2

class Recipe:
    questions = questions
    def __init__(self):
        self.name = ''
        self.priority = ''
        self.gender = ''
        self.age = ''
        self.topic = []
        self.list = {
            'vitamin_b':                {'score': 0, 'effected_by': {}},
            'b_complex':                {'score': 0, 'effected_by': {}},
            'vitamin_c':                {'score': 0, 'effected_by': {}},
            'vitamin_d':                {'score': 0, 'effected_by': {}},
            'prenatal':                 {'score': 0, 'effected_by': {}},
            'vitamin_k2':               {'score': 0, 'effected_by': {}},
            'whole_food_multivitamin':  {'score': 0, 'effected_by': {}},
            'magnesium':                {'score': 0, 'effected_by': {}},
            'bone_triad':               {'score': 0, 'effected_by': {}},
            'iron':                     {'score': 0, 'effected_by': {}},
            'zinc':                     {'score': 0, 'effected_by': {}},
            'ashwagandha':              {'score': 0, 'effected_by': {}},
            'rhodiola':                 {'score': 0, 'effected_by': {}},
            'kanna':                    {'score': 0, 'effected_by': {}},
            'turmeric':                 {'score': 0, 'effected_by': {}},
            'elderberry':               {'score': 0, 'effected_by': {}},
            'milk_thistle':             {'score': 0, 'effected_by': {}},
            'garlic':                   {'score': 0, 'effected_by': {}},
            'evening_primrose_oil':     {'score': 0, 'effected_by': {}},
            'saw_palmetto':             {'score': 0, 'effected_by': {}},
            'probiotic':                {'score': 0, 'effected_by': {}},
            'boulardii':                {'score': 0, 'effected_by': {}},
            'fish_oil':                 {'score': 0, 'effected_by': {}},
            'veggie_omega':             {'score': 0, 'effected_by': {}},
            'astaxanthin':              {'score': 0, 'effected_by': {}},
            'enzyme':                   {'score': 0, 'effected_by': {}},
            'coq10':                    {'score': 0, 'effected_by': {}}
        }
    def setName(self, name):
        self.name = name
    def setPriority(self, this_topic):
        self.priority = self.topic[this_topic]
    def setGender(self, gender):
        self.gender = gender
    def setAge(self, age):
        self.age = age
    def addTopic(self, this_topic):
        self.topic.append(this_topic)
    def addScore(self, product, effect_score, question_name, response):
        # 질문의 답변에 따라 제품에 점수를 주고 답변을 기록하는 모듈
        self.list[product]['score'] += int(str(effect_score))
        self.list[product]['effected_by'][question_name] = {'response': response, 'effect_score': effect_score}
    def show(self, type="selected"):
        if type == 'selected':
            selected_product = []
            for key in self.list:
                if self.list[key]['score'] > 60:
                    selected_product.append(key)
            p.pprint(selected_product)
            # print(selected_product)
        elif type == 'selected_detail':
            selected_product = {}
            for product in self.list:
                if self.list[product]['score'] > 60:
                    selected_product[product] = self.list[product]
            p.pprint(selected_product, width=20, indent=4)
            # print(selected_product)
        elif type == 'all':
            p.pprint(self.list)
            # print(self.list)

class Adjust:
    def getQuestionName():
        return inspect.currentframe().f_back.f_code.co_name
    def name            (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            response = input("이름을 말해주세요:) \n")
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")
        recipe.setName(response)
    def gender          (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            response = input("성별이 어떻게 되시나요? (male/female)\n")
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")
        recipe.setGender(response)
    def age             (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            response = input("나이가 어떻게 되시나요? (숫자를 입력해주세요. ex)24 )\n")
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")
        recipe.setAge(response)
    def topic           (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question_name = 'init'
            response = input(Recipe.questions[question_name]['content_ko'])
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        question_name = Adjust.getQuestionName()

        topic_indexes = response.split()
        for t in topic_indexes:
            this_topic = list(Product.topic.keys())[int(t)-1]
            recipe.addTopic(this_topic)
            for pd in Product.topic[this_topic]:
                recipe.addScore(pd, +100, question_name, response)
    def topicPriority   (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            recipe_topics = ""
            for num in range(0, len(recipe.topic)):
                recipe_topics += "%d) %s\n            " % (num, recipe.topic[num])
            response = input("""
            선택한 기능 중 가장 우선순위가 높은 기능은 어떤 것인가요?
            """ + recipe_topics +
            """
            \n
            """)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        # 응답 결과에 따른 처리
        recipe.setPriority(int(response))
    def topicQuestions  (recipe):
        for topic in recipe.topic:
            if topic == 'bones':
                question_name = 'family_history_osteoporosis'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.vitamin_d, +100, question_name, response)
                    recipe.addScore(Product.vitamin_k2, +100, question_name, response)
                    recipe.addScore(Product.magnesium, +100, question_name, response)
                    recipe.addScore(Product.bone_triad, +100, question_name, response)
            elif topic == 'brain':
                question_name = 'brain_focus_trouble_multitasking'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.ashwagandha, +100, question_name, response)
                    recipe.addScore(Product.kanna, +100, question_name, response)
                    recipe.addScore(Product.fish_oil, +100, question_name, response)
                    recipe.addScore(Product.veggie_omega, +100, question_name, response)
                    recipe.addScore(Product.astaxanthin, +100, question_name, response)
                question_name = 'brain_focus_trouble_focusing'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.rhodiola, +100, question_name, response)
                    recipe.addScore(Product.kanna, +100, question_name, response)
                question_name = 'short_term_memory_concern'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.ashwagandha, +100, question_name, response)
            elif topic == 'prenatal':
                question_name = 'prenatal_postnatal_yes_no'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.bone_triad, +100, question_name, response)
                    recipe.addScore(Product.iron, +100, question_name, response)
                question_name = 'pregnancy_which_of_these'
                response = input(question)
                    # 적용되는 부분 없음
            elif topic == 'digestion':
                question_name = 'digestion_concern'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.probiotic, +100, question_name, response)
                    recipe.addScore(Product.boulardii, +100, question_name, response)
                    recipe.addScore(Product.enzyme, +100, question_name, response)
                question_name = 'digestion_bowel_movements'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.probiotic, +100, question_name, response)
                    recipe.addScore(Product.boulardii, +100, question_name, response)
                    recipe.addScore(Product.enzyme, +100, question_name, response)
            elif topic == 'energy':
                question_name = 'energy_trouble_sleeping'
                response = input(Recipe.questions[question_name]['content_ko'])
                if response == 'y':
                    recipe.addScore(Product.ashwagandha, +100, question_name, response)
                    recipe.addScore(Product.rhodiola, +100, question_name, response)
                    recipe.addScore(Product.kanna, +100, question_name, response)
                    recipe.addScore(Product.magnesium, +100, question_name, response)
                question_name = 'energy_stress_fatigued'
                response = input(Recipe.questions[question_name]['content_ko'])
            elif topic == 'heart':
                question_name = 'heart_family_history_disease'
                response = input(Recipe.questions[question_name]['content_ko'])
                question_name = 'any_heart_concerns'
                response = input(Recipe.questions[question_name]['content_ko'])
            elif topic == 'immunity':
                question_name = 'immunity_frequently_get_sick'
                response = input(Recipe.questions[question_name]['content_ko'])
                question_name = 'immunity_cold_like_symptoms'
                response = input(Recipe.questions[question_name]['content_ko'])
                question_name = 'immunity_traveling_plane'
                response = input(Recipe.questions[question_name]['content_ko'])
                question_name = 'immunity_planning_high_intensity'
                response = input(Recipe.questions[question_name]['content_ko'])
            elif topic == 'skin':
                question_name = 'skin_concerns'
                response = input(Recipe.questions[question_name]['content_ko'])
            elif topic == 'stress':
                question_name = 'is_your_stress'
                response = input(Recipe.questions[question_name]['content_ko'])
                question_name = 'do_you_have_bad_mood'
                response = input(Recipe.questions[question_name]['content_ko'])
            elif topic == 'eyes':
                question_name = 'eyes_computer_screen'
                response = input(Recipe.questions[question_name]['content_ko'])
                question_name = 'eyes_dry_symptoms'
                response = input(Recipe.questions[question_name]['content_ko'])
    def seafood         (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "해산물 자주 드시나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        question_name = Adjust.getQuestionName()

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 생선 많이 먹는 경우
            recipe.addScore(Product.fish_oil, -100, question_name, response)       # 생선기름 제외
            recipe.addScore(Product.veggie_omega, -50, question_name, response)    # 식물성 오메가 제외
            recipe.addScore(Product.astaxanthin, -50, question_name, response)     # 아스타산신 제외
        elif response == 'n':                               ### 생선 별로 안 먹는 경우
            if recipe.list[Product.veggie_omega]['score'] + recipe.list[Product.fish_oil]['score'] == 0 : # 식물성오메가나 생선기름 처방이 안 되어 있으면
                recipe.addScore(Product.fish_oil, +100, question_name, response)    # 생선기름 추가 (만약 채식주의자면 식이요법쪽에서 veggie_omega로 바꿔야 함)
            recipe.addScore(Product.astaxanthin, +100, question_name, response)     # 아스타산신 추가
    def meat            (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "육류를 자주 드시나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        question_name = Adjust.getQuestionName()

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 육류 많이 먹는 경우
            recipe.addScore(Product.vitamin_b, -50, question_name, response)    # 비타민B12 제외
            recipe.addScore(Product.zinc, -50, question_name, response)            # 아연 제외
            recipe.addScore(Product.iron, -50, question_name, response)            # 철분 제외
        elif response == 'n':                               ### 육류 별로 안 먹는 경우
            recipe.addScore(Product.vitamin_b, -100, question_name, response)   # 비타민B12 추가
            recipe.addScore(Product.zinc, -100, question_name, response)           # 아연 추가
            recipe.addScore(Product.iron, -100, question_name, response)           # 철분 추가
    def vegetables      (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "과일이나 야채를 자주 드시나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 과일, 야채를 많이 먹는 경우
            pass
        elif response == 'n':                               ### 과일, 야채를 안 먹는 경우
            pass
    def exercise        (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "운동을 자주 하시나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 운동 많이 하는 경우
            pass
        elif response == 'n':                               ### 운동 별로 안 하는 경우
            pass
    def alcohol         (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "술을 자주 드시나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 육류 많이 먹는 경우
            pass
        elif response == 'n':                               ### 육류 별로 안 먹는 경우
            pass
    def smoke           (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "담배를 많이 피시나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        question_name = Adjust.getQuestionName()

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 담배 피는 경우
            recipe.addScore(Product.fish_oil, -100, question_name, response)       # 생선기름 제외
            recipe.addScore(Product.veggie_omega, -50, question_name, response)    # 식물성 오메가 제외
            recipe.addScore(Product.astaxanthin, -50, question_name, response)     # 아스타산신 제외
        elif response == 'n':                               ### 담배 안 피는 경우
            if recipe.list[Product.veggie_omega]['score'] + recipe.list[Product.fish_oil]['score'] == 0 : # 식물성오메가나 생선기름 처방이 안 되어 있으면
                recipe.addScore(Product.fish_oil, +100, question_name, response)    # 생선기름 추가 (만약 채식주의자면 식이요법쪽에서 veggie_omega로 바꿔야 함)
            recipe.addScore(Product.astaxanthin, +100, question_name, response)     # 아스타산신 추가
    def device          (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "전자기기를 많이 보시나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 전자기기 많이 보는 경우
            pass
        elif response == 'n':                               ### 전자기기 많이 안 보는 경우
            pass
    def medication      (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "먹고 계신 약이 있나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 먹는 약이 있는 경우
            pass
        elif response == 'n':                               ### 먹는 약이 없는 경우
            pass
    def diet            (recipe, response='', question=True):
        # question의 기본값 사용여부에 따른 처리
        if question == True:
            question = "따르고 있는 식이요법이 있나요? (y/n)\n"
            response = input(question)
        else:
            if response == '':
                raise ValueError("If question argument is False, you must pass valid response argument.")

        # 응답 결과에 따른 처리
        if response == 'y':                                 ### 식이요법 있는 경우
            pass
        elif response == 'n':                               ### 식이요법 안 보는 경우
            pass


def run() :
    recipe = Recipe()
    Adjust.name             (recipe)
    Adjust.gender           (recipe)
    Adjust.age              (recipe)
    Adjust.topic            (recipe)
    Adjust.topicPriority    (recipe)
    Adjust.topicQuestions   (recipe)
    Adjust.seafood          (recipe)
    Adjust.meat             (recipe)
    Adjust.vegetables       (recipe)
    Adjust.exercise         (recipe)
    Adjust.alcohol          (recipe)
    Adjust.smoke            (recipe)
    Adjust.device           (recipe)
    Adjust.medication       (recipe)
    Adjust.diet             (recipe)


    recipe.show(type="selected_detail")
    recipe.show()

if __name__ == '__main__':
    run()
