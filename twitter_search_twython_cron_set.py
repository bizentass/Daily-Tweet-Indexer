from crontab import CronTab

cron = CronTab()

job_english = cron.new(command = 'nohup python3 /Users/bronco/Documents/Code/CSE_535/twitter_scrapper/twitter_search_twython.py sports-english', comment = 'job_english')
job_german = cron.new(command = 'nohup python3 /Users/bronco/Documents/Code/CSE_535/twitter_scrapper/twitter_search_twython.py sports-german', comment = 'job_german')
job_russian = cron.new(command = 'nohup python3 /Users/bronco/Documents/Code/CSE_535/twitter_scrapper/twitter_search_twython.py sports-russian', comment = 'job_russian')

job_english.minute.every(10)
job_german.minute.every(10)
job_russian.minute.every(10)
