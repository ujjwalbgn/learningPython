class myClass():            #define a class 
  def method1(self):        #define method
    print("myClass Method1")

  def method2(self, someString):
    print("myClass Method 2 "+ someString)

class anotherClass(myClass):    #define a class
  def method1(self):            
    myClass.method1(self)       #inheriting a function from another class 
    print("anotherClass Method1")

  def method2(self, someString):
    print("AnotehrClass Method 2 ")

def main():
  c = myClass()
  c.method1()

  c.method2("This is a string")

  c2 = anotherClass()
  c2.method1()
  
  
if __name__ == "__main__":
  main()
