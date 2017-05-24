
# url = 'https://vinglehelp.zendesk.com/api/v2/tickets/{ticket_id}/comments.json'
# TOKEN = 'YLixcuvGNG0QRUJdSxKGaBQ5CW4vUuynj7a1YlAo'

# Command to get tickets from testers : curl -u zendesk@vingle.net/token:YLixcuvGNG0QRUJdSxKGaBQ5CW4vUuynj7a1YlAo https://vinglehelp.zendesk.com/api/v2/search.json?query=type:ticket tags:testers

from JsonHandler import JsonHandler
import io
from datetime import datetime

CONFIG_FILE="./data/testers_tickets/testers_tickets.json"



testers_tickets = JsonHandler.OpenJsonFileConvertToDict(CONFIG_FILE)

a = ''
for results in testers_tickets['results']:
    if any(x for x in JsonHandler(results).getValue('tags') if 'Korean'):
        a = a+(JsonHandler(results).getValue('description'))+','
    else:
        continue

print ('\nFinished parsing.')

export_file_name = 'data/testers_tickets/testers_tickets'+' '+str(datetime.now())+'.csv'
with io.open(export_file_name, 'w', encoding='utf-8') as f:
  f.write(a)

print ('File Exported as ' + "'" + export_file_name + "'" + '\n')
