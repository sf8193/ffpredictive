import nflgame
import csv

everyseason=nflgame.games(year=[2009,2010,2011,2012,2013,2014,2015,2016],kind='REG')
players=nflgame.combine(everyseason,plays=True)

with open('targets vs reception.csv','wb') as csvfile:
	schedulewriter=csv.writer(csvfile,delimiter=',')
	schedulewriter.writerow(['player','receptions','targets'])

	for numbers in players.receiving().sort("receiving_tar").limit(300):
		rec=float(numbers.receiving_rec)
		tar=float(numbers.receiving_tar)
		ratio=rec/tar
		schedulewriter.writerow([numbers,numbers.receiving_rec,numbers.receiving_tar,ratio])
		print numbers, numbers.receiving_rec, numbers.receiving_tar, '{:.1%}'.format(ratio)
