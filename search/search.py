from django.conf import settings
from requests_oauthlib import OAuth1Session
import oauth2 as oauth

import base64
import requests
import urllib.parse
import pprint

class Twitter:
	CONSUMER_KEY = settings.CONSUMER_KEY
	CONSUMER_SECRET = settings.CONSUMER_SECRET
	ACCESS_TOKEN = settings.ACCESS_TOKEN
	ACCESS_SECRET = settings.ACCESS_SECRET
	twitter = OAuth1Session(client_key=CONSUMER_KEY,
							client_secret=CONSUMER_SECRET,
							resource_owner_key=ACCESS_TOKEN,
							resource_owner_secret=ACCESS_SECRET)



	def get_bearer_token(self):
		# enconde consumer key
		consumer_key = urllib.parse.quote(self.CONSUMER_KEY)
		# encode consumer secret
		consumer_secret = urllib.parse.quote(self.CONSUMER_SECRET)
		# create bearer token
		bearer_token = consumer_key + ':' + consumer_secret
		# base64 encode the token
		base64_encoded_bearer_token = base64.b64encode(bearer_token.encode('utf-8'))
		# set headers
		auth_token_url = 'https://api.twitter.com/oauth2/token'
		headers = {
			"Authorization": "Basic " + base64_encoded_bearer_token.decode('utf-8') + "",
			"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
			"Content-Length": "29"}

		response = requests.post(auth_token_url, headers=headers, data={'grant_type': 'client_credentials'})
		to_json = response.json()
		print(to_json)
		print("token_type = %s\naccess_token  = %s" % (to_json['token_type'], to_json['access_token']))

		return to_json['access_token']

	def search(self, access_token):
		url = 'https://api.twitter.com/1.1/tweets/search/30day/development.json'
		headers = {'Authorization': 'Bearer %s' % access_token,
				   'Content-Type': 'application/json'
		 }
		body = {
				'query': "essay",
				'maxResults': 10,
		}
		print(url, headers, body)

		return self.twitter.post(url, json=body, headers=headers)


# curl -X POST "https://api.twitter.com/1.1/tweets/search/30day/development.json" -d '{"query":"(snow OR sleet OR hail OR (freezing rain)) has:images","maxResults":10}' -H "Authorization: Bearer 3156199463-9AMhUNuekvuYk2CDl1U5BvIKY5U1cpoWP8kFUDz"


# curl  "https://api.twitter.com/1.1/tweets/search/:product/:label.json?query=TwitterDev%20%5C%22search%20api%5C%22&maxResults=500" -H "Authorization: Bearer 3156199463-tkJrpr3yoPZb423WhAT0f41AhQjxUSrrDWptyZ1"


# CONSUMER_KEY = settings.CONSUMER_KEY
#     CONSUMER_SECRET = settings.CONSUMER_SECRET
#     ACCESS_TOKEN = settings.ACCESS_TOKEN
#     ACCESS_SECRET = settings.ACCESS_SECRET
#     twitter = OAuth1Session(CONSUMER_KEY,
#                             client_secret=CONSUMER_SECRET,
#                             resource_owner_key=ACCESS_TOKEN,
#                             resource_owner_secret=ACCESS_SECRET)
#     def register_crc(self):
#         webhook_endpoint = urllib.parse.quote_plus('https://44c3b65c.ngrok.io/api/crc_callback')
#         url = 'https://api.twitter.com/1.1/account_activity/all/notifier/webhooks.json?url={}'.format(
#             webhook_endpoint)
#         return self.twitter.post(url)

#     def active_webhooks(self):
#         url = 'https://api.twitter.com/1.1/account_activity/all/webhooks.json'
#         headers = {'Authorization': 'Bearer %s' % self.ACCESS_TOKEN }
#         res = self.twitter.get(url, headers=headers)
#         one = res.json()['environments']
#         two = one[0]
#         three = two['webhooks']
#         four = three[0]

#         return res.json()






# import requests
# from requests.auth import HTTPBasicAuth
# import pprint
# import datetime
# import base64

# class lipanampesa:
#     consumer_key = settings.CONSUMER_KEY
#     consumer_secret = settings.CONSUMER_SECRET
#     clients_credentials_url = settings.CLIENTS_CREDENTIALS_URL
#     base_url = settings.BASE_URL

#     def get_access_token(self):
#         r = requests.get(self.clients_credentials_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
#         access_token = r.json()["access_token"]
#         return access_token

#     def register_url(self, access_token):
#         url_register = settings.REGISTER_URL
#         headers = {
#             'Authorization': 'Bearer %s' % access_token,
#             'Content-Type': 'application/json'
#         }
#         body = {
#             "ShortCode": "174379",
#             "ResponseType": "complete",
#             "ConfirmationURL": "%s/confirmation" % self.base_url ,
#             "ValidationURL": "%s/validation" % self.base_url,
#         }
#         print(headers, body, url_register)

#         response = requests.post(url_register, json=body, headers=headers)
#         return response.json()

#     def pay(self, access_token):
#         timestamp = str(int(datetime.datetime.now().timestamp()))
#         shortcode = str(settings.SHORTCODE)
#         passkey = settings.PASSKEY

#         toencode = (timestamp+shortcode+passkey).encode('utf')
#         print(toencode)

#         encoded = base64.b64encode(toencode)
#         password = encoded.decode('utf')

#         # Json
#         lipaonline_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

#         headers = {
#             'Authorization': 'Bearer %s' % access_token,
#             'Content-Type': 'application/json'
#         }

#         body = {
#             "BusinessShortCode": "174379",
#             "Password": password,
#             "Timestamp": timestamp,
#             "TransactionType": "CustomerPayBillOnline",
#             "Amount": "10",
#             "PartyA": "254717771518",
#             "PartyB": "174379",
#             "PhoneNumber": "254717771518",
#             "CallBackURL": "%s/validation" % self.base_url,
#             "AccountReference": "account",
#             "TransactionDesc": "test" ,
#         } 
#         print(lipaonline_url, body, headers)

#         response = requests.post(lipaonline_url, json=body, headers=headers)
        














