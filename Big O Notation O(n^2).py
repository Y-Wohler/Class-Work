import time
from random import randrange

def minimumValue(values):
	overallMin = values[0]
	for i in values:
		smallest = True
		for j in values:
			if i > j:
				smallest = False
		if smallest:
   			overallMin = i
	return overallMin

for listSize in range (100, 1001, 100):
	values = [randrange(1000) for x in range(listSize)]
	start = time.time()
	print(minimumValue(values))
	end = time.time()
	print("size: %d time: %f" % (listSize, end-start))