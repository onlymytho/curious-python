# 1898570 방에서 400에러 뜨는 거 잡기
# 방이 존재하는 범위로 돌렸는데, 가끔씩 데이터를 못 불러오는 경우에 대해 해결하기.
# csv export까지 하는 프로그램으로 제작하기

from bs4 import BeautifulSoup
import urllib.request
import html5lib
from datetime import datetime
import time
import csv
import Record as r

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
       }

products = ['vitamin-b-12_1', 'b-complex_3', 'vitamin-c_1', 'vitamin-d-1000_2', 'prenatal_1', 'vitamin-k2_1', 'whole-food-multivitamin_2', 'magnesium-small_1', 'bone-triad_2', 'iron_1', 'zinc_1', 'ashwagandha_1', 'rhodiola_1', 'kanna_1', 'turmeric_1', 'elderberry_1', 'milk-thistle_1', 'garlic_1', 'evening-primrose-oil_1', 'saw-palmetto_1', 'probiotic_1', 'boulardii_1', 'fish-oil_1', 'veggie-omega_1', 'astaxanthin_3-1', 'enzyme_1', 'coq10_1']


def run(target) :
    if target == 'product':
        n = 0

        a = datetime.now()
        f = open('data/takecareof/takecareof-product-'+' '+str(datetime.now())+'.csv','w', newline='')
        csvWriter = csv.writer(f)
        csvWriter.writerow(
            [
                'product_name',
                'code_name',
                'subtitle',
                'symbol_label',
                'description',
                'amount_and_price',
                'assessment_text',
                'assessment_base',
                'nutrition_interaction',
                'label',
                'product_type',
                'dosage',
                'ingredients',
                'does_not_contain'
            ]
        )

        for product in products:
            n += 1
            print (str(n) + ':' + str(product))
            r.start(product)
            request = urllib.request.Request(HOST+product,None,headers) #The assembled request
            time.sleep(4)
            data = urllib.request.urlopen(request).read()

            soup = BeautifulSoup(data, 'lxml')
            body = soup.find('body')

            code_name = product
            product_name = body.find('h1', attrs={'class':'h0'}).get_text()
            subtitle = body.find('h3', attrs={'class': 'h4 subtitle'}).get_text()
            symbol_labels = body.find_all('div', attrs={'class': 'caps-label'})
            symbol_label = ''
            for item in symbol_labels: symbol_label += (str(item.get_text()) + ', ')
            description = body.find('div', attrs={'class': 'info-block'}).find('p').get_text()
            amount_and_price = body.find('p', attrs={'class': 'ginger'}).get_text()
            assessment_text = body.find('p', attrs={'class': 'align-left flex-order-first'}).get_text()
            assessment_base = body.find('div', attrs={'class': 'product-benefits__info-block'}).find('h4').get_text()
            nutrition_interactions = body.find_all('div', attrs={'class': 'accordion-item__title'})
            nutrition_interaction = ''
            for item in nutrition_interactions: nutrition_interaction += (str(item.get_text()) + ', ')
            labels = body.find_all('div', attrs={'class': 'picto-item__content'})
            label = ''
            for item in labels: label += (str(item.get_text()) + ', ')

            details = body.find_all('div', attrs={'class': 'info-block__box_border_thick'})
            product_type = details[0].find('h5').get_text()
            dosage = details[1].find('div', attrs={'class': 'box'}).get_text().replace('\n', ' ')
            ingredients = details[2].find('p', attrs={'class': 'ginger small'}).get_text()
            does_not_contain = details[3].find('p', attrs={'class': 'ginger small'}).get_text()

            this_product = [
                product_name,
                code_name,
                subtitle,
                symbol_label,
                description,
                amount_and_price,
                assessment_text,
                assessment_base,
                nutrition_interaction,
                label,
                product_type,
                dosage,
                ingredients,
                does_not_contain
            ]
            csvWriter.writerow(this_product)
            r.end(product)
        f.close()
    if target == 'ingredient':
        a = datetime.now()
        f = open('data/takecareof/takecareof-ingredient-'+' '+str(datetime.now())+'.csv','w', newline='')
        csvWriter = csv.writer(f)
        csvWriter.writerow(
            [
                'ingredient',
                'description'
            ])

        n = 0
        request = urllib.request.Request('https://takecareof.com/ingredients',None,headers) #The assembled request
        data = urllib.request.urlopen(request).read()

        soup = BeautifulSoup(data, 'lxml')
        body = soup.find('body')

        ingredient_list = body.find_all('div', attrs={'class':'ingredient'})
        name_list = []
        for ingredient in ingredient_list:
            n += 1
            name = ingredient.find('a', attrs={'class': 'ingredient__title'}).get_text()
            description = ingredient.find('p').get_text()
            name_l = name.lower()
            if name_l in name_list:
                continue
            elif name_l[:-1] in name_list:
                continue
            this_ingredient = [name, description]
            name_list.append(name_l)
            csvWriter.writerow(this_ingredient)
            print (str(n) + ' ' + str(name))
        f.close()
    if target == 'research':
        a = datetime.now()
        f = open('data/takecareof/takecareof-research-'+' '+str(datetime.now())+'.csv','w', newline='')
        csvWriter = csv.writer(f)
        csvWriter.writerow(
            [
                'name',
                'disclaimer',
                'description',
                'claim_title',
                'claim_description',
                'claim_reference'
            ])
        n = 0

        for product in products:
            request = urllib.request.Request('https://takecareof.com/research/'+product,None,headers) #The assembled request
            time.sleep(4)
            data = urllib.request.urlopen(request).read()

            soup = BeautifulSoup(data, 'lxml')
            body = soup.find('body')

            claims = body.find_all('div', attrs={'class': 'research-claim'})
            for i in range(0, len(claims)):
                n += 1
                name = body.find('div', attrs={'class': 'research__header'}).find('h1').get_text()
                disclaimer = body.find('div', attrs={'class': 'research__disclaimer'}).get_text()
                description = body.find('div', attrs={'class': 'research__description'}).get_text()
                claim_title = claims[i].find('h4', attrs={'class': 'research-claim__title'}).get_text()
                claim_description = claims[i].find('p', attrs={'class': 'research-claim__description'}).get_text()
                claim_references = claims[i].find_all('li', attrs={'class': 'reference'})
                this_research = [
                    name,
                    disclaimer,
                    description,
                    claim_title,
                    claim_description
                ]
                for r in range(0, len(claim_references)):
                    ref_title = claim_references[r].find('div', attrs={'class': 'reference__title'}).get_text()
                    ref_authors = claim_references[r].find('div', attrs={'class': 'reference__authors'}).get_text()
                    ref_journal = claim_references[r].find('div', attrs={'class': 'reference__journal'}).get_text()
                    ref_year = claim_references[r].find('div', attrs={'class': 'reference__year'}).get_text()
                    this_reference = [
                        ref_title,
                        ref_authors,
                        ref_journal,
                        ref_year
                    ]
                    this_research += this_reference

                csvWriter.writerow(this_research)
                print (str(n) + ' ' + str(name) + ' - ' + str(claim_title))
        f.close()
    if target == 'personalize':
        # personalize 부분은 전부 javascript에서 로딩하는 거라서 beautifulsoup으로 안 됨.
        questions_using_selection = [
            'experience',
            'vitamins-supplements-past',
            'number-vitamins-recommendation',
            'vitamins-supplements-how-often-adherence',
            'curious-currently-take-vitamins-supplements',
            'gender',
            'prenatal-postnatal-yes-no',
            'pregnancy-which-of-these',
            'why-vitamins-motivation',
            'topics',
            'most-important',
            'immunity-frequently-get-sick',
            'immunity-cold-like-symptoms',
            'immunity-traveling-plane',
            'immunity-planning-high-intensity',
            'brain-focus-trouble-multitasking',
            'brain-focus-trouble-focusing',
            'short-term-memory-concern',
            'is-your-stress',
            'do-you-have-bad-mood',
            'energy-trouble-sleeping',
            'energy-stress-fatigued',
            'skin-concerns',
            'family-history-osteoporosis',
            'digestion-concern',
            'digestion-bowel-movements',
            'heart-family-history-disease',
            'Any heart concerns?',
            'healthy-lifestyle',
            'fish',
            'meat',
            'fruits-vegetables',
            'dairy',
            'exercise',
            'female-alcohol-three-single-day',
            'male-alcohol-four-single-day',
            'exercise-muscle-recovery',
            'female-alcohol-seven-week',
            'male-alcohol-fourteen-week',
            'smoke',
            'eyes-computer-screen',
            'eyes-dry-symptoms',
            'medications-ssri',
            'allergies',
            'restrictions-diet',
            'values-traditional-eastern-medicine',
            'values-new-product-research',
            'how-did-you-hear-about-us'
        ]
        a = datetime.now()
        f = open('data/takecareof/takecareof-personalize-'+' '+str(datetime.now())+'.csv','w', newline='')
        csvWriter = csv.writer(f)
        csvWriter.writerow([
            'question_id',
            'option_count',
            'option_id'
            ])
        n = 0

        for question in questions_using_selection:
            request = urllib.request.Request('https://takecareof.com/survey/new?question='+question,None,headers) #The assembled request
            time.sleep(8)
            data = urllib.request.urlopen(request).read()

            soup = BeautifulSoup(data, 'lxml')
            body = soup.find('body')
            form = body.find('form')
            multiselect = body.find('div', attrs={'class': 'multiselect-component'})
            print (form.prettify())
            # options = body.select('div[data-response-identifer]')
            options = body.find_all('div', attrs={"data-response-identifer": True})
            question_set = [question, len(options)]
            for opt in options:
                question_set.append(opt['dataset']['responseIdentifer'])

            csvWriter.writerow(question_set)
            print (question_set)

r.start('main')
# run('product')
# run('ingredient')
# run('research')
# run('personalize')
r.end('main')


# # radio, checkbox
# items = document.querySelectorAll('div[data-response-identifer]'); option_ids = [];
# for (i=0; i<items.length; i++) {option_ids.push(items[i].dataset.responseIdentifer);} console.log(option_ids);
#
# # inputbox
# document.querySelector('.question-component').getAttribute('data-identifier')
