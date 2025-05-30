import random, sqlite3
from datetime import date
import json
import os

checklistFile = 'dailyChecklist.json'

def generateList():
	conn = sqlite3.connect('exercise_data.db')
	cursor = conn.cursor()

	cursor.execute("SELECT exercisenumber FROM exercises")
	rows = cursor.fetchall()

	pastProbs = [row[0] for row in rows]

	problems = {'1': {'1': '80', '2': '32', '3': '66', '4': '9', '5': '49', '6': '66', '7': '44', '8': '73'}, '2': {'1': '61', '2': '65', '3': '110', '4': '58', '5': '90', '6': '62', '7': '36', '8': '50', '9': '42'}, '3': {'1': '72', '2': '36', '3': '77', '4': '74', '5': '60', '6': '28', '7': '80', '8': '40', '9': '73'}, '4': {'1': '32', '2': '75', '3': '84', '4': '74', '5': '85'}, '5': {'1': '64', '2': '72', '3': '48', '4': '34', '5': '24'}, '6': {'1': '50', '2': '111', '3': '74', '4': '94', '5': '22', '6': '80', '7': '71', '8': '104'}, '7': {'1': '74', '2': '70', '3': '44', '4': '75', '5': '84', '6': '46', '7': '50', '8': '82'}, '8': {'1': '46', '2': '39', '3': '51', '4': '23', '5': '21'}, '9': {'1': '17', '2': '28', '3': '54', '4': '25', '5': '38', '6': '12'}, '10': {'1': '52', '2': '74', '3': '78', '4': '56', '5': '66', '6': '31'}, '11': {'1': '93', '2': '92', '3': '46', '4': '46', '5': '36', '6': '53', '7': '38', '8': '42', '9': '42', '10': '86', '11': '39'}, '12': {'1': '48', '2': '52', '3': '65', '4': '54', '5': '83', '6': '53'}, '13': {'1': '54', '2': '58', '3': '68', '4': '46'}, '14': {'1': '81', '2': '46', '3': '105', '4': '46', '5': '59', '6': '70', '7': '60', '8': '50'}, '15': {'1': '52', '2': '70', '3': '41', '4': '33', '5': '24', '6': '55', '7': '31', '8': '49', '9': '28'}, '16': {'1': '36', '2': '52', '3': '36', '4': '31', '5': '39', '6': '64', '7': '49', '8': '20', '9': '32'}, '17': {'1': '35', '2': '28', '3': '18', '4': '12'}}

	dailyProbs = []

	while len(dailyProbs) < 10:
	    chapter = random.choice(list(problems.keys()))
	    section = random.choice(list(problems[chapter].items()))
	    exercise = random.randrange(1,int(section[1])+1)
	    prob = f'{chapter}.{section[0]}: {exercise}'
	    if prob not in pastProbs:
	        dailyProbs.append(prob)
	        pastProbs.append(prob)

	organizedProbs = sorted(dailyProbs, key=lambda x: (float(x.split(':')[0]), float(x.split(':')[1])))

	today = str(date.today())

	if os.path.exists(checklistFile):
		with open(checklistFile, 'r') as f:
			data = json.load(f)
			if data["date"] == today:
				return data['checklist']

	newItems = [{'id': random.randint(1,1000000), 'name': x, 'checked': False} for x in organizedProbs]

	with open(checklistFile, 'w') as f:
		json.dump({'date': today, 'checklist': newItems},f)

	return newItems

def saveChecklist(checklist):
	today = str(date.today())
	with open(checklistFile, 'w') as f:
		json.dump({'date': today, 'checklist': checklist},f)

def moreWork():
	conn = sqlite3.connect('exercise_data.db')
	cursor = conn.cursor()

	cursor.execute("SELECT exercisenumber FROM exercises")
	rows = cursor.fetchall()

	pastProbs = [row[0] for row in rows]

	problems = {'1': {'1': '80', '2': '32', '3': '66', '4': '9', '5': '49', '6': '66', '7': '44', '8': '73'}, '2': {'1': '61', '2': '65', '3': '110', '4': '58', '5': '90', '6': '62', '7': '36', '8': '50', '9': '42'}, '3': {'1': '72', '2': '36', '3': '77', '4': '74', '5': '60', '6': '28', '7': '80', '8': '40', '9': '73'}, '4': {'1': '32', '2': '75', '3': '84', '4': '74', '5': '85'}, '5': {'1': '64', '2': '72', '3': '48', '4': '34', '5': '24'}, '6': {'1': '50', '2': '111', '3': '74', '4': '94', '5': '22', '6': '80', '7': '71', '8': '104'}, '7': {'1': '74', '2': '70', '3': '44', '4': '75', '5': '84', '6': '46', '7': '50', '8': '82'}, '8': {'1': '46', '2': '39', '3': '51', '4': '23', '5': '21'}, '9': {'1': '17', '2': '28', '3': '54', '4': '25', '5': '38', '6': '12'}, '10': {'1': '52', '2': '74', '3': '78', '4': '56', '5': '66', '6': '31'}, '11': {'1': '93', '2': '92', '3': '46', '4': '46', '5': '36', '6': '53', '7': '38', '8': '42', '9': '42', '10': '86', '11': '39'}, '12': {'1': '48', '2': '52', '3': '65', '4': '54', '5': '83', '6': '53'}, '13': {'1': '54', '2': '58', '3': '68', '4': '46'}, '14': {'1': '81', '2': '46', '3': '105', '4': '46', '5': '59', '6': '70', '7': '60', '8': '50'}, '15': {'1': '52', '2': '70', '3': '41', '4': '33', '5': '24', '6': '55', '7': '31', '8': '49', '9': '28'}, '16': {'1': '36', '2': '52', '3': '36', '4': '31', '5': '39', '6': '64', '7': '49', '8': '20', '9': '32'}, '17': {'1': '35', '2': '28', '3': '18', '4': '12'}}

	dailyProbs = []

	while len(dailyProbs) < 10:
	    chapter = random.choice(list(problems.keys()))
	    section = random.choice(list(problems[chapter].items()))
	    exercise = random.randrange(1,int(section[1])+1)
	    prob = f'{chapter}.{section[0]}: {exercise}'
	    if prob not in pastProbs:
	        dailyProbs.append(prob)
	        pastProbs.append(prob)

	organizedProbs = sorted(dailyProbs, key=lambda x: (float(x.split(':')[0]), float(x.split(':')[1])))

	today = str(date.today())

	with open(checklistFile, 'r') as f:
		data = json.load(f)

	checklistItems = data['checklist']
	newItems = [{'id': random.randint(1,1000000), 'name': x, 'checked': False} for x in organizedProbs]
	updatedList = checklistItems + newItems

	with open(checklistFile,'w') as f:
		json.dump({'date': today, 'checklist': updatedList},f)

	return updatedList
