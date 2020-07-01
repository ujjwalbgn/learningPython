##   Hello World  ##
# baisc Hello World
# print('Hello World') #this also works on python
print("Hello World")
#define main which prints Hello World
def main():
    print("Hello World from main")
main() #calling the main function 




##   Variables  ##
print("\n\nVariables:")
# Declare a variable and initialize it
f =0
print(f)
# re-declaring the variable works
f = "abc"
print(f)

# ERROR: variables of different types cannot be combined
# ERROR: print("this is a string " + 123 )   #this style works in JS
# Proper way to do  this 
print("This is a string " + str(123) )




## Array ##
print("\n\nArrays")
days = ["Mon","Tue","Wed","Thu","Fri","Sat"]
print(days)  # this will print arrays in array format

#printing all elements of an array
for d in days: 
    print(d)


##  Fucntions ##
print("\n\nFucntions:")
# function that takes arguments
def printArgs(arg1,arg2):
    print(arg1,arg2)

# function that returns a value
def cube(x):
    return x*x*x

# calling functions
printArgs("Hello my name is","Ujjwal.")
print(cube(3))

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with vaiable number of arguments
def multi_add(*args):   # '*' means we can pass in variable number of arguments   
    result = 0 
    for x in args:
        result = result + x
    return result

# examples printing function with default value for an argument
print(power(2))  # here x=1(default value) and 2^1 is printed
print(power(2,3)) # here x=3 and 2^3 is printed
print(power(x=3,num=2)) # this also works as arguments are passed with values and python interpreter figures which arugments to supply the value to 
print(multi_add(2,4,6,7,3))



## Conditionals ## 
print("\n\nConditional:")
x, y = 100, 100

# conditional flow uses if, elif, else  
if(x < y):
    st = "x is less than y"
elif(x == y):
    st = "x is the same as y"
else:
    st ="x is greater than y"
print(st)

# python doesn't have switch cases



## Loops ##
print("\n\nLoops")
# python only has for and while loop

# define a while loop
x = 0
while(x <5):
    print(x)
    x+=1  # there is no x++ operater in python

# define a for loop
for x in range(5,10):
    print(x)

# use the break and continue statements
for x in range(5,30):
    #if (x == 7): break  # when x ==7 loop will end and next block of code will execute 
    if (x %2 == 0) : continue # when x == even number, loop will go back to start and run again ignoring the even numbers and only printing odd numbers
    print(x)

#using the enumerate() function to get index 
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

for i,d in enumerate(days):
    print(i,d)