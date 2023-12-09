import requests, json, os, sys
from threading import Thread
import threading
from datetime import datetime
from time import strftime
from time import sleep
import random
camxuc=[]
dem=0


class Facebook:
	def __init__(self,cookie):
		self.cookie = cookie
		self.headers = {
			'authority': 'mbasic.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
			'cache-control': 'max-age=0',
			'cookie': cookie,
			'origin': 'https://www.facebook.com',
			'referer': 'https://www.facebook.com',
			'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			}
	def thongtin(self):
		try:
			url=requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).url
			home = requests.get(url,headers=self.headers).text
			self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten = home.split('<title>')[1].split('</title>')[0]
			self.user_id = cookie.split('c_user=')[1].split(';')[0]
			print(f'Tên Facebook: {ten} | ID: {self.user_id} ', end='')
			sys.stdout.flush()
		except:
			print('Không Get Được Thông Tin ! ')
			return 0
	def profile5(self):
		headers={
           	     'authority': 'www.facebook.com',
            	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          	      'accept-language': 'vi',
       	         'cookie': self.cookie,
           	     'sec-ch-prefers-color-scheme': 'light',
            	    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            	    'sec-ch-ua-mobile': '?0',
          	      'sec-ch-ua-platform': '"Windows"',
          	      'sec-fetch-dest': 'document',
           	     'sec-fetch-mode': 'navigate',
           	     'sec-fetch-site': 'none',
           	     'sec-fetch-user': '?1',
             	   'upgrade-insecure-requests': '1',
           	     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            	    'viewport-width': '1366',
          	 	 }
		data ={
					'av':self.user_id,
					'fb_dtsg':self.fb_dtsg,
					'jazoest':self.jazoest,
					'fb_api_caller_class':'RelayModern',
					'fb_api_req_friendly_name':'CometSettingsDropdownListQuery',
					'variables':'{"fetchTestUserProfileListCell":false,"includeHorizBadging":false,"inProfileSwitcherEntry":false,"inSimpleHeaderEntry":true,"scale":2}',
					'server_timestamps':'true',
					'doc_id':'8179507702122101',
				}
		try:
			a=requests.post('https://www.facebook.com/api/graphql/', headers=headers,data=data).json()
			get = a['data']['viewer']['actor']['profile_switcher_eligible_profiles']
			tong = get['count']
			data_pro5 = get['nodes']
			print(f'| {tong} Page Profile')
			return data_pro5
		except:
			print('\nKhông Tìm Thấy Page Profile !')
			exit()

	def View(self,story_url,id_page,name):
		cookie = self.cookie
		ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
		bucket_id = story_url.split('facebook.com/stories/')[1].split('/')[0]
		story_id = story_url.split(f'{bucket_id}/')[1].split('/')[0]
		headers = {
			'authority': 'www.facebook.com',
			'accept': '*/*',
			'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
			'cookie': ck_pro5,
			'origin': 'https://www.facebook.com',
			'referer': 'https://www.facebook.com',
			'sec-ch-prefers-color-scheme': 'dark',
			'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
		}
		data = {
			'av': id_page,
			'fb_dtsg': self.fb_dtsg,
			'jazoest': self.jazoest,
			'fb_api_caller_class': 'RelayModern',
			'fb_api_req_friendly_name': 'storiesUpdateSeenStateMutation',
			'variables': '{"input":{"bucket_id":"'+bucket_id+'","story_id":"'+story_id+'","actor_id":"'+id_page+'","client_mutation_id":"1"},"scale":1}',
			'server_timestamps': 'true',
			'doc_id': '5127393270671537',
		}
		try:
			xem = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
			check = xem['data']['direct_message_thread_update_seen_state']['story']['story_card_seen_state']['is_seen_by_viewer']
			print(f'[√] | {bucket_id} | VIEW | {id_page} | {name} |')
		except:
			print(f'[×] | {bucket_id} | ERROR | {id_page} | {name}')
			

while True:
	cookie=input ('Nhập Cookie Nick Cầm Page Profile: ')
	fb = Facebook(cookie)
	a=fb.thongtin()
	data_pro5 = fb.profile5()
	story_url = input('Nhập Link Story: ')
	try:
		bucket_id = story_url.split('facebook.com/stories/')[1].split('/')[0]
		story_id = story_url.split(f'{bucket_id}/')[1].split('/')[0]
	except:
		print('Link Story Gặp Lỗi !')
	for x in data_pro5:
		id_page=x['profile']['id']
		name=x['profile']['name']
		threading.Thread(target=fb.View,args=(story_url,id_page,name)).start()
