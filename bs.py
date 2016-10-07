import flask
from flask import *
from pymongo import MongoClient
from aux.dc import *
from aux.aux import *
from bs4 import BeautifulSoup

#connect to mongo
client = MongoClient('localhost')
bsDb = client.battlesqueel

teamObjs = [{"name": "minnesota", "depthChartUrl": "ourlads.com/nfldepthcharts/depthchart/min", "twitter": ["arifhasannfl", "purplebuckeye", "eric_j_thompson", "kjsegall", "wludford", "infraren"], "abbr": "min", "sbnation": "dailynorseman.com", "_id": {"$oid": "57a2c396bab0044fd5219102"}, "nickname": "vikings"}, {"name": "green bay", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/gb", "twitter": ["BobMcGinn", "byryanwood"], "abbr": "gb", "sbnation": "acmepackingcompany.com", "_id": {"$oid": "57a6f49f366a35226a3c8f1f"}, "nickname": "packers"}, {"name": "detroit", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/det", "twitter": ["davebirkett", "ttwentyman"], "abbr": "det", "sbnation": "prideofdetroit.com", "_id": {"$oid": "57a6f49f366a35226a3c8f20"}, "nickname": "lions"}, {"name": "chicago", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/chi", "twitter": ["BradBiggs"], "abbr": "chi", "sbnation": "windycitygridiron.com", "_id": {"$oid": "57a6f49f366a35226a3c8f21"}, "nickname": "bears"}, {"name": "carolina", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/car", "twitter": ["josephperson"], "abbr": "car", "sbnation": "catscratchreader.com", "_id": {"$oid": "57a6f49f366a35226a3c8f22"}, "nickname": "panthers"}, {"name": "new orleans", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/no", "twitter": ["MikeTriplett", "nick_underhill"], "abbr": "no", "sbnation": "canalstreetchronicles.com", "_id": {"$oid": "57a6f49f366a35226a3c8f23"}, "nickname": "saints"}, {"name": "tampa bay", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/tb", "twitter": ["gregauman", "nFLSTROUD"], "abbr": "tb", "sbnation": "bucsnation.com", "_id": {"$oid": "57a6f49f366a35226a3c8f24"}, "nickname": "buccaneers"}, {"name": "atlanta", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/atl", "twitter": ["DOrlandoAJC", "vxmcclure23"], "abbr": "atl", "sbnation": "thefalcoholic.com", "_id": {"$oid": "57a6f49f366a35226a3c8f25"}, "nickname": "falcons"}, {"name": "new york giants", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/nyg", "twitter": ["NYPost_Schwartz"], "abbr": "nyg", "sbnation": "bigblueview.com", "_id": {"$oid": "57a6f49f366a35226a3c8f26"}, "nickname": "giants"}, {"name": "washington", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/was", "twitter": ["MikeJonesWaPo", "john_keim"], "abbr": "was", "sbnation": "hogshaven.com", "_id": {"$oid": "57a6f49f366a35226a3c8f27"}, "nickname": "redskins"}, {"name": "dallas", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/dal", "twitter": ["fishsports"], "abbr": "dal", "sbnation": "bloggingtheboys.com", "_id": {"$oid": "57a6f49f366a35226a3c8f28"}, "nickname": "cowboys"}, {"name": "philadelphia", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/phi", "twitter": ["JimmyKempski", "zberm"], "abbr": "phi", "sbnation": "bleedinggreennation.com", "_id": {"$oid": "57a6f49f366a35226a3c8f29"}, "nickname": "eagles"}, {"name": "san francisco", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/sf", "twitter": ["MaioccoCSN", "mattbarrows"], "abbr": "sf", "sbnation": "ninersnation.com", "_id": {"$oid": "57a6f49f366a35226a3c8f2a"}, "nickname": "49ers"}, {"name": "seattle", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/sea", "twitter": ["gbellseattle", "bcondotta", "SheilKapadia"], "abbr": "sea", "sbnation": "fieldgulls.com", "_id": {"$oid": "57a6f49f366a35226a3c8f2b"}, "nickname": "seahawks"}, {"name": "los angeles", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/ram", "twitter": ["jthom1", "MylesASimmons"], "abbr": "ram", "sbnation": "turfshowtimes.com", "_id": {"$oid": "57a6f49f366a35226a3c8f2c"}, "nickname": "rams"}, {"name": "arizona", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/arz", "twitter": ["kentsomers", "cardschatter"], "abbr": "arz", "sbnation": "revengeofthebirds.com", "_id": {"$oid": "57a6f49f366a35226a3c8f2d"}, "nickname": "cardinals"}, {"name": "pittsburgh", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/pit", "twitter": ["C_AdamskiTrib", "DustinDopirak"], "abbr": "pit", "sbnation": "behindthesteelcurtain.com", "_id": {"$oid": "57a6f49f366a35226a3c8f2e"}, "nickname": "steelers"}, {"name": "cincinnati", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/cin", "twitter": ["pauldehnerjr", "jaymorrisoncmg"], "abbr": "cin", "sbnation": "cincyjungle.com", "_id": {"$oid": "57a6f49f366a35226a3c8f2f"}, "nickname": "bengals"}, {"name": "baltimore", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/bal", "twitter": ["jeffzrebiecsun", "RavensInsider"], "abbr": "bal", "sbnation": "baltimorebeatdown.com", "_id": {"$oid": "57a6f49f366a35226a3c8f30"}, "nickname": "ravens"}, {"name": "cleveland", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/cle", "twitter": ["MaryKayCabot", "NateUlrichABJ"], "abbr": "cle", "sbnation": "dawgsbynature.com", "_id": {"$oid": "57a6f49f366a35226a3c8f31"}, "nickname": "browns"}, {"name": "indianapolis", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/ind", "twitter": ["mchappell51", "HolderStephen"], "abbr": "ind", "sbnation": "stampedeblue.com", "_id": {"$oid": "57a6f49f366a35226a3c8f32"}, "nickname": "colts"}, {"name": "jacksonville", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/jax", "twitter": ["ryanohalloran"], "abbr": "jax", "sbnation": "bigcatcountry.com", "_id": {"$oid": "57a6f49f366a35226a3c8f33"}, "nickname": "jaguars"}, {"name": "houston", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/hou", "twitter": ["AaronWilson_NFL"], "abbr": "hou", "sbnation": "battleredblog.com", "_id": {"$oid": "57a6f49f366a35226a3c8f34"}, "nickname": "texans"}, {"name": "tennessee", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/ten", "twitter": ["terrymc13", "jwyattsports"], "abbr": "ten", "sbnation": "musiccitymiracles.com", "_id": {"$oid": "57a6f49f366a35226a3c8f35"}, "nickname": "titans"}, {"name": "new england", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/ne", "twitter": ["mikereiss", "BenVolin"], "abbr": "ne", "sbnation": "patspulpit.com", "_id": {"$oid": "57a6f49f366a35226a3c8f36"}, "nickname": "patriots"}, {"name": "miami", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/mia", "twitter": ["JamesWalkerNFL"], "abbr": "mia", "sbnation": "thephinsider.com", "_id": {"$oid": "57a6f49f366a35226a3c8f37"}, "nickname": "dolphins"}, {"name": "buffalo", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/buf", "twitter": ["JoeBuscaglia", "ChrisTrapasso"], "abbr": "buf", "sbnation": "buffalorumblings.com", "_id": {"$oid": "57a6f49f366a35226a3c8f38"}, "nickname": "bills"}, {"name": "new york jets", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/nyj", "twitter": ["BrianCoz", "KMart_LI", "RichCimini", "darrylslater"], "abbr": "nyj", "sbnation": "ganggreennation.com", "_id": {"$oid": "57a6f49f366a35226a3c8f39"}, "nickname": "jets"}, {"name": "denver", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/den", "twitter": ["MikeKlis", "TroyRenck"], "abbr": "den", "sbnation": "milehighreport.com", "_id": {"$oid": "57a6f49f366a35226a3c8f3a"}, "nickname": "broncos"}, {"name": "oakland", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/oak", "twitter": ["LeviDamien", "Jerrymcd", "VicTafur"], "abbr": "oak", "sbnation": "silverandblackpride.com", "_id": {"$oid": "57a6f49f366a35226a3c8f3b"}, "nickname": "raiders"}, {"name": "san diego", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/sd", "twitter": ["sdutgehlken"], "abbr": "sd", "sbnation": "boltsfromtheblue.com", "_id": {"$oid": "57a6f49f366a35226a3c8f3c"}, "nickname": "chargers"}, {"name": "kansas city", "depthChartUrl": "http://www.ourlads.com/nfldepthcharts/depthchart/kc", "twitter": ["TerezPaylor", "adamteicher"], "abbr": "kc", "sbnation": "arrowheadpride.com", "_id": {"$oid": "57a6f49f366a35226a3c8f3d"}, "nickname": "chiefs"}]

app = flask.Flask(__name__)
app.secret_key = 'aaabbbbccc'

@app.route('/test')
def test():
	depthChartHtml = Markup(getDepthHtml('MIN'))
	return render_template('game.html',depthChartHtml=depthChartHtml)

@app.route('/')
def home():
	return render_template('index.html',depthChartHtml=depthChartHtml)

@app.route('/<gameId>')
def game(gameId):
	homeTeam = {}
	awayTeam = {}
	#get each teams data
	awayTeam['abbr'] = gameId.split('@')[0]
	homeTeam['abbr'] = gameId.split('@')[1]
	#awayDoc = bsDb['teams'].find_one({'abbr':awayTeam['abbr']})
	#homeDoc = bsDb['teams'].find_one({'abbr':homeTeam['abbr']})

	awayDoc = [d for d in teamObjs if d['abbr'] == awayTeam['abbr']][0]
	homeDoc = [d for d in teamObjs if d['abbr'] == homeTeam['abbr']][0]
	print 'here'

	awayTeam['sbnation'] = awayDoc['sbnation']
	homeTeam['sbnation'] = homeDoc['sbnation']

	awayTeam['name'] = awayDoc['name']
	homeTeam['name'] = homeDoc['name']

	awayTeam['nickname'] = awayDoc['nickname']
	homeTeam['nickname'] = homeDoc['nickname']

	awayTeam['depthChart'] = Markup(getDepthHtml(awayTeam['abbr']))
	homeTeam['depthChart'] = Markup(getDepthHtml(homeTeam['abbr']))

	#get teams tweets
	awayTeamTwitterList = awayDoc['twitter']
	homeTeamTwitterList = homeDoc['twitter']
	awayTeam['tweets'] = getTeamTweets(awayTeamTwitterList)
	homeTeam['tweets'] = getTeamTweets(homeTeamTwitterList)
	return render_template('game.html', homeTeam=homeTeam,awayTeam=awayTeam)

if __name__ == '__main__':
    app.run(debug = True)