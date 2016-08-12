import sys
from lsh import *
import pickle
from sets import Set

counter = 0

def groupTrainFPs(listFPs):
	sizeList = [84002, 42001, 21005, 10500, 5250, 2625, 1312, 656, 0]
	groupDict = {}

	for index, fp in enumerate(listFPs):
		length = len(fp)
		numIndex = 0
		
		while length < sizeList[numIndex]:
			numIndex += 1

		if numIndex not in groupDict:
			groupDict[numIndex] = []

		groupDict[numIndex].append(index)

	return groupDict

def fpMatching(fpList1, fpList2):
	global counter
	counter += 1
	fpSet1 = Set(fpList1)
	fpSet2 = Set(fpList2)

	fpIntersect = fpSet1.intersection(fpSet2)
	
	if len(fpSet1) == 0:
		return False
	elif len(fpIntersect) * 1.0 / len(fpSet1) >= 0.9:
		return True
	else:
		return False

	

		

if __name__ == '__main__':
	sTrainDirectory = sys.argv[1]
	sTestDirectory = sys.argv[2]

	listTrainFPs, listTrainFPFiles = sparseListFromDirectory(sTrainDirectory)
	listTestFPs, listTestFPFiles = sparseListFromDirectory(sTestDirectory)

	coeffsA, coeffsB = generateCoeffs(100)

	listTrainMinHash = []
	listTestMinHash  = []


	print 'Computing MinHash for Train Set'
	print
	for index, fp in enumerate(listTrainFPs):
		listTrainMinHash.append(compMinHash1(fp, coeffsA, coeffsB))

	print 'Computing MinHash for Test Set'
	print
	for index, fp in enumerate(listTestFPs):
		listTestMinHash.append(compMinHash1(fp, coeffsA, coeffsB))

	groupDict = groupTrainFPs(listTrainFPs)	
	lshDict = {}

	#saveList = [listFPs, listFPFiles, coeffsA, coeffsB, listMinHash, groupDict]

	#with open('filename.pickle', 'wb') as handle:
	#	pickle.dump(saveList, handle)

	#exit()
	#with open('filename.pickle', 'rb') as handle:
	#	saveList = pickle.load(handle)

	#print 'finish loading'
	#listFPs = saveList[0]
	#listFPFiles = saveList[1]
	#coeffsA = saveList[2] 
	#coeffsB = saveList[3] 
	#listMinHash = saveList[4] 
	#groupDict = saveList[5]

	#sTestFile = '../test/59fd30f13a2a7fc737b073d3dedd0ec4.bb'

	#lshDict = {}
	print 'Computing LSH for Train Set'
	print
	for groupIndex in groupDict:
		lshCache = LSH()
		
		for index in groupDict[groupIndex]:
			lsh = LSH.getLSH(listTrainMinHash[index], 20, 5)
			lshCache.insertLSH(lsh, index)

		lshDict[groupIndex] = lshCache


	#lshDict[3].printStat()


	#for testMinHash in listTestMinHash:
	
	numNecessaryMatching = 0	

	for index, testMinHash in enumerate(listTestMinHash):
		#print testMinHash
		lsh = LSH.getLSH(testMinHash, 20, 5)
		checkList = []
 		for groupIndex in lshDict:
			retList = lshDict[groupIndex].searchLSH(lsh)
			#print retList
			checkList = checkList + retList


		checkList = list(Set(checkList))
		matchingList = []

		boolFlag = True		

		for checkID in checkList:
			if fpMatching(listTrainFPs[checkID], listTestFPs[index]):
				matchingList.append(checkID)

				if boolFlag:
					numNecessaryMatching += 1 
					boolFlag = False

			if boolFlag:
				numNecessaryMatching += 1

		MD5List = [listTrainFPFiles[matchingID][-35:-3] for matchingID in matchingList]
		print listTestFPFiles[index][-35:-3]
		print MD5List
		print

	print "Matching Computing:", counter
	print 'Necessary Matching Number:', numNecessaryMatching

