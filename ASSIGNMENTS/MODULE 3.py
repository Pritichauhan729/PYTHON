#---------------------------------------------------------------------------------------------------------------------------------------#
#                                                           MODULE - 3                                                                  #
#---------------------------------------------------------------------------------------------------------------------------------------#

---------------------------------------------
# LIST
---------------------------------------------
# What is List? How will you reverse a list?
"""
ANS - A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. 
-Each element or value that is inside of a list is called an item. 
-Just as strings are defined as characters between quotes, 
-lists are defined by having values between square brackets [ ] .

REVERSING A LIST :
Every list in Python has a built-in reverse() method you can call to reverse the contents of the 
list object in-place. Reversing the list in-place means won't create a new list and copy the existing 
elements to it in reverse order.

EXAMPLE :
>>> mylist = [1, 2, 3, 4, 5]
>>> print(mylist)
>>> mylist.reverse()
O/P--[5, 4, 3, 2, 1]
"""

# How will you remove last object from a list?
"""
ANS - You can use list.pop() method to remove the last element from the list.

"""
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
"""
ANS - 25
Explanation: -1 corresponds to the last index in the list.
"""
# Differentiate between append () and extend () methods?
"""
ANS - 1). Python append() method adds an element to a list, and the extend() method concatenates the 
first list with another list (or another iterable). When append() method adds its argument as a single 
element to the end of a list.

2).The length of the list itself will increase by one. Whereas extend() method iterates over its argument
adding each element to the list, extending the list. The length of the list will increase by however
many elements were in the iterable argument.
"""
#Write a Python function to get the largest number, smallest num and sum of all from a list.

"""
ANS - lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
total = 0
for ele in range(0, len(lst)):
    total = total + lst[ele]
 
# printing total value
print("Sum of all elements in given list: ", total)

"""

# How will you compare two lists?
"""
ANS - There are three ways to compare two lists :

1)Using list.sort() and == operator. The list. ...
2)Using collections.Counter() This method tests for the equality of the lists by comparing frequency
of each element in first list with the second list. ...
3)Using == operator. This is a modification of the first method.

"""

#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given list of strings.
"""
ANS - def match_words(words):
  element = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      element += 1
  return element

print(match_words(['abc', 'xyz', 'aba', '1221']))

"""
# Write a Python program to remove duplicates from a list.
"""
ANS - a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

"""
# Write a Python program to check a list is empty or not.
"""
ANS - def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1
 
# Driver Code
lis1 = []
if Enquiry(lis1):
    print("The list is not empty")
else:
    print("Empty List")
"""
# Write a Python function that takes two lists and returns true if they have at least one common member.
"""
ANS - def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
"""
# Write a Python program to generate and print a list of first and last 5
#elements where the values are square of numbers between 1 and 30.
"""
ANS - def Values():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

Values()
"""
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""
ANS - def unique(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique([1,2,3,3,3,3,4,5])) 
"""
# Write a Python program to convert a list of characters into a string.
"""
ANS - s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)
"""

# Write a Python program to select an item randomly from a list.
"""
ANS - import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))
"""
# Write a Python program to find the second smallest number in a list.
"""
ANS - def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length-1])
    print("Smallest element is:", list1[0])
    print("Second Largest element is:", list1[length-2])
    print("Second Smallest element is:", list1[1])
 
# Driver Code
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)
"""
# Write a Python program to get unique values from a list
"""
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)
"""
# Write a Python program to check whether a list contains a sub list
"""
ANS - def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))
"""
# Write a Python program to split a list into different variables.
"""
ANS - color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)
"""
-------------------------------------------------
# TUPLE
-------------------------------------------------
# What is tuple? Difference between list and tuple.
"""
ANS - In Python, tuples are allocated large blocks of memory with lower overhead, 
since they are immutable; whereas for lists, small memory blocks are allocated. 
Between the two, tuples have smaller memory. 
This helps in making tuples faster than lists when there are a large number of elements.
"""
# Write a Python program to create a tuple with different data types.
"""
ANS - data = ("data", True, 3.2, 150)
print(data)
"""
# Write a Python program to create a tuple with numbers.
"""
ANS - data = 2 , 4 , 6, 20 , 67
print(data)
#Create a tuple of one item
data = 18,
print(data)
"""
# Write a Python program to convert a tuple to a string.
"""
ANS - data = ('s', 'h', 'e', 'e', 'r', 'i', 'n')
string =  ''.join(data)
print(string)
"""

#Wri te a Python program to check whether an element exists within a tuple.
"""
ANS - data = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in data)
print(5 in data)

"""
# Write a Python program to find the length of a tuple.
"""
ANS - tuplex = tuple("w3resource")
print(tuplex)
#use the len() function to known the length of tuple
print(len(tuplex))
"""

# Write a Python program to convert a list to a tuple.
"""
ANS - lst = [5, 10, 7, 4, 15, 3]
print(lst)
#use the tuple() function built-in Python, passing as parameter the list
data = tuple(lst)
print(data)
"""
# Write a Python program to reverse a tuple.
"""
ANS - x = (2, 4, 6)
result = reversed(x)
result = tuple(result)
print(result)
"""
# Write a Python program to replace last value of tuples in a list.
"""
ANS - data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in data])
"""
# Write a Python program to find the repeated items of a tuple.
"""
ANS - data = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(data)
#return the number of times it appears in the tuple.
count = data.count(4)
print(count)
"""
# Write a Python program to remove an empty tuple(s) from a list of tuples.
"""
ANS - L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)
"""
# Write a Python program to unzip a list of tuples into individual lists.
"""
ANS - l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))
"""
-----------------------------------------------------
# DICTIONARY
------------------------------------------------------
# Write a Python program to convert a list of tuples into a dictionary.

"""
ANS - tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
result = dict(tuples)
print(result)
"""

# How will you create a dictionary using tuples in python?
"""
ANS - To convert a tuple to dictionary in Python, use the dict() method. 
A dictionary object can be constructed using a dict() function.
The dict() function takes a  tuple of tuples as an argument and returns the dictionary.
"""
# How will you create a dictionary using tuples in python?
"""
To convert a tuple to dictionary in Python, use the dict() method. 
A dictionary object can be constructed using a dict() function. 
The dict() function takes a tuple of tuples as an argument and returns the dictionary.
"""
# Write a Python script to sort (ascending and descending) a dictionary by value.
"""
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
"""
# Write a Python script to concatenate following dictionaries to create a new one.
"""
ANS - data1={1:10, 2:20}
data2={3:30, 4:40}
data3={5:50,6:60}
data4 = {}
for d in (data1, data2, data3): data4.update(d)
print(data4)
"""
# Write a Python script to check if a given key already exists in a dictionary.
"""
ANS - d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
"""
# How Do You Traverse Through A Dictionary Object In Python?
"""
ANS - There are two ways of iterating through a Python dictionary object. 
-One is to fetch associated value for each key in keys() list. 
-There is also items() method of dictionary object which returns list of tuples,
each tuple having key and value.
"""
# How Do You Check The Presence Of A Key In A Dictionary?
"""
ANS -Using has_key() method returns true if a given key is available in the dictionary.
-Otherwise, it returns a false. 
-With the Inbuilt method has_key(), use the if statement to check if the key is present in the dictionary or not.
"""
# Write a Python program to check multiple keys exists in a dictionary
"""
ANS - student = {
  'name': 'sheerin',
  'branch': 'python',
  'enroll_id': '10'
}
print(student.keys() >= {'branch', 'python'})
print(student.keys() >= {'name', 'sheerin'})
print(student.keys() >= {'enroll_id', 'name'})
"""
# Write a Python script to merge two Python dictionaries
"""
ANS - d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)
"""
# Write a Python program to map two lists into a dictionary
"""
ANS - keys = ['sheerin', 'helly', 'shweta']
values = ['graphics','gaming', 'datadesign']
student_dictionary = dict(zip(keys, values))
print(student_dictionary)
"""
# Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200,’d’:400}
"""
ANS - d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}

for i, j in d1.items():

    for x, y in d2.items():

        if i == x:

            d3[i]=(j+y)

print(d3)

Myresults = {'a': 400, 'b': 400}
"""
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).
"""
ANS -
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
"""
# Write a Python program to print all unique values in a dictionary.
"""
ANS - L = [{"":"S0010"}, {"V": "S0020"}, {"VI": "S0010"}, {"VI": "S0050"}, {"VII":"S0050"}, {"V":"S0090"},{"VIII":"S0070"}]
print("Original List: ",L)
unique_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",unique_value)
"""
# Why Do You Use the Zip () Method in Python?
"""
ANS - Python's zip() function creates an iterator that will aggregate elements from two or more 
iterables.
-You can use the resulting iterator to quickly and consistently solve common programming problems, 
like creating dictionaries.
"""
# Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.
#Sample data: {'1': ['a','b'], '2': ['c','d']}
#Expected Output:
#ac ad bc bd
"""
ANS - import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
"""
# Write a Python program to find the highest 3 values in a dictionary
"""
ANS - from collections import Counter
my_dict = {'A': 50, 'B': 45, 'C': 200,
           'D': 150, 'E': 125, 'F': 90}
 
k = Counter(my_dict)
high = k.most_common(3)
 
print("Initial Dictionary:")
print(my_dict, "\n")
 
 
print("Dictionary with 3 highest values:")
print("Keys: Values")
 
for i in high:
    print(i[0]," :",i[1]," ")
"""
# Write a Python program to combine values in python list of dictionaries.
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300},
#{'item': 'item1', 'amount': 750}]
#Expected Output: Counter ({'item1': 1150, 'item2': 300})
"""
ANS - from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result) 
"""
# Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. Sample string: 'w3resource'
#Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""
ANS - s = input("Enter a string: ")
dict = {} 
for ch in s:
    if ch in dict: 
        dict[ch] += 1
    else:
        dict[ch] = 1 
for key in dict:
    print(key,':',dict[key])
"""
# Write a Python function to calculate the factorial of a number (a nonnegative integer)
"""
ANS - def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
n=int(input("Enter a Number : "))
print(fact(n))

"""
# Write a Python function to check whether a number is in a given range
"""
ANS - def test_range(n):
    if n in range(8,15):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(12)
"""
# Write a Python function to check whether a number is perfect or not.
"""
ANS - def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect(28))
"""
# Write a Python function that checks whether a passed string is palindrome or not
"""
ANS -def Palindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(Palindrome('mam')) 

"""
# How do you perform pattern matching in Python? Explain
"""
ANS -STEPS FOR REGULAR EXPRESSION MATCHING :
1)Import the regex module with import re.
2)Create a Regex object with the re. compile() function. ...
3)Pass the string you want to search into the Regex object's search() method. ...
4)Call the Match object's group() method to return a string of the actual matched text.

EXAMPLE:
search_string = "sheerinshaikh"
pattern = "sheerin"
match = re.match(pattern, search_string)
#If-statement after search() tests if it succeeded
if match:
   print("regex matches: ", match.group())
else:
   print('pattern not found')
O/P:
regex matches: sheerin
"""
# What is lambda function in python? What we call a function which is incomplete version of a function?
"""
ANS - LAMBDA FUNCTION :
- A Lambda Function in Python programming is an anonymous function or a function having no name. 
- It is a small and restricted function having no more than one line. 
- Just like a normal function, a Lambda function can have multiple arguments with one expression.


"""
# How Many Basic Types Of Functions Are Available In Python?
"""
ANS - Python function types
There are two basic types of functions: 
1) built-in functions and user defined functions.
The built-in functions are part of the Python language; for instance dir, len, or abs. 
2) The user defined functions are functions created with the def keyword.
"""
# How can you pick a random item from a list or tuple?
"""
ANS - In Python, you can randomly sample elements from a list with choice() , sample() , and choices()
of the random module. These functions can also be applied to a string and tuple. 
 
- choice() returns one random element, and sample() and choices() return a list of multiple random
 elements.
"""
# How can you pick a random item from a range?
"""
ANS - randrange() function is used to get a random integer number from the given exclusive range by 
specifying the increment. For example, random. randrange(0, 10, 2) will return any random number 
between 0 and 20 (like 0, 2, 4, 6, 8).
"""
# How can you get a random number in python?
"""
ANS - To generate random number in Python, randint() function is used. 
This function is defined in random module.
"""
# How will you set the starting value in generating random numbers?
"""
ANS - seed() method to customize the start number of the random number generator.
EXAMPLE:
import random

random.seed(10)
print(random.random())

random.seed(5)
print(random.random())

"""
# How will you randomizes the items of a list in place?
"""
ANS - The shuffle() method randomizes the items of a list in place.
EXAMPLE :
import random

list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ",  list)

random.shuffle(list)
print ("Reshuffled list : ",  list)

O/P :
Reshuffled list : [16, 5, 10, 20]
reshuffled list : [20, 5, 10, 16]
"""
# Write a Python program to read a random line from a file.
"""
ANS - import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('Fruit_Store.py'))

"""
# Write a Python program to convert degree to radian
"""
ANS -pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

"""

# Write a Python program to calculate the area of a trapezoid
"""
ANS - a = 5
b = 6
height = float(input("Height of trapezoid: "))
a = float(input('Base one value: '))
b = float(input('Base two value: '))
area = ((a + b) / 2) * height
print("Area is:", area)
"""

# Write a Python program to calculate the area of a parallelogram
"""
ANS - 
base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)
"""
# Write a Python program to calculate surface volume and area of a cylinder
"""
ANS -
pi=22/7
h = float(input(' Enter Height of cylinder: '))
r = float(input(' Enter Radius of cylinder: '))
volume = pi * r * r * h
surface_area = ((2*pi*r) * h) + ((pi*r**2)*2)
print("Volume of cylinder is: ", volume)
print("Surface Area of cylinder is: ", surface_area)

"""

# Write a Python program to returns sum of all divisors of a number
"""
ANS -
def div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(div(15))
print(div(20))

"""

# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
"""
ANS -
from decimal import *
data = list(map(Decimal, '3.6 9.5 1.15 8.9 3.56 4.90 0.75'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))

"""
