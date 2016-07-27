import sys
import os
from os import listdir
from os.path import isfile, join
from tools import *


def listFromFile(sFileName):
	fp = [0] * FEATURE_SIZE
	ffpFile = open(sFileName, 'r')

	sFirstLine = ffpFile.readline()
	sSecondLine = ffpFile.readline()

	iNum = int(sFirstLine)

	if iNum < 10 or iNum > 168005:
		ffpFile.close()
		return []

	while True:
		line = ffpFile.readline()
		if not line:
			break

		numList = line.split()
		fp[int(numList[0])] = 1

	assert sum(fp) == iNum

	ffpFile.close()
	return fp


def listFromDirectory(sDirectory):
	listFPs = []
	fpFiles = []

	onlyfiles = [join(sDirectory, f) for f in listdir(sDirectory) if isfile(join(sDirectory, f)) and f.endswith('.bb')]

	for sFileName in onlyfiles:
		listTmp = listFromFile(sFileName)

		if len(listTmp) > 0:
			listFPs.append(listTmp)
			fpFiles.append(sFileName)

	return listFPs, fpFiles

def sparseListFromFile(sFileName):
	fp = []
	ffpFile = open(sFileName, 'r')

	sFirstLine = ffpFile.readline()
	sSecondLine = ffpFile.readline()

	iNum = int(sFirstLine)

	if iNum < 10 or iNum > 168005:
		ffpFile.close()
		return []

	while True:
		line = ffpFile.readline()
		if not line:
			break

		numList = line.split()
		fp.append(int(numList[0]))

	assert len(fp) == iNum

	ffpFile.close()
	return fp

def sparseListFromDirectory(sDirectory):
	listFPs = []
	fpFiles = []

	onlyfiles = [join(sDirectory, f) for f in listdir(sDirectory) if isfile(join(sDirectory, f)) and f.endswith('.bb')]

	for sFileName in onlyfiles:
		listTmp = sparseListFromFile(sFileName)

		if len(listTmp) > 0:
			listFPs.append(listTmp)
			fpFiles.append(sFileName)

	return listFPs, fpFiles

