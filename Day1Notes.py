#--------------------------------
#
# Signup
# https://cted.cybbh.io/tech-college/pns/public/pns/latest/inded.html
#
# Student GUIDE
# https://cted.cybbh.io/tech-college/pns/public/pns/latest/guides/fg.html
#
#--------------------------------

#the print function - this is what a function will look like
print(1)
# if you ever need to lookup something, the help function takes one or more parameters and can assist in lookup.
help()
#boolean - true or false
bool()
#type function will return what type of object is presented to the parameters
type(5)
# variable is an expression or what is contained within
a = 5
print(a)
# the above makes "a" 5.

print(type(a))

#floats are numbers that are not whole, numbers that contain decimals

b = 5.3
print(type(b))

#string is a set/array of characters
print(type("hello"))
print("This is another way of presenting/printing a string")
#strings always have quotes around them.

#lists
list()
lst = [1,2,3,4,5] # has square brackets
h = list(1,2,3,4,5)
emptyl = [] # this is how you create an empty list
#lists are also mutable - as in you can change and modify them.

# control "/" will auto-comment/uncomment blocks

tuple() #tuple function is an immutable collection (or list)
tup = (1,2,3,4,5)
tup


# cannot mix two object or operand types
# can however multiply strings to return that number of strings
'abc' * 5
# will return 'abcabcabcabcabc'

a=4
b=5
a+b
c=a+b

c

#lists and indexing
alist = [1,2,3,4,5]
alist

alist[0] #this calls the index of the input
#in this situation it would call the first item in the collection
#output: 1

alist[-1] # will return the last value in the collection

alist.append() #adds to a list
# del alist[] # deletes item at a given index

blist =[5, 2.3, "string", [1,2,3,4,5], (7,8,9), True]
blist # you can have multiple different objects within a list

blist[3] # will return the list
blist[3][2] #returns the third index of the list within blist
blist.pop() #returns the last item of the list and removes the last item.

#type conversions 
str(4.2) #will return as a string
str_flt = str(4.2) #converts a float into a string
int_flt = int(5.9) #conversta a float into an integer
int_flt

flt_str = float('9.5') # converts a string into a float
int_str = int('4') #string to int
#etcetcetcetc

# regular division is known as float division in python
# it will always return a float object
5/2 # returns the float 5.2
8/2 # still returns a float

# to do integer division you'll have to 
7//2 #this will return an integer

#modulus does division and returns the remainder
5%2 #returns 1

10%2 == 0 #boolean return of if it is equal to

"hello. my name is {}. that's{}. and he's {}.".format("Larry", "Curly", "Moe")
#positional insertion based on where the '{}' exists and the .format list / collection

name = "alber"
day = "today"

"hello {}. How are you {}".format(name, day)
#returns the full sentence based on vars

f"Hello{name}, how are you{day}"

PI = '{:.2f}'.format(3.14592635359)
#format specification mini language - this is something you can do to return only the first two digits after the decimal
PI
string_list = list("hello world") #converts a string into a list
print(string_list)

tup_string = tuple(string_list)
tup_string

hw = "hello world"
hw.split() # splits a str and a list of substrings
#output would ['hello', 'world']

hw = "hello world how are you"
hw.split()
# output: ['hello', 'world', 'how', 'are', 'you']
hw.replace(" ", ":") #out with the old and in with the new
# in the replace, the pairs are .replace("find","replace")
# so this will be 
hw_colon = hw.replace(" ", ":")
# hw colon returns:: hello:world:how:are:you

hw_colon.split(":")
#this will split on the colon

s = "hello" 

s[0]
#will return 'h'
s = s.replace("h", "j")

# s[0] = "j" this will not function because strings do not support item assignment
lst = list(s)
lst
lst[0] = "J"
# this will function because a list does have item assignment

''.join(lst) #creates a string from a list
#the args are: "''" the divider/separator and then the var that you want to join

#line breaks
print("hello");print ("world")


a = 5
print(f"I ran {a} miles today.")

input() # this is the command/operand to input something
name2 = input("What is your name?")
# will prompt user for input
name