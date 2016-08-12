
import sys
from os import listdir
from os.path import join, isfile
import shutil

if __name__ == '__main__':
	sSrcDirectory = sys.argv[1]
	sDstDirectory = sys.argv[2]
	numFiles = int(sys.argv[3])

	onlyfiles = [join(sSrcDirectory, f) for f in listdir(sSrcDirectory) if isfile(join(sSrcDirectory, f)) and f.endswith('.bb')]

	count = 0

	for f in onlyfiles:
		shutil.copy2(f, sDstDirectory)
		count += 1
		if count == numFiles:
			break
				
