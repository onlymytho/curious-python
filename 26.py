import requests
from instagram.client import InstagramAPI

# auth 파일에서 airbnb_my_user_api_key 받아오기
import sys
sys.path.insert(0, "/Users/onlymytho/python")
import auth

token = auth.instagram_access_token
secret = auth.instagram_client_secret
media_id = 'BTiPAOYlmeQ'
r = requests.post(url='https://api.instagram.com/v1/media/%s/comments?access-token='+token+'&text="This is my comment"') # % media_id, data={
#     'access-token':token,
#     'text':'This is my comment'
# })
#
print (r.text)



# api = InstagramAPI(access_token=token, client_secret=secret)
# print (api.user_recent_media(user_id="onlymytho", count=10))
# recent_media, next_ = api.user_recent_media(user_id="onlymytho", count=10)
# for media in recent_media:
#    print (media.caption.text)
