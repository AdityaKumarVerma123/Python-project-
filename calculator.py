 # python program to create a simple calculator

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def divide(num1,num2):
    return num1 / num2

def multiply(num1,num2):
    return num1 * num2

def avg(num1,num2):
    return (num1 + num2)/2

print("please select a operation:-\n 1.addition,\n 2.subtraction,\n3. divide,\n 4. multiply,\n5. avrage..!")

select = int(input("select a operation from 1,2,3,4,5:"))

number1 = int(input("enter your first number :-"))
number2 = int(input("enter your second number :-"))

if  select == 1:
    print(number1 ,"+", number2,"=",\
          add(number1,number2))
    

elif  select == 2:
    print(number1 ,"-", number2,"=",\
          sub(number1,number2))
    
elif  select == 3:
    print(number1 ,"/", number2,"=",\
          divide(number1,number2))
    
elif  select == 4:
    print(number1 ,"*", number2,"=",\
          multiply(number1,number2))
    
elif  select == 5:
    print("(",number1 ,"+", number2,")","/","2","=",\
          avg(number1,number2))
    
else :
    print("invailid operation! please select again!")
    

    

