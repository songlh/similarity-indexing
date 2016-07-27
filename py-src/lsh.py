from collections import defaultdict
from minHash import *
import random
import sys


class LSH:
	def __init__(self, n=100, b=20, r=5):
		self._n = n
		self._b = b
		self._r = r
		self._cache = [defaultdict(list) for i in range(b)]

	def getLSH(self, minHashSig):
		lsh = []

		r = self._r
		b = self._b
		for i, band in enumerate(range(b)):
			lsh.append(hash(tuple(minHashSig[i*r: i*r + r])))

		return lsh

	def insertLSH(self, lsh, doc_id):
		for i, band_bucket in enumerate(lsh):
			if doc_id not in self._cache[i][band_bucket]:
				self._cache[i][band_bucket].append(doc_id)




if __name__ == '__main__':
	sFileName1 = sys.argv[1]
	sFileName2 = sys.argv[2]

	fp1 = sparseListFromFile(sFileName1)
	fp2 = sparseListFromFile(sFileName2)

	coeffsA, coeffsB = generateCoeffs(100)

	minHash1 = minHash_1(fp1, coeffsA, coeffsB)
	minHash2 = minHash_1(fp2, coeffsA, coeffsB)

	#print minHash1
	#print minHash2

	print cmpMinHashPair(minHash1, minHash2)

	compLSH = LSH()

	print compLSH.getLSH(minHash1)
	print compLSH.getLSH(minHash2)
