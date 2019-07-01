import itertools as itl
import numpy as np
import matplotlib.pyplot as plt
import time


# slide 7: For/While loops
print "Slide 7"

#1
totalSum = 0
for n in range(1,1001):
    totalSum += n
print totalSum

#2
n = 10**6
ans = 0
while n > 1:
    n = n/2.0
    ans += 1
print ans

#3

num_list = [0, 5 ,2, 2, 4,7, 7, 8, 10, 10, 4, 11, 2, 12, 14]
total  = 0
for index, n in enumerate(num_list):
     if n == index: total += n
print total
print ""


# slide 12 : lists/tuples
print "Slide 12:"
list1 = list(range(0,11))
print list1[0:-3]
print list1[1::2]

s = range(1,10)* 2
s[9:] = s[:8:-1]
s = s + s
print s

print ""


# slide 15: Dictionaries/sets

print "Slide 15:"
#1)
dictionary = dict(zip(range(1,100), range(251,350)))
cummsum = 0
for key in dictionary.keys():
    if key % 2 == 0: cummsum += dictionary[key]
print "sum: " + str(cummsum)


#2)
num1 = 13176834768764271478714761221294
num2 = 12980180239829082389012392389190

digits1 = set(str(num1))
digits2 = set(str(num2))

print (digits1 - digits2) | (digits2 - digits1)
## or similarly range(0,10) - (digits1 & digits2)
print ""




# slide 19  : functions/lambda
print "Slide 19: "
#1)
def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    for div in range(2, int(np.sqrt(n)) + 1):
        if n % div == 0: return False
    return True

#2)
primes = filter(lambda x: isPrime(x), range(1,10**5))

#3)
primeStrings = [str(x) for x in primes]

digitCounts = [0]*10
for prime in primeStrings:
    for digit in prime:
        digitCounts[int(digit)] += 1
print digitCounts
print ""




# slide 26 : Recursion

print "Slide 26"

def ColSeq(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + ColSeq(n/2)
    else:
        return 1 + ColSeq(3*n + 1)

#maxLength = 0
#bestNum = 0
#for n in range(1, 10**6):
#    nextLength = ColSeq(n)
#    if nextLength > maxLength:
#        maxLength = nextLength
#        bestNum = n
#print "done!"
#print ""





#slide 28: file-parsing
#import sys
#orig_stdout = sys.stdout
#f = open('/Users/zackmcnulty/Desktop/out.txt', 'w')
#sys.stdout = f

#for line in reversed(list(open("/Users/zackmcnulty/Desktop/iGEM/Class?/SSH/python_test_files/p067_triangle.txt"))):
    #print line

#sys.stdout = orig_stdout
#f.close()

#with(open("/Users/zackmcnulty/Desktop/iGEM/Class?/SSH/python_test_files/slide28_triangle.txt")) as inputFile:
 #   last = inputFile.next().split(" ")
  #  last = [float(x) for x in last]
   # for line in inputFile:
    #    nums = line.split(" ")
     #   nums = [float(x) for x in nums]
      #  for index in range(0, len(nums)):
       #     nums[index] += max(last[index], last[index + 1])
        #last = nums
        #if len(nums) == 1: print nums

#1)
with(open("/Users/zackmcnulty/Desktop/iGEM/journals/labjournal/SSH_zack_temp/find_the_i.txt")) as inputFile:
    lineNum = 1
    for line in inputFile:
        for char in line:
            if char == "I": print "lineNum: ", lineNum
        lineNum += 1

#2)
import sys
with(open("/Users/zackmcnulty/Desktop/success.txt", 'w')) as f:
    orig_stdout = sys.stdout
    sys.stdout = f
    print "I did it!"
    sys.stdout = orig_stdout
    f.close()





# slide 33: Numpy

#1
a1 = np.ones((6,6))
a1[1:5,1:5] = 0
print a1

#2

a2 = np.transpose(np.array([(np.sqrt(2)/2, np.sqrt(3)/2, 1.0/2), (np.sqrt(2)/2, 1.0/2, np.sqrt(3)/2)]))
newArray = np.zeros((3,2))
newArray[:,0] = np.sqrt(a2[:,0]**2 + a2[:,1]**2)
newArray[:,1] = np.arctan(a2[:,1] / a2[:,0])
print newArray


# slide 36 itertools
print "slide 36: "

#1)
l1 = [1,2,3,4,5,7,11,13,17,21,32,34,45,54,54,65,12,32]
keys = []
groups = []
for k,g in itl.groupby(l1, isPrime):
    keys.append(k)
    groups.append(list(g))
primeStreaks = filter(lambda x: x[0], zip(keys,groups))
print "max cons primes:", max([len(x[1]) for x in primeStreaks])
print ""

#2)
cards = range(2,10) * 4 + [11] * 4 + [10] * 16
hands = list(itl.combinations(cards, 2))
blackjacks = filter(lambda x: x[0] + x[1] == 21, hands)
probOfBlackJack = len(blackjacks) * 1.0 / len(hands)
print probOfBlackJack



#slide 39

print "Slide 39: "
#part 1)
peteGames = [sum(x) for x in itl.product(range(1,5), repeat = 4)]
colinGames = [sum(y) for y in itl.product(range(1,7), repeat = 3)]

plt.subplot(1,2,1)
plt.hist(peteGames)
plt.subplot(1,2,2)
plt.hist(colinGames)
plt.show()

#part 2)
peteWins = filter(lambda x: x[0] > x[1], itl.product(peteGames, colinGames))
probWinning = 1.0*len(peteWins)/(len(peteGames)*len(colinGames))
print probWinning
print "" 