from cryptography.fernet import Fernet
import pyautogui as py
import pandas as pd
import numpy as np
import maskpass
import hashlib
import time
import cv2
import os

starting = "Boreal"
ending = "Warp"

while (True):
	os.system('cls')
	print("Wynncraft's Automated Data Collector\n")
	password = maskpass.advpass(prompt="Enter the password: ", mask="\u00B7") + "sniperjake1994"
	if (hashlib.sha256(password.encode('utf-8')).hexdigest() == "9fd768728cff0070570900e65a0355a725fb7762fd8522deb094050130e164c5"):
		break
	else:
		os.system('cls')
		maskpass.askpass(prompt="Wynncraft's Automated Data Collector\n\nPress enter to try again.", mask="")

os.system('cls')
key = maskpass.askpass(prompt="Wynncraft's Automated Data Collector\n\nAuthentication Successful\n\nPress enter to begin the program.", mask="") + "Adamastor"

if (hashlib.sha256(key.encode('utf-8')).hexdigest() == "5581a0b43e297785b843b22fed421ec6bda040d53da21c5577a60a84280b5cbd"):
	key += "Kiwi"
	key = hashlib.sha256(key.encode('utf-8')).hexdigest()
	key = key[:-21] + '='
	fernet = Fernet(key)
	encMessage = b'gAAAAABi8YDHVCaLZe4s9WoPKA5G98zHs9v6S_fqcPPVZVnfj0ysuI4PbK2pKFhl1nGGCwmvb8hX7s3P5dF_Rc2ho9hKHe60237SGOBy6naUcWmci3QV1daqyMQcoC-ac3QomlXTELD8'
	key = fernet.decrypt(encMessage).decode()
	print(key)
	#print("\n\nPress enter to close the program.", end = "")
	#maskpass.askpass(prompt="", mask="")
	exit()

mythics = ["Boreal", "Crusade Sabatons", "Dawnbreak", "Discoverer", "Galleon", "Moontower", "Resurgence", "Revenant", "Slayer", "Stardew", "Warchief",	
			"Az", "Divzer", "Epoch", "Freedom", "Grandmother", "Ignis",	"Spring", "Stratiformis",
			"Archangel", "Cataclysm", "Grimtrap", "Inferno", "Nirvana",	"Nullification", "Oblivion", "Weathered", 
			"Absolution", "Aftershock", "Fantasia",	"Hadal", "Immolation", "Olympic", "Sunstar", "Toxoplasmosis", 
			"Alkatraz",	"Apocalypse", "Collapse", "Convergence", "Guardian", "Hero", "Idol", "Thrundacrack",
			"Fatal", "Gaia", "Lament", "Monster", "Pure", "Quetzalcoatl", "Singularity", "Warp"]

ram = []

startingIndex = mythics.index(starting)
endingIndex = mythics.index(ending) + 1

directory = os.getcwd() + '\\'
xlWriter = pd.ExcelWriter(directory + 'data.xlsx')
directory += 'Images\\'
first = True
zeroStart = False
error = False
py.hotkey('alt', 'tab')
time.sleep(1)
startTime = time.time()

def check(caseNumber):
	passes = 0
	try:
		while True:
			location = ()
			if (caseNumber == 1):
				location = py.locateOnScreen(directory + 'checkSign.png', region=(1080, 510, 50, 50))
			elif (caseNumber == 2):
				location = py.locateOnScreen(directory + 'emeraldSign.png', region=(1125, 508, 525, 17))
			elif (caseNumber == 3):
				location = py.locateOnScreen(directory + 'reloadSign.png', region=(1080, 510, 50, 50))
			elif (caseNumber == 4):
				location = py.locateOnScreen(directory + 'signSign.png', region=(900, 335, 50, 50))
			elif (caseNumber == 5):
				location = py.locateOnScreen(directory + 'pinkWoolSign.png', region=(790, 335, 50, 50))
			elif (caseNumber == 6):
				location = py.locateOnScreen(directory + 'bookSignUpdated.png', region=(1060, 990, 40, 40))
			elif (caseNumber == 7):
				location = py.locateOnScreen(directory + 'halfBookSignUpdated.png', region=(1060, 990, 40, 40))
			elif (caseNumber == 8):
				location = py.locateOnScreen(directory + 'swordSign.png', region=(900, 410, 50, 50))
			elif (caseNumber == 9):
				location = py.locateOnScreen(directory + 'swordSign.png', region=(790, 370, 50, 50))
			elif (caseNumber == 0):
				location = py.locateOnScreen(directory + 'reloadSign.png', region=(1080, 335, 50, 50))
			elif (caseNumber == 11):
				location = py.locateOnScreen(directory + 'checkSign.png', region=(970, 425, 50, 50))
			try:
				location.left
				return 0
			except:
				passes += 1
				if (caseNumber == 7):
					py.press('t')
				if (caseNumber == 2):
					location = py.locateOnScreen(directory + 'arrowSign.png', region=(1205, 420, 65, 30))
					try:
						location.left
						return 1
					except:
						pass
				if (passes > 300):
					if (caseNumber == 2):
						return 2
					if (len(ram) > 0 and zeroStart):
						df = pd.DataFrame(ram)
						if (i <= 10):
							df.to_excel(excel_writer=xlWriter)
						elif (i <= 18):
							df.to_excel(excel_writer=xlWriter, startrow=13, header=False)
						elif (i <= 26):
							df.to_excel(excel_writer=xlWriter, startrow=22, header=False)
						elif (i <= 34):
							df.to_excel(excel_writer=xlWriter, startrow=31, header=False)
						elif (i <= 42):
							df.to_excel(excel_writer=xlWriter, startrow=40, header=False)
						elif (i <= 50):
							df.to_excel(excel_writer=xlWriter, startrow=49, header=False)
					if (zeroStart):
						xlWriter.close()
					py.hotkey('alt', 'tab')
					print("\nStopped at index " + str(i) +  ".")
					#print("\n\nPress enter to close the program.", end = "")
					#maskpass.advpass(prompt="", mask="")
					exit()
	except KeyboardInterrupt:
		print("\nStopped at index " + str(i) +  ".")
		#print("\n\nPress enter to close the program.", end = "")
		#maskpass.advpass(prompt="", mask="")
		exit()
	return 3

for i in range (startingIndex, endingIndex):
	if (i == 0):
		zeroStart = True

	if (first):
		check(0)
		py.moveTo(x = 1105, y = 465)
		py.click()
		check(1)

		py.moveTo(x = 995, y = 505)
		py.click()
		check(5)

		first = False

	else:
		py.moveTo(x = 1105, y = 415)
		py.click()
		check(3)

		py.moveTo(x = 1105, y = 360)
		py.click()
		check(1)

		py.moveTo(x = 850, y = 360)
		py.click()
		if (i == 12):
			py.moveTo(x = 100, y = 100)
		check(4)

		if (i == 12 and startingIndex != 12):
			py.moveTo(x = 850, y = 360)
			py.click()
			check(8)

	py.moveTo(x = 925, y = 360)
	py.click()
	check(6)

	py.press('t')
	check(7)

	py.write(mythics[i])
	py.press('enter')
	check(5)

	if (i == 11):
		py.moveTo(x = 1030, y = 395)
		py.click()
		check(9)

	py.moveTo(x = 1105, y = 540)
	py.click()
	py.moveTo(x = 100, y = 100)
	check(3)

	py.moveTo(x = 815, y = 360)
	py.click()
	py.moveTo(x = 1105, y = 450)
	number = check(2)
	if (number == 0):
		location = py.locateOnScreen(directory + 'emeraldSign.png', region=(1125, 508, 525, 17))
		boundary = location.left - 1369
		screenshot = py.screenshot(region=(1369, 508, boundary, 17))
		screenshot.save(directory + 'price.png')

		img_rgb = cv2.imread(directory + 'price.png')
		length = 0
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
		dictionary = {}
		for j in range(10):
			letter = str(j)
			template = cv2.imread(directory + letter + 'Sign.png', 0)
			res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
			threshold = 0.9999
			loc = np.where(res >= threshold)
			lists = loc[1].tolist()
			for k in lists:
				dictionary[k] = letter
				length += 1
			if (length == 7):
				break
		listOfKeys = sorted(dictionary)
		text = ""
		for j in range(len(listOfKeys)):
			text += dictionary.get(listOfKeys[j])
		number = int(text)
		ram.append(number)
	else:
		ram.append(number)
		error = True

	if (not zeroStart):
		print(number)
		#print(mythics[i]  + ": " + str(ram[-1]))
	if (i == 10 or i == 18 or i == 26 or i == 34 or i == 42 or i == 50):
		if (zeroStart):
			df = pd.DataFrame(ram)
			if (i == 10):
				df.to_excel(excel_writer=xlWriter)
			elif (i == 18):
				df.to_excel(excel_writer=xlWriter, startrow=13, header=False)
			elif (i == 26):
				df.to_excel(excel_writer=xlWriter, startrow=22, header=False)
			elif (i == 34):
				df.to_excel(excel_writer=xlWriter, startrow=31, header=False)
			elif (i == 42):
				df.to_excel(excel_writer=xlWriter, startrow=40, header=False)
			elif (i == 50):
				df.to_excel(excel_writer=xlWriter, startrow=49, header=False)
		else:
			print()
		ram.clear()

if (zeroStart):
	xlWriter.close()
finishTime = time.time() - startTime
py.hotkey('alt', 'tab')
print("\nCompleted in", finishTime, "seconds.")
if (error):
	print("Error")
#print("\n\nPress enter to close the program.", end = "")
#maskpass.advpass(prompt="", mask="")