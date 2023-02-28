#program that returns the sum of all even numbers from a given list

#import reduce
from functools import reduce

#given values
values = [1,2,3,4,5,6,7,8,9,10]

#use the filter function to get all even numbers
even_list = list(filter(lambda x : x % 2 == 0, values))

#use the reduce function to calculate the sum of all even numbers
sum = reduce(lambda x,y : x + y, even_list)
print(sum)