from collections import defaultdict
from minHash import *
from sets import Set
import random
import sys


class LSH:
	def __init__(self, n=100, b=20, r=5):
		self._n = n
		self._b = b
		self._r = r
		self._cache = [defaultdict(list) for i in range(b)]

	@staticmethod
	def getLSH(minHashSig, b, r):
		lsh = []

		#r = self._r
		#b = self._b
		for i, band in enumerate(range(b)):
			lsh.append(hash(tuple(minHashSig[i*r: i*r + r])))

		return lsh

	def insertLSH(self, lsh, doc_id):
		for i, band_bucket in enumerate(lsh):
			if doc_id not in self._cache[i][band_bucket]:
				self._cache[i][band_bucket].append(doc_id)

	def searchLSH(self, lsh):
		searchList = []
		for i, band_bucket in enumerate(lsh):
			if band_bucket in self._cache[i]:
				searchList = searchList + self._cache[i][band_bucket]

		return list(Set(searchList))	


	def printStat(self):		
		b = self._b

		for i in range(b):
			print 'BAND', i, len(self._cache[i])
			for key in self._cache[i]:
				print key, self._cache[i][key]
			print

		print 



if __name__ == '__main__':
	print 'hello world'	
