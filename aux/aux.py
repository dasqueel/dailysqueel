import twitter
from dateutil.parser import *
import datetime
import pytz

api = twitter.Api(consumer_key='<your consumer key>',
                  consumer_secret='<your consumer secret>',
                  access_token_key='<your access token key>',
                  access_token_secret='<your access token secret>')

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
