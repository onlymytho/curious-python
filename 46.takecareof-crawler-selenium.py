from selenium import webdriver
# 아래 코드들을 import 해 줍시다.
from selenium.webdriver.common.by import By
# WebDriverWait는 Selenium 2.4.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv
import Record as r



r.start('main')

preferences = webdriver.ChromeOptions()
# preferences.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
preferences.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
driver = webdriver.Chrome('/Users/onlymytho/python/curious-python/bin/chromedriver', chrome_options=preferences)

question_list = [
    ['first_name','inputbox'],
    ['experience','radio'],
    ['vitamins-supplements-past','radio'],
    ['number-vitamins-recommendation','radio'],
    ['vitamins-supplements-how-often-adherence','radio'],
    ['curious-currently-take-vitamins-supplements','radio'],
    ['gender','radio'],
    ['age','inputbox'],
    ['prenatal-postnatal-yes-no','radio'],
    ['location','inputbox'],
    ['pregnancy-which-of-these','radio'],
    ['why-vitamins-motivation','radio'],
    ['topics','checkbox'],
    ['most-important','radio'],
    ['email','inputbox'],
    ['family-history-osteoporosis','radio'],
    ['brain-focus-trouble-multitasking','radio'],
    ['brain-focus-trouble-focusing','radio'],
    ['short-term-memory-concern','radio'],
    ['digestion-concern','radio'],
    ['digestion-bowel-movements','radio'],
    ['energy-trouble-sleeping','radio'],
    ['energy-stress-fatigued','radio'],
    ['heart-family-history-disease','radio'],
    ['Any heart concerns?','checkbox'],
    ['immunity-frequently-get-sick','radio'],
    ['immunity-cold-like-symptoms','radio'],
    ['immunity-traveling-plane','radio'],
    ['immunity-planning-high-intensity','radio'],
    ['skin-concerns','checkbox'],
    ['is-your-stress','radio'],
    ['do-you-have-bad-mood','radio'],
    ['healthy-lifestyle','radio'],
    ['fish','radio'],
    ['meat','radio'],
    ['fruits-vegetables','radio'],
    ['dairy','radio'],
    ['exercise','radio'],
    ['female-alcohol-three-single-day','radio'],
    ['male-alcohol-four-single-day','radio'],
    ['exercise-muscle-recovery','radio'],
    ['female-alcohol-seven-week','radio'],
    ['male-alcohol-fourteen-week','radio'],
    ['smoke','radio'],
    ['eyes-computer-screen','radio'],
    ['eyes-dry-symptoms','radio'],
    ['medications-ssri','radio'],
    ['allergies','checkbox'],
    ['restrictions-diet','checkbox'],
    ['values-traditional-eastern-medicine','radio'],
    ['values-new-product-research','radio'],
    ['how-did-you-hear-about-us','radio'],
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

for question in question_list:
    print (question)
    driver.get('https://takecareof.com/survey/new?question=' + question[0])
    print ('https://takecareof.com/survey/new?question=' + question[0])

    try:
        # WebDriverWait와 .until 옵션을 통해 우리가 찾고자 하는 HTML 요소를
        # 기다려 줄 수 있습니다.
        if question[1] == 'radio' or question[1] == 'checkbox':
            print ('multiselect type')
            checker = WebDriverWait(driver, 10) \
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-response-identifer]")))

            data = driver.page_source
            soup = BeautifulSoup(data, 'lxml')
            body = soup.find('body')
            # form = body.find('form')
            # multiselect = body.find('div', attrs={'class': 'multiselect-component'})
            options = body.select('div[data-response-identifer]')
            question_set = [question, len(options)]
            for opt in options:
                question_set.append(opt['dataset']['responseIdentifer'])

        elif question[1] == 'inputbox':
            print ('inputbox type')
            checker = WebDriverWait(driver, 10) \
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, ".question-component")))

            data = driver.page_source
            soup = BeautifulSoup(data, 'lxml')
            body = soup.find('body')
            # form = body.find('form')
            # multiselect = body.find('div', attrs={'class': 'multiselect-component'})
            options = body.select('.question-component')
            question_set = [question[0], len(options)]
            for opt in options:
                question_set.append(opt['data-identifier'])
        else:
            pass

        csvWriter.writerow(question_set)
        print (question_set)

    except socket.timeout as e:
        print ("timeout")
    except http.client.HTTPException as e:
        print ("HTTPException")
    except http.client.RemoteDisconnected as e:
        print ("RemoteDisconnected")
    except ConnectionResetError as e:
        print ("ConnectionResetError")
    except BrokenPipeError as e:
        print ("BrokenPipeError")
    finally:
        driver.quit()
r.end('main')
