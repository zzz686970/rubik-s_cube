import requests
import pandas as pd



# def flatten(d):
#     out = []
#     for key, val in d.items():
#         if isinstance(val, dict):
#             val = [val]
#         if isinstance(val, list):
#             for subdict in val:
#                 deeper = flatten(subdict)
#                 out.extend([val2 for val2 in deeper])
#         else:
#             out.append(val)
#     return out

# def flatten_json(y):
#     out = {}

#     def flatten(x, name=''):
#         if type(x) is dict:
#             for a in x:
#                 flatten(x[a], name + a + '_')
#         elif type(x) is list:
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + '_')
#                 i += 1
#         else:
#             out[name[:-1]] = x

#     flatten(y)
#     return out

# x = {'f': [{'v': '6781915834426845575'}, {'v': '7'}, {'v': '1551918776'}, {'v': '1551918776'}, {'v': '20190307'}, {'v': None}, {'v': '1'}, {'v': None}, {'v': None}, {'v': None}, {'v': None}, {'v': None}, {'v': None}, {'v': None}, {'v': None}, {'v': '(direct)'}, {'v': '(none)'}, {'v': 'GoogleAnalytics'}, {'v': 'iOS'}, {'v': 'true'}, {'v': 'tablet'}, {'v': 'Canada'}, {'v': [{'v': {'f': [{'v': '1'}, {'v': '0'}, {'v': '1'}, {'v': 'false'}, {'v': None}, {'v': None}, {'v': 'EVENT'}, {'v': None}, {'v': None}, {'v': None}, {'v': 'ios.shop_list'}, {'v': 'shop_list.loaded'}, {'v': None}, {'v': None}, {'v': [{'v': {'f': [{'v': '18'}, {'v': '-73.55298483453905'}]}}, {'v': {'f': [{'v': '11'}, {'v': 'shop_list'}]}}, {'v': {'f': [{'v': '15'}, {'v': 'CA'}]}}, {'v': {'f': [{'v': '19'}, {'v': '45.52945781674692'}]}}, {'v': {'f': [{'v': '16'}, {'v': ''}]}}]}]}}]}]}
# d = flatten_json(x)
# print(d, len(d))

headers = {
	'accept': 'application/json, text/plain, */*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7',
	'authorization': 'SAPISIDHASH 1600785216_6fa57daa9aabc3e66fad7d8fb300c839c3de367c',
	'cache-control': 'no-cache',
	'cookie': 'HSID=AzOe_pHw53BeNyrGZ; SSID=AV9QevYpv1mEUnGJr; APISID=y2QiLwlfzfWpnymm/Ai6DiwEr9UC8tlFbz; SAPISID=JkwORNShkc6-7MBM/AfrDt0neBI6-qzwOM; __Secure-3PAPISID=JkwORNShkc6-7MBM/AfrDt0neBI6-qzwOM; CONSENT=YES+SG.en+; SID=0wf8e-rs8zHQVyuuW3yFsl1O6yUubQPBbrUXh2gDAgnvqdy_diqhunbTSmH3A5oLW6fM2w.; __Secure-3PSID=0wf8e-rs8zHQVyuuW3yFsl1O6yUubQPBbrUXh2gDAgnvqdy_JFy80UFyarCkgPiYlHQmYA.; SEARCH_SAMESITE=CgQI2ZAB; 1P_JAR=2020-09-22-10; NID=204=CusQLYs87IR09bzPYRsyTGl2nDQd_idMW6kYWzUg4t7aEZkHxyKR03dYeYAfC7unYQrcWF378a3nCu0qqSvvN7tzlodR_EXhW3scZTo_sV7imhR0WmP8Bz0Ii_dD-Rz7RaZAuC-DQsdEsFc0nH30SrLaR9ocGWekkI-SeyNnhMBie0GHQfYWkyWVBCnU-mPNEYC1mx-7ARlwkxUUJFEvj-ZFwLimXIR_jYhho-dhHD5mg1TtgKvwIhc6ik9FnHr6vsHWL7lAjtIZhIWnKZJ1vRhDHjEgmkuT7TT2l33o3q_s1ll33A; SIDCC=AJi4QfFKsoZj1RNpCYxIt78XtqeTVJMeZ5jQtd0TptLEqYm08vK9cn7_MHlOBcMC6s421Hcw9Zs; __Secure-3PSIDCC=AJi4QfG6QOfV00rS8RZC7seE1N37hvPbMfZ2mpXQzIFlM6R2q-1vmZQVk8oyDPuwRTPWiHDWzwg',
	'dnt': '1',
	'origin': 'https://console.cloud.google.com',
	'pragma': 'no-cache',
	'referer': 'https://console.cloud.google.com/',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
	'x-client-data': 'CJO2yQEIpbbJAQjEtskBCKmdygEIlqzKAQiZtcoBCPbHygEI58jKAQjpyMoBCKvJygEI9c3KAQj72MoB',
	'x-goog-authuser': '0',
}


cnt = 0 
result = []

url = "https://clients6.google.com/bigquery/v2internal/projects/dhh-analytics-hiringspace/datasets/GoogleAnalyticsSample/tables/ga_sessions_export/data"
# url2 = "https://clients6.google.com/bigquery/v2internal/projects/dhh-analytics-hiringspace/datasets/GoogleAnalyticsSample/tables/ga_sessions_export/data?key=AIzaSyCI-zsRP85UVOi0DjtiCwWBwQ1djDy741g&maxResults=13&startIndex=195"
params = {
	'key':'AIzaSyCI-zsRP85UVOi0DjtiCwWBwQ1djDy741g',
	'maxResults':10,
}

resp = requests.get(url, params = params, headers = headers,)
resp.raise_for_status()
# print(resp.json())

total_counts = int(resp.json().get('totalRows'))
pageToken = resp.json().get('pageToken')
for idx, row in enumerate(resp.json()['rows'], 1):
	# print(row)
	temp = [idx]
	temp.append(flatten(row))
	# print(temp)
	# print(temp)
	# for el in row.get('f'):
	# 	if isinstance(el, dict):
	# 		temp.append(el.get('v'))
	# 	elif isinstance(el, list):

	# temp = [idx] + [el.get('v') for el in row.get('f') if ]
	# result.append(temp)

df = pd.DataFrame(result)
df.to_csv('ga_sessions_export.csv', index = False, header = False)

while cnt < 20:
	result = []
	params.update({'pageToken': pageToken})
	params.update({'startIndex': cnt})
	resp = requests.get(url, params = params, headers = headers,)
	pageToken = resp.json().get('pageToken')
	resp.raise_for_status()
	print("\n**********************************\n")
	# print(resp.json())
	for idx, row in enumerate(resp.json()['rows'], cnt+1):
		temp = [idx] + [el.get('v') for el in row.get('f')]
		# print(temp)
		result.append(temp)
	cnt += len(resp.json()['rows'])


	df = pd.DataFrame(result)
	df.to_csv('ga_sessions_export.csv', index = False, mode='a', header=False)

# df.columns = ['Row','fullvisitorid','visitNumber','visitId','visitStartTime','date','visits','hits','timeOnSite','transactions','transactionRevenue','newVisits','screenviews','uniqueScreenviews','timeOnScreen','totalTransactionRevenue','source','medium','browser','operatingSystem','isMobile','deviceCategory','country','hit.hitNumber','hit.time','hit.hour','hit.isInteraction','hit.isEntrance','hit.isExit','hit.type','hit.name','hit.landingScreenName','hit.screenName','hit.eventCategory','hit.eventAction','hit.eventLabel','hit.transactionId','hit.customDimensions.index','hit.customDimensions.value']



