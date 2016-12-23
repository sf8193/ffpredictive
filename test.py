import nflgame

totalRushYards = dict()
totalRushYardsAtHome = dict()
totalRushYardsAway = dict()


rushattemptleaders = dict()
rushAttemptsAtHome = dict()
rushAttemptsAway = dict()


averageattempt = dict()
averageAttemptAtHome = dict()
averageAttemptAway = dict() 
differenceHomeAndAway = dict()
teams = dict()
yolo = "             "
currentLeaderYards = 0
currentWeek = 16


#prints out the top 100 rushers of each week
def printcurrentWeek(players):
	for player in players.rushing().sort('rushing_yds').limit(100):
		msg = '%s %d carries for %d yards and %d TDs'
		print player.team
		print msg % (player, player.rushing_att, player.rushing_yds, player.rushing_tds)

#adds a player to totalRushYards.txt  	
#if said player is already in the map, then their yards are added to their total
#EDIT - made so that whenever a player is added, their home/away stats also get added	
def addPlayerToList(players, totalrushYards):
	for player in players.rushing().sort('rushing_yds').limit(100):
		currentPlayer = str(player)
		if currentPlayer in totalRushYards:
			totalRushYards[currentPlayer] = totalRushYards[currentPlayer] + player.rushing_yds
		else:
			totalRushYards[currentPlayer] = player.rushing_yds
		if player.home:
			if currentPlayer in totalRushYardsAtHome:
				totalRushYardsAtHome[currentPlayer] = totalRushYardsAtHome[currentPlayer] + player.rushing_yds
			else:
				totalRushYardsAtHome[currentPlayer] = player.rushing_yds
		else:
			if currentPlayer in totalRushYardsAway:
				totalRushYardsAway[currentPlayer] = totalRushYardsAway[currentPlayer] + player.rushing_yds
			else:
				totalRushYardsAway[currentPlayer] = player.rushing_yds

#returns the player with the most rushing yards  
def getLeader(totalRushYards):
	currentLeaderYards = 0
	for currentLeader in totalRushYards:
		if totalRushYards[currentLeader] > currentLeaderYards:
			leader = currentLeader
			currentLeaderYards = totalRushYards[currentLeader]
	return leader

	
	
#adds a player to totalRushAttempts.txt  	
#if said player is already in the map, then their attempts are added to their total	
#EDIT - made so that whenever a player is added, their home/away stats also get added
def addRushingAttemptToList(players, rushattemptleaders):
	for player in players.rushing().sort('rushing_att').limit(100):
		currentPlayer = (str(player)) 
		if currentPlayer in rushattemptleaders:
			rushattemptleaders[currentPlayer] = rushattemptleaders[currentPlayer] + player.rushing_att
		else:
			rushattemptleaders[currentPlayer] = player.rushing_att
		if player.home:
			if currentPlayer in rushAttemptsAtHome:
				rushAttemptsAtHome[currentPlayer] = rushAttemptsAtHome[currentPlayer] + player.rushing_att
			else:
				rushAttemptsAtHome[currentPlayer] = player.rushing_att
		else:
			if currentPlayer in rushAttemptsAway:
				rushAttemptsAway[currentPlayer] = rushAttemptsAway[currentPlayer] + player.rushing_att
			else:
				rushAttemptsAway[currentPlayer] = player.rushing_att

				
#added for shits and giggles				
def addToTeams(players):
		for player in players.rushing().sort('rushing_att').limit(100):
			currentPlayer = str(player)
			teams[currentPlayer] = player.team

#main loop of program			
for week in range(1, currentWeek):
	games = nflgame.games(2016, week)
	players = nflgame.combine_game_stats(games)

	#printcurrentWeek(players)

	addPlayerToList(players, totalRushYards)
	addToTeams(players)
	addRushingAttemptToList(players, rushattemptleaders)
	leader = getLeader(totalRushYards)
	print "Leading Rusher so far is :", leader, totalRushYards[leader]
	print ""

#output rush yard leaders to totalRushYards.txt
sortedLeaders = sorted(totalRushYards, key = totalRushYards.__getitem__)
target = open('totalRushYards.txt', 'w')
for currentPlayer in sortedLeaders:
	target.write("{} : {}".format(currentPlayer, totalRushYards[currentPlayer]) + '\n')

#calculate the average amount each player gains on a rushing attempt
for currentPlayer in totalRushYards:
	if currentPlayer in rushattemptleaders:
		averageattempt[currentPlayer] = float(float(totalRushYards[currentPlayer]) / float(rushattemptleaders[currentPlayer]))

#calculate the average amount each player gains on a rushing attempt at home
for currentPlayer in totalRushYardsAtHome:
	if currentPlayer in rushAttemptsAtHome:
		averageAttemptAtHome[currentPlayer] = float(float(totalRushYardsAtHome[currentPlayer]) / float(rushAttemptsAtHome[currentPlayer]))

		
#calculate the average amount each player gains on a rushing attempt away
for currentPlayer in totalRushYardsAway:
	if currentPlayer in rushAttemptsAway:
		averageAttemptAway[currentPlayer] = float(float(totalRushYardsAway[currentPlayer]) / float(rushAttemptsAway[currentPlayer])) 		

#prints players that average the most rushing yards in increasing order
sortedAverageRushLeaders = sorted(averageattempt, key = averageattempt.__getitem__)
target = open('averageRushPerAttempt.txt', 'w')
for currentPlayer in sortedAverageRushLeaders:
	target.write("{} : {}".format(currentPlayer, averageattempt[currentPlayer]) + '\n')

	
target = open('rushAttemptAtHome.txt', 'w')
for currentPlayer in rushAttemptsAtHome:
	target.write("{} : {}".format(currentPlayer, rushAttemptsAtHome[currentPlayer]) + '\n')
target = open('rushAttemptAway.txt', 'w')
for currentPlayer in rushAttemptsAway:
	target.write("{} : {}".format(currentPlayer, rushAttemptsAway[currentPlayer]) + '\n')
#prints players that average the most rushing yards in increasing order at home
sortedAverageRushLeadersAtHome = sorted(averageAttemptAtHome, key = averageAttemptAtHome.__getitem__)
target = open('averageRushPerAttemptHome.txt', 'w')
for currentPlayer in sortedAverageRushLeadersAtHome:
	target.write("{} : {}".format(currentPlayer, averageAttemptAtHome[currentPlayer]) + '\n')
	
#prints players that average the most rushing yards in increasing order at home
sortedAverageRushLeadersAway = sorted(averageAttemptAway, key = averageAttemptAway.__getitem__)
target = open('averageRushPerAttemptAway.txt', 'w')
for currentPlayer in sortedAverageRushLeadersAway:
	target.write("{} : {}".format(currentPlayer, averageAttemptAway[currentPlayer]) + '\n')
	
#determine the difference between average yards gained per attempt at home and the average yards gained per attempt away	
for currentPlayer in averageAttemptAtHome:
	if currentPlayer in averageAttemptAway:
		differenceHomeAndAway[currentPlayer] = averageAttemptAtHome[currentPlayer] - averageAttemptAway[currentPlayer]
#output that ish
sortedAverageRushDifference = sorted(differenceHomeAndAway, key = differenceHomeAndAway.__getitem__)	
target = open('averageRushDifference.txt', 'w')
for currentPlayer in sortedAverageRushDifference:
	if currentPlayer in teams:
		
