class Product:
    vitamin_b = 'vitamin_b'
    b_complex = 'b_complex'
    vitamin_c = 'vitamin_c'
    vitamin_d = 'vitamin_d'
    prenatal = 'prenatal'
    vitamin_k2 = 'vitamin_k2'
    whole_food_multivitamin = 'whole_food_multivitamin'
    magnesium = 'magnesium'
    bone_triad = 'bone_triad'
    iron = 'iron'
    zinc = 'zinc'
    ashwagandha = 'ashwagandha'
    rhodiola = 'rhodiola'
    kanna = 'kanna'
    turmeric = 'turmeric'
    elderberry = 'elderberry'
    milk_thistle = 'milk_thistle'
    garlic = 'garlic'
    evening_primrose_oil = 'evening_primrose_oil'
    saw_palmetto = 'saw_palmetto'
    probiotic = 'probiotic'
    boulardii = 'boulardii'
    fish_oil = 'fish_oil'
    veggie_omega = 'veggie_omega'
    astaxanthin = 'astaxanthin'
    enzyme = 'enzyme'
    coq10 = 'coq10'

    topic = {
        'brain': [
            ashwagandha,
            rhodiola,
            kanna,
            fish_oil,
            veggie_omega,
            astaxanthin
        ],
        'energy': [
            vitamin_b,
            b_complex,
            iron,
            rhodiola
        ],
        'eyes': [
            fish_oil,
            veggie_omega
        ],
        'heart': [
            vitamin_k2,
            garlic,
            fish_oil,
            veggie_omega,
            astaxanthin,
            coq10
        ],
        'immunity': [
            vitamin_c,
            zinc,
            elderberry,
            garlic,
            probiotic
        ],
        'joints': [
            turmeric,
            fish_oil,
            veggie_omega
        ],
        'prenatal': [
            prenatal,
            bone_triad,
            iron,
            probiotic,
            fish_oil,
            veggie_omega
        ],
        'bones': [
            vitamin_d,
            vitamin_k2,
            magnesium,
            bone_triad
        ],
        'stress': [
            ashwagandha,
            rhodiola,
            kanna
        ],
        'digestion': [
            probiotic,
            boulardii,
            fish_oil,
            enzyme
        ],
        'skin': [
            evening_primrose_oil,
            astaxanthin
        ]
    }

questions = {
    "init": {"content_ko": """
    원하는 기능의 번호를 입력해주세요. 여러 기능을 선택하려면 띄어쓰기로 구분해주세요. (ex. 1 2 3)
    1) 두뇌\t\t(Brain)
    2) 에너지\t\t(Energy)
    3) 눈\t\t(Eyes)
    4) 심장\t\t(Heart)
    5) 면역력\t\t(Immunity)
    6) 관절\t\t(Joints)
    7) 임신\t\t(Prenatal)
    8) 뼈\t\t(Bones)
    9) 스트레스\t\t(Stress)
    10) 소화\t\t(Digestion)
    11) 피부\t\t(Skin)
    \n
    """},
    "vitamins_supplements_past": {"content_ko": "이전에 비타민이나 영양제를 드신 적이 있나요?"},
    "number_vitamins_recommendation": {"content_ko": "보통 몇 개를 드셨나요?"},
    "vitamins_supplements_how_often_adherence": {"content_ko": "보통 한 주에 몇 번 챙겨드셨나요?"},
    "curious_currently_take_vitamins_supplements": {"content_ko": "지금 드시고 계신 비타민이나 영양제가 있나요?"},
    "gender": {"content_ko": "성별을 알려주세요"},
    "age": {"content_ko": "나이를 알려주세요"},
    "prenatal_postnatal_yes_no": {"content_ko": "임신 혹은 산후 건강에 대해 관심 있으신가요?"},
    "pregnancy_which_of_these": {"content_ko": "임신 및 출산에 대해 {{first_name}}님을 어떻게 이해하면 될까요?"},
    "topics": {"content_ko": "어떤 기능에 관심 있으신가요?"},
    "most_important": {"content_ko": "이 중 가장 우선순위가 높은 건 어떤 건가요?"},
    "family_history_osteoporosis": {"content_ko": "가족 중에 뼈와 관련된 증상을 겪은 분이 계신가요?"},
    "brain_focus_trouble_multitasking": {"content_ko": "멀티태스킹(동시에 여러 일을 하는 것)이 어려우신가요?"},
    "brain_focus_trouble_focusing": {"content_ko": "집중력이 낮으신가요?"},
    "short_term_memory_concern": {"content_ko": "단기 기억력이 안 좋으신가요?"},
    "digestion_concern": {"content_ko": "소화에 문제를 겪고 계신가요?"},
    "digestion_bowel_movements": {"content_ko": "대변을 얼마나 자주 보시나요?"},
    "energy_trouble_sleeping": {"content_ko": "잠에 잘 들지 못 하는 편인가요?"},
    "energy_stress_fatigued": {"content_ko": "지치거나 번아웃 증상을 겪고 계신가요?"},
    "heart_family_history_disease": {"content_ko": "가족 중에 심장 실환을 겪은 분이 계신가요?"},
    "any_heart_concerns": {"content_ko": "심장과 관련해서 어떤 고민이 있으신가요?"},
    "immunity_frequently_get_sick": {"content_ko": "자주 아프신가요?"},
    "immunity_cold_like_symptoms": {"content_ko": "지금 감기에 걸렸나요?"},
    "immunity_traveling_plane": {"content_ko": "다음 달 이내에 비행기 탈 일이 있나요?"},
    "immunity_planning_high_intensity": {"content_ko": "강도 높은 운동을 자주 하시나요?"},
    "skin_concerns": {"content_ko": "어떤 피부 고민이 있으신가요?"},
    "is_your_stress": {"content_ko": "스트레스를 많이 받으시는 편인가요?"},
    "do_you_have_bad_mood": {"content_ko": "최근에 기분이 별로 안 좋으신가요?"},
    "fish": {"content_ko": "보통 한 주에 해산물을 얼마나 자주 드시나요?"},
    "meat": {"content_ko": "보통 한 주에 육류를 얼마나 자주 드시나요?"},
    "fruits_vegetables": {"content_ko": "보통 하루에 과일이나 야채를 얼마나 자주 드시나요?"},
    "dairy": {"content_ko": "보통 하루에 음료를 얼마나 자주 드시나요?"},
    "exercise": {"content_ko": "보통 한 주에 운동을 얼마나 하시나요?"},
    "female_alcohol_three_single_day": {"content_ko": "하루에 4잔 이상의 술을 마시나요?"},
    "male_alcohol_four_single_day": {"content_ko": "하루에 5잔 이상의 술을 마시나요?"},
    "exercise_muscle_recovery": {"content_ko": "운동 후 근육회복에 도움이 필요하신가요?"},
    "female_alcohol_seven_week": {"content_ko": "한 주에 8잔 이상의 술을 마시나요?"},
    "male_alcohol_fourteen_week": {"content_ko": "한 주에 15잔 이상의 술을 마시나요?"},
    "smoke": {"content_ko": "흡연하시나요?"},
    "eyes_computer_screen": {"content_ko": "하루에 3시간 이상 모니터 혹은 전자기기를 보시나요?"},
    "eyes_dry_symptoms": {"content_ko": "눈이 건조하거나, 빨개지거나, 화상 입은듯한 느낌을 받으시나요?"},
    "medications_ssri": {"content_ko": "현재 항불안제나 항우울제를 복용하고 계신가요?"},
    "allergies": {"content_ko": "다음 중 겪고 있는 알레르기 증상이 있으신가요?"},
    "restrictions_diet": {"content_ko": "다음 중 따르고 있는 식이요법이 있으신가요?"}
}

# product_list = {
#     'product': {
#         'vitamin_b': ['Energy'],
#         'b_complex': ['Energy'],
#         'vitamin_c': ['Immunity'],
#         'vitamin_d': ['Bones'],
#         'prenatal': ['prenatal'],
#         'vitamin_k2': ['Heart', 'Bones'],
#         'whole_food_multivitamin': [],
#         'magnesium': ['Bones'],
#         'bone_triad': ['prenatal','Bones'],
#         'iron': ['Energy', 'prenatal'],
#         'zinc': ['Immunity'],
#         'ashwagandha': ['Brain', 'Stress'],
#         'rhodiola': ['Brain', 'Energy', 'Stress'],
#         'kanna': ['Brain', 'Stress'],
#         'turmeric': ['Joints'],
#         'elderberry': ['Immunity'],
#         'milk_thistle': [],
#         'garlic': ['Heart', 'Immunity'],
#         'evening_primrose_oil': ['Skin'],
#         'saw_palmetto': [],
#         'probiotic': ['Immunity', 'prenatal', 'Digestion'],
#         'boulardii': ['Digestion'],
#         'fish_oil': ['Brain', 'Eyes', 'Heart', 'Joints', 'prenatal', 'Digestion'],
#         'veggie_omega': ['Brain', 'Eyes', 'Heart', 'Joints', 'prenatal'],
#         'astaxanthin': ['Brain', 'Heart', 'Skin'],
#         'enzyme': ['Digestion'],
#         'coq10': ['Heart']
#     }
# }

# questions
# 보통 한 주에 해산물을 얼마나 자주 드시나요?
# 보통 한 주에 육류를 얼마나 자주 드시나요?
# 보통 하루에 과일이나 야채를 얼마나 자주 드시나요?
# 보통 하루에 음료를 얼마나 자주 드시나요?
# 보통 한 주에 운동을 얼마나 하시나요?
# 하루에 4잔 이상의 술을 마시나요?
# 하루에 5잔 이상의 술을 마시나요?
# 운동 후 근육회복에 도움이 필요하신가요?
# 하루에 8잔 이상의 술을 마시나요?
# 하루에 15잔 이상의 술을 마시나요?
# 흡연하시나요?
# 하루에 3시간 이상 모니터 혹은 전자기기를 보시나요?
# 눈이 건조하거나, 빨개지거나, 화상 입은듯한 느낌을 받으시나요?
# 현재 항불안제나 항우울제를 복용하고 계신가요?
# 다음 중 겪고 있는 알레르기 증상이 있으신가요?
# 다음 중 따르고 있는 식이요법이 있으신가요?
