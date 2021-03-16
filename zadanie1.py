from random import randint

randList = [randint(0, 100) for x in range(10)]
randList.sort()
print(randList)

evenRand = [x for x in randList if x%2==0]
print(evenRand)