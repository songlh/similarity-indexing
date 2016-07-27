import ast
import random
from fpLoader import *

def parseCoeffsFromFile(sFileName):
	fcoeffs = open(sFileName, 'r')
	sFirstLine = fcoeffs.readline()
	sSecondLine = fcoeffs.readline()	
	fcoeffs.close()

	coeffsA = [int(strNum) for strNum in sFirstLine.split()]
	coeffsB = [int(strNum) for strNum in sSecondLine.split()]

	return coeffsA, coeffsB

def loadCoeffsFromFile(sFileName):
	fcoeffs = open(sFileName, 'r')
	sFirstLine = fcoeffs.readline()
	sSecondLine = fcoeffs.readline()

	coeffsA = ast.literal_eval(sFirstLine)
	coeffsB = ast.literal_eval(sSecondLine)

	fcoeffs.close()

	return coeffsA, coeffsB

def dumpCoeffsToFile(coeffsA, coeffsB, sFileName):
	fcoeffs = open(sFileName, 'w')
	fcoeffs.write(str(coeffsA))
	fcoeffs.write('\n')
	fcoeffs.write(str(coeffsB))
	fcoeffs.write('\n')
	fcoeffs.close()



def generateCoeffs(numHash):

	coeffsA = []
	coeffsB = []

	while numHash > 0:
		randIndex = random.randint(0, MAXCOEFFVALUE) 

		# Ensure that each random number is unique.
		while randIndex in coeffsA:
			randIndex = random.randint(0, MAXCOEFFVALUE)

		coeffsA.append(randIndex)

		randIndex = random.randint(0, MAXCOEFFVALUE) 

		# Ensure that each random number is unique.
		while randIndex in coeffsB:
			randIndex = random.randint(0, MAXCOEFFVALUE)

		coeffsB.append(randIndex)

		numHash -= 1

	return coeffsA, coeffsB


def compMinHash0(sparseFP, coeffsA, coeffsB, totalFPs = FEATURE_SIZE):
	signatures = [totalFPs] * len(coeffsA)
	numIndex = 0

	for num in sparseFP:
		numIndex = 0

		while numIndex < len(coeffsA):
			numHashCode = (coeffsA[numIndex] * num + coeffsB[numIndex]) % totalFPs
			#print numHashCode, signatures[numIndex]

			if numHashCode < signatures[numIndex]:
				signatures[numIndex] = numHashCode

			numIndex +=1

	return signatures

def compMinHash1(sparseFP, coeffsA, coeffsB, totalFPs = FEATURE_SIZE):

	numIndex = 0
	signatures = []

	while numIndex < len(coeffsA):

		minHashCode = totalFPs
		for num in sparseFP:
			numHashCode = (coeffsA[numIndex] * num + coeffsB[numIndex]) % totalFPs

			if numHashCode < minHashCode:
				minHashCode = numHashCode

		signatures.append(minHashCode)
		numIndex += 1

	return signatures

def cmpMinHashPair(minHash1, minHash2):

	numIndex = 0
	numEqual = 0

	while numIndex < len(minHash1):
		if minHash1[numIndex] == minHash2[numIndex]:
			numEqual += 1

		numIndex += 1

	return numEqual * 1.0 / len(minHash1)

def testCompMinHash():
	coeffsA = [1, 3]
        coeffsB = [1, 1]

        S1 = [0, 3]
        S2 = [2]
        S3 = [1, 3, 4]
        S4 = [0, 2, 3]

        print compMinHash1(S1, coeffsA, coeffsB, 5)
        print compMinHash1(S2, coeffsA, coeffsB, 5)
        print compMinHash1(S3, coeffsA, coeffsB, 5)
        print compMinHash1(S4, coeffsA, coeffsB, 5)




if __name__ == '__main__':
	numCoeffs = int(sys.argv[1])
	strSave = sys.argv[2]

	coeffsA, coeffsB = generateCoeffs(numCoeffs)
	dumpCoeffsToFile(coeffsA, coeffsB, strSave)


