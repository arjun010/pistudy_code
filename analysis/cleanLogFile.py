import os
import sys
import json


fileToRead = sys.argv[1]
fileToReadFP = open(fileToRead,"r")
allLinesInFile = fileToReadFP.readlines()


resList = []

for line in allLinesInFile:
	arr = line[line.index("{"):line.index("}]")].split("},")
	for item in arr:
		#print item+"}"
		resList.append(json.loads(item+"}"))
		#resList.append(json.loads(line[line.index("{"):line.index("}]")+1]))	


with open('data.json', 'w') as outfile:
    json.dump(resList, outfile,indent=0)