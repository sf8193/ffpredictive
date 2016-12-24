import nflgame
import datetime
import forecastio
import pytz




##################################################################################################################
##################################################################################################################
#populate the location, month, day, time dictionaries
gameCount = 0
gameLocation = dict()
gameMonth = dict()
gameDay = dict()
gameTime = dict()
gameAway = dict()
for year in range(2009,2015):
	for week in range(1,18):
		future_games = nflgame.live._games_in_week(year, week)
		for game in future_games:
			gameCount += 1
			print '{} {} at {} on {}/{} {}'.format(str(gameCount), game['away'], game['home'], game['month'], game['day'], game['time'])
			gameLocation[gameCount] = game['home']
			gameAway[gameCount] = game['away']
			gameMonth[gameCount] = int(game['month'])
			gameDay[gameCount] = int(game['day'])
			gameTime[gameCount] = game['time']
		print""
	print""
print gameCount
##################################################################################################################
##################################################################################################################
##################################################################################################################
#populate latitude dictionary
latitude = dict()
latitude['NO'] = 29.9511
latitude['SEA'] = 47.5952
latitude['SF'] = 37.4023
latitude['DEN'] = 39.7439
latitude['WAS'] = 38.9076
latitude['TEN'] = 36.1665
latitude['TB'] = 27.9759
latitude['PIT'] = 40.4468
latitude['NYG'] = 40.8128
latitude['NE'] = 42.0909
latitude['MIN'] = 44.9737
latitude['MIA'] = 25.9580
latitude['KC'] = 39.0489
latitude['HOU'] = 29.6847
latitude['GB'] = 44.5013
latitude['BAL'] = 39.2780
latitude['ATL'] = 33.7577
latitude['CIN'] = 39.0955
latitude['ARI'] = 33.5276
latitude['OAK'] = 37.7516
latitude['DAL'] = 32.7473
latitude['STL'] = 38.6226
latitude['NYJ'] = 40.8128
latitude['CHI'] = 41.8623
latitude['CAR'] = 35.2258
latitude['JAC'] = 30.3239
latitude['PHI'] = 39.9008
latitude['SD'] = 32.7831
latitude['IND'] = 39.7601
latitude['DET'] = 42.3400
latitude['BUF'] = 42.7738
latitude['CLE'] = 41.5061

##################################################################################################################
##################################################################################################################
##################################################################################################################
#populate longitutututude dictionary
longitutututude = dict()
longitutututude['NO'] = -90.0812
longitutututude['SEA'] = -122.3316
longitutututude['SF'] = -121.9690
longitutututude['DEN'] = -105.0201
longitutututude['WAS'] = -76.8645
longitutututude['TEN'] = -86.7713
longitutututude['TB'] = -82.5033
longitutututude['PIT'] = -80.0158
longitutututude['NYG'] = -74.0742
longitutututude['NE'] = -71.2643
longitutututude['MIN'] = -93.2577
longitutututude['MIA'] = -80.2389
longitutututude['KC'] = -94.4839
longitutututude['HOU'] = -95.4107
longitutututude['GB'] = -88.0622
longitutututude['BAL'] = -76.6227
longitutututude['ATL'] = -84.4008
longitutututude['CIN'] = -84.5161
longitutututude['ARI'] = -112.2626
longitutututude['OAK'] = -122.2005
longitutututude['DAL'] = -97.0945
longitutututude['STL'] = -90.1928
longitutututude['NYJ'] = -74.0742
longitutututude['CHI'] = -87.6167
longitutututude['CAR'] = -80.8528
longitutututude['JAC'] = -81.6373
longitutututude['PHI'] = -75.1675
longitutututude['SD'] = -117.1196
longitutututude['IND'] = -86.1639
longitutututude['DET'] = -83.0456
longitutututude['BUF'] = -78.7870
longitutututude['CLE'] = -81.6995
##################################################################################################################
##################################################################################################################
##################################################################################################################
#DO THE BUSINESS
api_key = "b33d8c80314ec37ccc9741aa81362839"
currentGame = 0
gameWeatherCollection = dict()
target = open('weatherCollection.txt', 'w')
for currentGame in range(1, 1537):
		currentYear = int((currentGame / 256) + 2009)
		if currentYear == 2015:
			currentYear = 2014
		lat = latitude[gameLocation[currentGame]]
		lng = longitutututude[gameLocation[currentGame]]
		if len(str(gameTime[currentGame])) == 4:
			if (gameLocation[currentGame] == 'KC') or (gameLocation[currentGame] == 'CHI') or (gameLocation[currentGame] == 'HOU') or (gameLocation[currentGame] == 'TEN') or (gameLocation[currentGame] == 'DAL') or (gameLocation[currentGame] == 'GB') or (gameLocation[currentGame] == 'MIN') or (gameLocation[currentGame] == 'STL'):
				hour = int(gameTime[currentGame][:1]) + 11 #central time
			elif (gameLocation[currentGame] == 'SF') or (gameLocation[currentGame] == 'SEA') or (gameLocation[currentGame] == 'SD') or (gameLocation[currentGame] == 'OAK') or (gameLocation[currentGame] == 'ARI'):
				hour = int(gameTime[currentGame][:1]) + 9 #pacific time
			elif (gameLocation[currentGame] == 'ARI') or (gameLocation[currentGame] == 'DEN'):
				hour = int(gameTime[currentGame][:1]) + 10 #mountain time
			else:
				hour = int(gameTime[currentGame][:1]) + 12 #regular time
		else:
			if (gameLocation[currentGame] == 'KC') or (gameLocation[currentGame] == 'CHI') or (gameLocation[currentGame] == 'HOU') or (gameLocation[currentGame] == 'TEN') or (gameLocation[currentGame] == 'DAL') or (gameLocation[currentGame] == 'GB') or (gameLocation[currentGame] == 'MIN') or (gameLocation[currentGame] == 'STL'):
				hour = int(gameTime[currentGame][:2]) + 11 #central time
			elif (gameLocation[currentGame] == 'SF') or (gameLocation[currentGame] == 'SEA') or (gameLocation[currentGame] == 'SD') or (gameLocation[currentGame] == 'OAK') or (gameLocation[currentGame] == 'ARI'):
				hour = int(gameTime[currentGame][:2]) + 9 #pacific time
			elif (gameLocation[currentGame] == 'ARI') or (gameLocation[currentGame] == 'DEN'):
				hour = int(gameTime[currentGame][:2]) + 10 #mountain time
			else:
				hour = int(gameTime[currentGame][:2]) + 12 #regular time
		if hour >= 24:
			hour -= 12
		minute = int(gameTime[currentGame][-2:])
		time = datetime.datetime(currentYear, gameMonth[currentGame], gameDay[currentGame], hour, minute, 0)
	
		forecast = forecastio.load_forecast(api_key, lat, lng, time)
		
		print forecast.currently()
		
		byHour = forecast.hourly()
		
		print byHour.icon
		
		count = 0
		for hourlyData in byHour.data:
			if count == 2:
				break
			if count == 0:
				target.write("CURRENT GAME: {} : TEMPERATURE: {} WEATHER CONDITIONS: {}    HOME:{}    AWAY: {} ".format(currentGame, (hourlyData.temperature), (byHour.icon), gameLocation[currentGame], gameAway[currentGame])+ '\n')
			if count == 1:
				target.write("CURRENT GAME: {} : TEMPERATURE: {} WEATHER CONDITIONS: {}    HOME:{}    AWAY: {} ".format(currentGame, (hourlyData.temperature), (byHour.icon), gameLocation[currentGame], gameAway[currentGame])+ '\n')
			print hourlyData.temperature
			count = count + 1
		
		if currentGame % 16 == 0:
			print ""
	
	