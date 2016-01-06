import json
import os
import glob
from datetime import datetime, tzinfo
import pytz
import codecs

for filename in glob.glob('rus*'):
	with open(filename, encoding='utf-8-sig') as data_file:    
		
		data = json.load(data_file)
		if (data['entities']['urls']):
                        normalized_urls = data['entities']['urls'][0]['expanded_url']
		else:
                        normalized_urls = ''
		if (data['entities']['hashtags']):
			normalized_hashtags = data['entities']['hashtags'][0]['text']
		else:
			normalized_hashtags = ''
		
		fmt = '%Y-%m-%dT%H:%M:%SZ'
		temp = datetime.strptime(data['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
		normalized_date = temp.strftime(fmt) 

	normalized_filename = '../normalized_tweets/norm_'+str(filename)
	with open(normalized_filename,'a') as outfile:
		outfile.write('[');
		json.dump({'created_at':normalized_date,'id':data['id'],'tweet_urls':normalized_urls,'tweet_hashtags':normalized_hashtags,'text_ru':data['text'],'lang': data['lang']}, outfile)
		outfile.write(']');

