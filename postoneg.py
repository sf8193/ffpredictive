import nflgame
import csv

games=nflgame.games(year=[2009,2010,2011,2012,2013,2014,2015,2016],kind='REG')
players=nflgame.combine_plays(games)

counterpos=0
counterneg=0

rushers={}

with open('pos vs neg.csv','wb') as csvfile:
	schedulewriter=csv.writer(csvfile,delimiter=',')
	schedulewriter.writerow(['player','positive','negative'])

	for numbers in players.rushing().sort("rushing_yds"):
		if(numbers.rushing_yds > 0):
			rushers[numbers]++
			
		schedulewriter.writerow([numbers,numbers.receiving_rec,numbers.receiving_tar,ratio])
		print numbers, numbers.receiving_rec, numbers.receiving_tar, '{:.1%}'.format(ratio)
