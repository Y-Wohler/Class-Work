import time
from random import randrange

def minimumValue(values):
	miniVal = values[0]
	for i in values:
		if i < miniVal:
   			miniVal = i
	return miniVal

for listSize in range (100, 1001, 100):
	values = [randrange(1000) for x in range(listSize)]
	start = time.time()
	print(minimumValue(values))
	end = time.time()
	print("size: %d time: %f" % (listSize, end-start))