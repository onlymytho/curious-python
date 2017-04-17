
# Zenpy accepts an API token
creds = {
    'email' : 'zendesk@vingle.net',
    'token' : '38XqgKh2KHJl2NuP1KtzrJeZUkEUPlYd5gCI2CJu',
    'subdomain': 'vinglehelp'
}

from zenpy import Zenpy
import datetime

# Default
zenpy_client = Zenpy(**creds)


yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
today = datetime.datetime.now()

test_start_day = '2017-03-09'

for ticket in zenpy_client.search("tags:testers created_at>2017-03-09", type='ticket'):
    print (ticket.description)
