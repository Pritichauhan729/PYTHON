#---------------------------------------------------------------------------------------------------------------------------------------#
#                                                           MODULE - 4                                                                  #
#---------------------------------------------------------------------------------------------------------------------------------------#

# What is File function in python? What is keywords to create and write file.
"""
ANS = 
    Python has a built-in open() function to open a file. This function returns a file object, also called a handle,
    as it is used to read or modify the file accordingly.

    EXAMPLE :
    >>> f = open("test.txt")    # open file in current directory
    >>> f = open("C:/Python38/README.txt")  # specifying full path
"""
# Write a Python program to read an entire text file.

"""
ANS =
 def file_read(fname):
    txt = open(fname)
    print(txt.read())

file_read('test.txt')
"""
# Write a Python program to append text to a file and display the text.
"""
ANS =
def Appendtext(fname):
	with open(fname,'a+') as f:
		f.write('appending line 1, ')
		f.write('appending line 2. ')
	f.close()
Appendtext('file1.txt')

x= open('file1.txt')
print(x.read())
"""
# Write a Python program to read first n lines of a file.
"""
ANS =
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)
"""
# Write a Python program to read last n lines of a file.
"""
ANS =
def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')
if __name__ == '__main__':
    fname = 'File1.txt'
    N = 3
    try:
        LastNlines(fname, N)
    except:
        print('File not found')
"""
# Write a Python program to read a file line by line and store it into a list
"""
ANS =
Let the content of the file data_file.txt be

honda 1948
mercedes 1926
ford 1903

- Source Code

with open("data_file.txt") as f:
    content_list = f.readlines()
print(content_list)
content_list = [x.strip() for x in content_list]
print(content_list)

- Output

['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
['honda 1948', 'mercedes 1926', 'ford 1903']
"""
# Write a Python program to read a file line by line store it into a variable.
"""
ANS = 
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')
"""
# Write a python program to find the longest words.
"""
ANS =
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))
"""
# Write a Python program to count the number of lines in a text file.
"""
ANS =
with open(r"myfile.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)
"""
# Write a Python program to count the frequency of words in a file.
"""
ANS =
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))
"""
# Write a Python program to write a list to a file.
"""
ANS =
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())

- OUTPUT:
Red                                                                                                           
Green                                                                                                         
White                                                                                                         
Black                                                                                                         
Pink                                                                                                          
Yellow
"""
# Write a Python program to copy the contents of a file to another file.
"""
ANS =
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
	for line in firstfile:
			secondfile.write(line)
"""
-----------------------------------------------------------------------------------------------------------------------------------------
# EXCEPTION HANDLING
-----------------------------------------------------------------------------------------------------------------------------------------
# Explain Exception handling? What is an Error in Python?
"""
ANS =
    Exception and Error in Python :

    Errors are the problems in a program due to which the program will stop the execution. On the other hand, 
    exceptions are raised when some internal events occur which changes the normal flow of the program. 

    - Two types of Error occurs in python. 
    1) Syntax errors
    2)Logical errors (Exceptions) 
"""
# How many except statements can a try-except block have? Name Some built-in exception classes:
"""
ANS =
    There has to be at least one except statement.

    - SOME BUILT-IN EXCEPTION CLASSES:
    1) Exception	
    2) ImportError
    3) IndexError	
    4) KeyError	
    5) MemoryError
    6) NameError
    7) LookupError
    8) OverflowError
    9) RuntimeError
    10) SyntaxError
    11) SystemError
"""
# When will the else part of try-except-else be executed?
"""
ANS =
    The else part is executed when no exception occurs.
"""
# Can one block of except statements handle multiple exception?
"""
ANS =
    In Python, try-except blocks can be used to catch and respond to one or multiple exceptions. 
    In cases where a process raises more than one possible exception, they can all be handled using a single except clause.
"""
# When is the finally block executed?
"""
ANS = 
    finally block is always executed after leaving the try statement. 
    In case if some exception was not handled by except block, it is re-raised after execution of finally block. 
    finally block is used to deallocate the system resources.
"""
# What happens when „1‟== 1 is executed?
"""
ANS =
    It simply evaluates to false and does not raise any exception.
"""
# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
"""
ANS =
    In Python, exceptions can be handled using a try statement. 
    The critical operation which can raise an exception is placed inside the try clause. 
    The code that handles the exceptions is written in the except clause.

- Code:
a = ["Python", "Exceptions", "try and except"]  
try:  
    #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
     for i in range( 4 ):  
        print( "The index and element from the array is", i, a[i] )  
except:  
    print ("Index out of range")  

Output:
The index and element from the array is 0 Python
The index and element from the array is 1 Exceptions
The index and element from the array is 2 try and except
Index out of range
"""
# Write python program that user to enter only odd numbers, else will raise an exception.
"""
ANS =

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
"""
# What are oops concepts? Is multiple inheritance supported in java
"""
ANS =
    - Multiple Inheritance is a feature of an object-oriented concept, 
    - where a class can inherit properties of more than one parent class. 
    - The problem occurs when there exist methods with the same signature in both the superclasses and subclass.

    - For Example,
    Consider a scenario where A, B, and C are three classes. 
    The C class inherits A and B classes. If A and B classes have the same method and you call it from child class object, 
    there will be ambiguity to call the method of A or B class.

    - Since compile-time errors are better than runtime errors, 
    Java renders compile-time error if you inherit 2 classes. 
    So whether you have same method or different, there will be compile time error.

class A{  
void msg(){System.out.println("Hello");}  
}  
class B{  
void msg(){System.out.println("Welcome");}  
}  
class C extends A,B{//suppose if it were  
   
 public static void main(String args[]){  
   C obj=new C();  
   obj.msg();//Now which msg() method would be invoked?  
}  
}  
"""
# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
"""
ANS =
Defining a Class: 
   - A class in Python can be defined using the class keyword.
   - Class is defined using the class keyword followed by the ClassName1 and : operator after the class name, 
     which allows you to continue in the next indented line to define class members.

SYNTAX:
class <ClassName1>:
    <statement1>
    <statement2>
    .
    <statementN>

__init__() function:
    - To understand the meaning of classes we have to understand the built-in __init__() function.
    - __init__() function is used to assign values to object properties

Self in Python class:
    - Self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. 
    - It binds the attributes with the given arguments.
    - To understand the meaning of classes we have to understand the built-in __init__() function.
    - __init__() function is used to assign values to object properties

EXAMPLE OF CLASS:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
"""
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
"""
ANS =
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
"""
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
"""
ANS =
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
"""
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
"""
ANS =
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
"""
# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
"""
ANS =
INHERITANCE:
- Inheritance relationship defines the classes that inherit from other classes as derived, subclass, or sub-type classes. 
- Base class remains to be the source from which a subclass inherits. 
- For example, you have a Base class of “Animal,” and a “Lion” is a Derived class. The inheritance will be Lion is an Animal.  

EXAMPLE(Creating a Parent Class):

class Person(object):
  def __init__(self, name, id):
    self.name = name
    self.id = id
  def Display(self):
    print(self.name, self.id)
emp = Person("Satyam", 102) 
emp.Display()

INIT:
   "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. 
   This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

CONSTRUCTOR:
    - Constructors are generally used for instantiating an object. 
    - The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 
    - In Python the __init__() method is called the constructor and is always called when an object is created.
"""
# What is Instantiation in terms of OOP terminology?
"""
ANS =
    In the OOP language, instantiation describes the processes of creating a new object for a class using a new keyword.
"""
# What is used to check whether an object o is an instance of class A?
"""
ANS =
    - Using isinstance() function, we can test whether an object/variable is an instance of the specified type 
      or class such as int or list.
    
    - In the case of inheritance, we can checks if the specified class is the parent class of an object. 
    - For example, isinstance(x, int) to check if x is an instance of a class int .
"""
# What relationship is appropriate for Course and Faculty?
"""
ANS =
    "ASSOCIATION" Relationship is appropriate for Course and Faculty.
"""
# What relationship is appropriate for Student and Person?
"""
ANS =
    "INHERITANCE" Relationship is appropriate for Student and Person.
"""
