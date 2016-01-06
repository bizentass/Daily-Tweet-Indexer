# Daily-Tweet-Indexer

To Extract Tweets
	
	1. The code here assumes that the user has created a list in twitter and has included all the twitter handles that he wants to track in that list. The lists are divided by language, for example the russian list contains russian twitter handles.

	2.In twitter_search_twython.py input the Consumer Key, Consumer Secret Key, Access Token and Access Secret Token in the appropriate fields. Also input your user name (this is also described in the Twython API usage link).

	3. Since the tweets are divided by language, input the language as an argument while running the python file.

	4. Specify the directory where you want to save the tweets in the variable tweet_file_dir_path.


To Normalize Tweets

	1. Apache's Solr expects the data to be in a predetermined format and also we usually remove redundant data, so to do that we need to normalize the tweets, this is handled by the file - twitter_search_normalize.py

	2. Since my requirement was to index the data according to language, I had to read russian tweets separately and index them under text_ru. The language specific changes are to be made in line no. 8 and line no. 28 of twitter_search_normalize.py.

To Set Up a Cron Job

	1. Using the python-crontab 2.0.1 API I created cronjobs for three languages running every 10 minutes.

	2. Using the cron.new() method run the twitter_search_twython.py along with the list names as arguments (specified as sports-german, sports-english etc. here)

	Modify this to suit your requirements as necessary. Thank you! 