from math import log

numInt = int(input("Enter the number of integers you are entering"))
elements = numInt
mainList = []

while numInt != 0:
	numInt -= 1
	val = int(input("Enter value"))
	mainList.append(val)


bubTime = int(2 * pow(elements,2))
insertTime = int(pow(elements,2))
mergeTime = int(elements * log(elements,10))

method = 0

if bubTime < insertTime and mergeTime:
	method = 1
elif insertTime < bubTime and mergeTime:
	method = 2
elif mergeTime < bubTime and insertTime:
	method = 3
else:
	method = 0

class Sort:
	def __init__(self, mainList, method):
		if method == 1:
			self.__bubble(mainList)
		elif method == 2:
			self.__insertion(mainList)
		elif method == 3:
			self.__merge(mainList)
		else:
			print("Invalid integer, Please retry")

	def __bubble(self, mainList):
		exchanges = True
		self.passnum = len(mainList)-1
		while self.passnum > 0 and exchanges:
			exchanges = False
			for i in range(self.passnum):
				if mainList[i]>mainList[i+1]:
					exchanges = True
					temp = mainList[i]
					mainList[i] = mainList[i+1]
					mainList[i+1] = temp
			self.passnum = self.passnum-1

	def __insertion(self, mainList):
		for i in range(1,len(mainList)):
			while i > 0 and mainList[i-1] > mainList[i]:
				mainList[i], mainList[i-1] = mainList[i-1], mainList[i]
				i -=1
		return mainList

	def __merge(self, mainList):
		if len(mainList) > 1:
			mid = len(mainList) // 2
			lefthalf = mainList[:mid]
			righthalf = mainList[mid:]

			self.__merge(lefthalf)
			self.__merge(righthalf)

			i = 0
			j = 0
			k = 0

			while i < len(lefthalf) and j < len(righthalf):
				if lefthalf[i] < righthalf[j]:
					mainList[k] = lefthalf[i]
					i = i + 1
				else:
					mainList[k] = righthalf[j]
					j = j + 1
					k = k + 1

			while i < len(lefthalf):
				mainList[k] = lefthalf[i]
				i = i + 1
				k = k + 1

			while j < len(righthalf):
				mainList[k] = righthalf[j]
				j = j + 1
				k = k + 1

newObj = Sort(mainList,method)
print(mainList)