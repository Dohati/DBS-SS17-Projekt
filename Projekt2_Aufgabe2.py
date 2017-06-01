# -*- coding: utf-8 -*-
from openpyxl import Workbook
from openpyxl import load_workbook
import re

gDB = load_workbook('american-election-tweets.xlsx') #Gegebende Datenbank wird geladen


wsgDB = gDB.active #Aktives Worksheet der gegebenen Datenbank


nDB = Workbook() #Workbook für neue Datenbank wird angelegt

wsnDB = nDB.active #Aktives Worksheet der neuen Datenbank

#Herausfiltern der benötigten Informationen, basierend auf dem Relationalen Modells.
i=1
for row in wsgDB:
	wsnDB['A'+str(i)] = wsgDB['A'+str(i)].value #Kopieren von "handle" in die neue Datenbank
	wsnDB['B'+str(i)] = wsgDB['B'+str(i)].value #Kopieren von "text" in die neue Datenbank
	wsnDB['C'+str(i)] = wsgDB['E'+str(i)].value #Kopieren von "time" in die neue Datenbank
	wsnDB['D'+str(i)] = wsgDB['H'+str(i)].value #Kopieren von "retweet_count" in die neue Datenbank
	wsnDB['E'+str(i)] = wsgDB['I'+str(i)].value #Kopieren von "favorite_count" in die neue Datenbank
	i=i+1 #Zähler wird um eins erhöhen, umnächste Zelle ansprechen zu können

#Herausfiltern der Hashtags aus dem Text

k=1
z=0
for row in wsgDB: #Gehe jede Zeile der Spalte "text" durch
	hashs = '' #Alle hashtags eines textes werden hier gespeichert
	hashtag = '' #Hashtags werden hier einzeln erfasst
	temp = wsgDB['B' + str(k)].value #Abspeichern des textes in einer Variable
	for j in temp: #Gehen dem derzeitigen text durch (jeden einzeln) und speichern alle hashtags ab
		if (j == '#'): #Hashtag im text temp gefunden
			for a in range(z, len(temp)): #Sollte ein hashtag gefunden worden sein, gehen wir den nachfolgenden Text durch um es zu erfassen
				if (temp[a]==' ' or temp[a]=='\n'): 
				#Wenn nicht erwünschtes Zeichen gedunden
					break #...ende des Hashtags erreicht
				else:
					hashtag += temp[a] #Wenn kein space gefunden, dann ist a Teil des Hashtags
			if (len(hashtag) > 1):	#Wurde ein Hashtag falsch verwendet, wird es hier herausgefiltert
				hashs += re.sub("[^a-zA-Z0-9#]", "",hashtag).upper() #Speichere alle gefunden hashtags in der entsprechenden Zeile
		hashtag=''
		z+=1
	wsnDB['F' +str(k)] = hashs #Speichern der Hashtags in die entsprechende Zelle
	k=k+1 #Zähler um eins erhöhen, um nächte Zelle ansprechen zu können
	z=0

wsnDB['F1'] = "hashtags" #Name der neuen Spalte
nDB.save('neueDatenbank.xlsx') #Speichern der neuen Datenbank
