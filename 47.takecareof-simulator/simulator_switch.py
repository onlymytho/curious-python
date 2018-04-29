import pprint as p

product_list = {
    'product': {
        'Vitamin B12': ['Energy'],
        'B-Complex': ['Energy'],
        'Vitamin C': ['Immunity'],
        'Vitamin D': ['Bones'],
        'Prenatal': ['Prenatal'],
        'Vitamin K2': ['Heart', 'Bones'],
        'Multivitamin': [],
        'Magnesium': ['Bones'],
        'Calcium Plus': ['Prenatal','Bones'],
        'Iron': ['Energy', 'Prenatal'],
        'Zinc': ['Immunity'],
        'Ashwagandha': ['Brain', 'Stress'],
        'Rhodiola': ['Brain', 'Energy', 'Stress'],
        'Kanna': ['Brain', 'Stress'],
        'Turmeric': ['Joints'],
        'Elderberry': ['Immunity'],
        'Milk Thistle': [],
        'Garlic': ['Heart', 'Immunity'],
        'Evening Primrose': ['Skin'],
        'Saw Palmetto': [],
        'Probiotic Blend': ['Immunity', 'Prenatal', 'Digestion'],
        'S. boulardii': ['Digestion'],
        'Fish Oil': ['Brain', 'Eyes', 'Heart', 'Joints', 'Prenatal', 'Digestion'],
        'Veggie Omega': ['Brain', 'Eyes', 'Heart', 'Joints', 'Prenatal'],
        'Astaxanthin': ['Brain', 'Heart', 'Skin'],
        'Digestive Enzymes': ['Digestion'],
        'CoQ10': ['Heart']
    },
    'topic': {
        'brain': [
            'Ashwagandha',
            'Rhodiola',
            'Kanna',
            'Fish Oil',
            'Veggie Omega',
            'Astaxanthin'
        ],
        'energy': [
            'Vitamin B12',
            'B-Complex',
            'Iron',
            'Rhodiola'
        ],
        'eyes': [
            'Fish Oil',
            'Veggie Omega'
        ],
        'heart': [
            'Vitamin K2',
            'Garlic',
            'Fish Oil',
            'Veggie Omega',
            'Astaxanthin',
            'CoQ10'
        ],
        'immunity': [
            'Vitamin C',
            'Zinc',
            'Elderberry',
            'Garlic',
            'Probiotic Blend'
        ],
        'joints': [
            'Turmeric',
            'Fish Oil',
            'Veggie Omega'
        ],
        'prenatal': [
            'Prenatal',
            'Calcium Plus',
            'Iron',
            'Probiotic Blend',
            'Fish Oil',
            'Veggie Omega'
        ],
        'bones': [
            'Vitamin D',
            'Vitamin K2',
            'Magnesium',
            'Calcium Plus'
        ],
        'stress': [
            'Ashwagandha',
            'Rhodiola',
            'Kanna'
        ],
        'digestion': [
            'Probiotic Blend',
            'S. boulardii',
            'Fish Oil',
            'Digestive Enzymes'
        ],
        'skin': [
            'Evening Primrose',
            'Astaxanthin'
        ]
    }
}

# command = input("\n\n어서오세요!\n제품 목록(list)을 보거나 맞춤 처방(start)을 시작할 수 있습니다. 종료하려면 'exit'을 입력해주세요.\n")
# if command == 'exit':
#     exit()
# elif command == 'list':
#     p.pprint (product_list)
# elif command == 'start':
selected_topic = input("""
원하는 기능의 번호를 입력해주세요. 여러 가지를 원한다면 띄어쓰기로 구분해주세요.
(1) Brain
(2) Energy
(3) Eyes
(4) Heart
(5) Immunity
(6) Joints
(7) Prenatal
(8) Bones
(9) Stress
(10) Digestion
(11) Skin
\n
""")
topic_indexes = selected_topic.split()
chosen_products = []
for t in topic_indexes:
    this_topic = list(product_list['topic'].keys())[int(t)-1]
    for pd in product_list['topic'][this_topic]:
        if chosen_products.count(pd) == 0:
            chosen_products.append(pd)
p.pprint (chosen_products)

class checklist:
    def seafood(recipe, response):
        if response == 'many':                          # 해산물 많이 먹으면
            try:
                recipe.remove('Fish Oil')               # 생선기름 제외
                recipe.remove('Veggie Omega')           # 식물성 오메가 제외
                recipe.remove('Astaxanthin')            # 아스타산신 제외
            except ValueError:                          # 만약 이미 리스트에 없는 걸 없애려고 했다면
                pass                                    # 그냥 잘 됐다고 생각하고 넘어가기
        if response == 'little':                        # 해산물 별로 안 먹으면
            if recipe.count('Veggie Omega') + recipe.count('Fish Oil') == 0 and : # 식물성오메가나 생선기름 처방이 안 되어 있으면
                recipe.append('Fish Oil')               # 생선기름 추가 (만약 채식주의자면 식이요법쪽에서 Veggie Omega로 바꿔야 함)
            recipe.append('Astaxanthin')                # 아스타산신 추가

    def meat(recipe, response):
        if response == 'many':
            recipe.remove('B-Complex')                  # 비타민-B12 많이 먹으니까 B복합체 제거 (다른데서도 검토해야 함)
            recipe.remove('Zinc')                       # 아연 제외
            recipe.remove('iron')                       # 철분 제외
            # 이렇게 쉽게 빼버리면, 다른 것 때문에 필요한 사람은 손해보게 될 수 있음.
            # 점수 개념으로 하는 편이 나을 수 있을 것 같은데, 그럼 제대로 된 점수 배점을 주는 게 관건.
        if response == 'little':
            recipe.append('B-Complex')                  # 비타민-B12 먹기 위해 B복합체 추가
            recipe.append('Zinc')                       # 아연 추가
            recipe.append('iron')                       # 철분 추가
    def vegetables(recipe, response):

    def exercise(recipe, response):

    def alcohol(recipe, response):

    def smoke(recipe, response):
        if response == 'many':
            try:
                recipe.remove('Fish Oil')
                recipe.remove('Veggie Omega')
                recipe.remove('Astaxanthin')
            except ValueError:
                pass
        if response == 'little':
            if recipe.count('Veggie Omega') == 0:
                recipe.append('Fish Oil')
            recipe.append('Astaxanthin')

    def device(recipe, response):

    def medication(recipe, response):

    def diet(recipe, response):
