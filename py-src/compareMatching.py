import sys
import re
import ast

def parseMatchingFile(sFileName):
	reMD5 = re.compile(r'^[0-9a-f]{32}')
	f = open(sFileName)

	dictMatch = {}

	while True:
		line = f.readline()
		if not line:
			break

		match = reMD5.match(line)
		if match:
			sMD5 = line[:-1]
			continue

		if line.startswith('['):
			listMatching = ast.literal_eval(line[:-1])
			listMatching.sort()
			dictMatch[sMD5] = listMatching
			continue

	f.close()

	return dictMatch	



if __name__ == '__main__':
	sMatchingFile = sys.argv[1]
	sIndexFile = sys.argv[2]

	matchDict = parseMatchingFile(sMatchingFile)
	
	indexDict = parseMatchingFile(sIndexFile)

	

	numMiss = 0
	numPartial = 0
	numCorrectMatch = 0

	for md5 in indexDict:
		if md5 not in matchDict:
			continue

		if len(indexDict[md5]) == 0 and len(matchDict[md5]) > 0:
			numMiss += 1
			continue

		if cmp(indexDict[md5], matchDict[md5]) != 0:
			numPartial += 1

		elif len(indexDict[md5]) > 0:
			numCorrectMatch += 1		

			
	print 'MISS:', numMiss
	print 'PARTIAL:', numPartial
	print 'CorrectMatch:', numCorrectMatch
	print 'TOTAL:', len(indexDict)
