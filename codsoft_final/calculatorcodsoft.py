print("THIS IS A SIMPLE CALCULATOR:")

while True:
    a=int(input("Enter a number of your choice:\n"))
    b=int(input("Enter another number of your choice:\n"))
    i=int(input("Enter\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for modulus\n"))
    if i==1:
      result=a+b
      print("The addition of two numbers is:\n",result)
    elif i==2:
      result=a-b
      print("The subtraction of two numbers is:\n",result)
    elif i==3:
      result=a*b
      print("The multiplicaton of two numbers is:\n",result)
    elif i==4:
      result=a/b
      print("The division of two numbers is:\n",result)
    elif i==5:
      result=a%b
      print("The modulus of two numbers is:\n",result)
    else:
        print("INVALID INPUT!!!")
    choice=input("Enter \ny to continue using the calculator\nn for exiting\n")
    if choice=='n':
      break

