import random
import time

# input, some random unsorted array, random numbers from random.org
# you can also use generateRandomArray() function, which takes 2 params: length and max number
unsortedArray = [7647,3397,8423,7025,9562,2410,1971,779,4790,4384,213,4899,675,8038,5048,8395,8275,9048,3424,2235,3172,3374,4645,9296,1860,280,2883,6093,1893,1128,2128,3559,2495,7372,4677,5086,8987,6907,326,8615,7390,1440,489,2225,7797,4371,6132,9523,9934,1723,5047,4099,6123,6212,2866,1088,6480,1404,9869,1931,8888,4929,1967,5848,8675,137,8694,8477,1433,6071,6953,1975,5362,3861,9142,392,3832,5923,5509,9464,9069,1448,7042,8771,5338,6960,8667,6423,9686,4486,2410,6284,134,344,8873,9379,6338,5971,4479,3703]

def generateRandomArray(length, maxNum):
    array = []
    for i in range(length + 1):
        array.append(random.randrange(maxNum))
    return array

# find the biggest number of array
def findBiggest(array):
    biggest = 0
    for element in array:
        if element > biggest:
            biggest = element
    return biggest

# sorting algo
def sort(array):
    biggest = findBiggest(array)        # get biggest number
    newArray = []                       # new array for return n shit
    for i in range(biggest + 1):        # iterate over all numbers from 0 to the biggest found, because we want to assign that number to newArray[] if it matches
        for j in array:                 # iterate over elements in array
            if(i == j):                 # if element in array matches the number "i",
                newArray.append(i)      # append it to the newArray[]
    return newArray                     # return newArray lol

# start timer 
start_time = time.time()

# compute results
result = sort(unsortedArray)                            # (uncomment if you want to sort defined array)  
#result = sort(generateRandomArray(1000, 1000))         # (uncomment if you want to sort random array)

# stop timer
end_time = time.time()

# print results
# !!! WARNING !!!
# this can take a fuckton of time when using big arrays (actually a LOT longer than actual computing)  
#print(result)          # uncomment to see sorted array

print("Computation took", end_time - start_time, "seconds")