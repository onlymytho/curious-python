import requests
import json
import io
from datetime import datetime


class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None
        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [ v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)
            if not val:
                break;
        return val


# url = 'http://openapi.seoul.go.kr:8088/sample/json/ListPublicPhysicalPlant/1/5/'
#
# r = requests.get(url)

url = '/openapi/ListPublicPhysicalPlant/ListPublicPhysicalPlant 2017-03-27 00/53/47.372328.json'
r = requests.get(url)
print(r)

# datadict = r.json()

# row = datadict['ListPublicPhysicalPlant']['row']
# print (row['TEL'])

# datajson = json.dumps(datadict, indent=4)
# print (datajson)

# with io.open('openapi/ListPublicPhysicalPlant/ListPublicPhysicalPlant'+' '+str(datetime.now())+'.json', 'w', encoding='utf-8') as f:
#   f.write(datajson)


# for item in animals:
