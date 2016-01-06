#! usr/bin/env python

import sys
import os
from twython import Twython
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

slug_name = sys.argv[1]
owner_name = ""
tweet_file_dir_path = ""

twitter = Twython(consumer_key, consumer_secret, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(consumer_key, access_token=ACCESS_TOKEN)

result_list = twitter.get_list_statuses(slug=slug_name,owner_screen_name='',include_rts='false',count='75')
for result in result_list:
	file_name = os.getenv('HOME')+ tweet_file_dir_path +slug_name[7:10]+'_'+str(result['id'])+'.json'
	with open(file_name, 'w') as outfile:
		json.dump(result, outfile)

