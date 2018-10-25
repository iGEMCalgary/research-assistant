from .webScraper import Parser
from .summarizer import Summarizer
import time

# def getYear(prompt=''):
	# while True:
		# try:
			# year = int(input(prompt))
			# if(year < 2008 or year > 2017):
				# raise Exception
			# break
		# except Exception:
			# print('\nInvalid input. ')
			# prompt = 'Please enter a valid year between 2008 and 2017 inclusive: '
	# return str(year)
	
# year = getYear('Please enter a year: ')
# print('\nExtracting iGEM ' +  + ' software...')

def main(year, team, description):
	# print("Extracting iGEM software.")
		
	start = time.time()
	teamInfo = 0
	p = Parser()
	# for year in range (2008, 2009):
	teamInfo = p.getData(str(year))

	summarizer = Summarizer()
	summary = ''
	teamsWithSoftware = 0

	teamsToRemove = []

	for i in range(len(teamInfo)):
		result = summarizer.summarize(teamInfo[i][1])
		
		# Notes: - Original summary accessed by result['MeanDescription'] - or topNDescription
					# - No error messages - only 'Unable to retrive <team name> software.'
					# at teamInfo[i][1]
		if result['Success'] and len(result['MeanDescription']) > 0:
			teamInfo[i][1] = result['MeanDescription']
			teamsWithSoftware += 1
		else:	
			teamsToRemove.append(i)
		
	for i in range(len(teamsToRemove)-1, -1, -1):
		del(teamInfo[teamsToRemove[i]])
		
	# print("Year: " + str(year) + "\nTime: " + str(time.time() - start) + "\nEntries: " + str(len(teamInfo)))
		
	for i in range(len(teamInfo)):
		# print(teamInfo[i][0])
		team.append(teamInfo[i][0])
		# print(teamInfo[i][1])
		description.append(teamInfo[i][1])

	end = time.time() - start
	# print("total time: " + str(end))