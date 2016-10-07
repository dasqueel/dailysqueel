import twitter
from pymongo import MongoClient
from dateutil.parser import *
import datetime
import pytz

api = twitter.Api(consumer_key='QiNQsfq7VIxrftmuddCEvtmBB',
                  consumer_secret='KC9oBtsoBuiwZcvslVEFlWePx0AiLIaO8WFI8yEQ5fHdLZSjuq',
                  access_token_key='411707002-Q9t3EVZLcqiLCEsgQVMJsG2OCdVt1RoYWkBQJzfM',
                  access_token_secret='K1F1soxnY19ccoJyNKwpK9LFfm62z6UHCIOCeFfhMOlco')

def getTeamTweets(beatWriters):
	tweets = []
	for user in beatWriters:
		statuses = api.GetUserTimeline(screen_name=user,include_rts=False, count=15)
		for s in statuses[::-1]:
			urls = []
			for url in s.urls: urls.append(url.url)
			tweets.append({'tweet':s.text,'created_at':parse(s.created_at),'author':s.user.name,'urls':urls})

	tweets.sort(key=lambda item:item['created_at'], reverse=True)
	now = datetime.datetime.now()

	#get mins ago for tweets
	for tweet in tweets:
		fmt = '%Y-%m-%d %H:%M:%S'
		tweetTime = tweet['created_at']
		now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
		d1 = datetime.datetime.strptime(str(tweetTime)[:-6], fmt)
		d2 = datetime.datetime.strptime(str(now)[:-13], fmt)
		minsAgo = (d2-d1).total_seconds()/60
		tweet['minsAgo'] = int(round(minsAgo))

	return tweets
