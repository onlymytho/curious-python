import requests
import json
import csv
import io
from datetime import datetime


my_user_api_key = 'd306zoyjsyarp7ifhu67rjxn52tv0t20'
sample_user_api_key = '3092nxybyb0otqw18e8nh5nty'


end_point_url = 'https://api.airbnb.com/v2/search_results'

r = requests.get(end_point_url +
                 '?client_id=d306zoyjsyarp7ifhu67rjxn52tv0t20'+
                 '&locale=ko'+
                 '&currency=USD'+
                 '&_format=for_search_results_with_minimal_pricing'+
                 '&_limit=50'+
                 '&_offset=0'+
                 '&guests=2'+
                 '&ib=false'+
                 '&location=Yeonnam'+
                 '&min_bathrooms=0'+
                 '&min_bedrooms=0'+
                 '&min_beds=1'+
                 '&min_num_pic_urls=5'+
                 '&price_max=150'+
                 '&price_min=0'+
                 '&sort=1'+
                 '&user_lat=37.560512'+
                 '&user_lng=126.908462')

print (r)

datadict = r.json()
datajson = json.dumps(datadict, indent=4)
# print (datajson)

with io.open('airbnb_listings/airbnb_listings'+' '+str(datetime.now())+'.json', 'w', encoding='utf-8') as f:
  f.write(datajson)

# x = datajson
# x = json.loads(x)
#
# #f = csv.writer(open("test.csv", "wb+"))
# f = open('airbnb_listings/airbnb_listings '+' '+str(datetime.now())+'.csv','w', newline='')
# csvWriter = csv.writer(f)
#
# # Write CSV Header, If you dont need that, remove this line
# #f.writerow(["pk", "model", "codename", "name", "content_type"])
#
#
# for x in x:
#     csvWriter.writerow([x["metadata"]["geography"]["lat"], x["metadata"]["geography"]["lng"]])

# def SearchListings($data, $token) :
# 	# Send the request
# 	data = requests.api.get('https://api.airbnb.com/v2/search_results', client_id='3092nxybyb0otqw18e8nh5nty')SendRequest('v2/search_results', $token, FALSE, $data, TRUE);
# 	return @json_decode($data['response'], TRUE);
