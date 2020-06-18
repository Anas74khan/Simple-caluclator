
def add():
    m=0
    n=float(input("Enter numbers: "))
    if(n>0):
       while True:
          m=m+n
          n=int(input("+"))
          if(n==0):
             break
    return m
    
def sub():
    m=0
    n=float(input("Enter numbers: "))
    if(n>0):
       while True:
           m=m-n
           n=int(input("-"))
           if(n==0):
               break
    return m    
    
def div():
    m=float(input("Division only supports operation between 2 numbers enter numbers: "))
    n=float(input("/"))
    if(n>0 and m>0):
       m=m/n
    else:
        s="number should be greater than 0"
        return s
    return m  
 
def mul():
    m=1
    n=float(input("Enter numbers: "))
    if(n>0):
       while True:
           m=m*n
           n=int(input("*"))
           if(n==0):
               break
    else:
        s="number should be greater than 0"
        return s
    return m  

val="y"
while val=="y":    
    print('What would you like to perform')
    print("1 Addition\n2 Subtraction\n3 Multiplication\n4 Division")
    x=int(input("Choose[1-4]: "))
    print("enter 0 to get the answer")
    if(x==1):
        print(f"Answer is: {add()}")
    if(x==2):
        print(f"Answer is: {sub()}")
    if(x==3):
        print(f"Answer is: {mul()}")
    if(x==4):
        print(f"Answer is: {div()}")
    val=input("If you want to do other operations enter y or enter any other key to exit: ")
