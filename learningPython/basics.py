##   Hello World  ##
# baisc Hello World
# print('Hello World') #this also works on python
print("Hello World")
#define main which prints Hello World
def main():
    print("Hello World from main")
main() #calling the main function 



##   Variables  ##
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




##  Fucntions ##
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
# examples printing function with default value for an argument
print(power(2))  # here x=1(default value) and 2^1 is printed
print(power(2,3)) # here x=3 and 2^3 is printed
print(power(x=3,num=2)) # this also works as arguments are passed with values and python interpreter figures which arugments to supply the value to 