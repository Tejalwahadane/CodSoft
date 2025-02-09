def calc():
    print("*********Menu*********")
    print("1.Addition(+)\n2.Subtraction(-)\n3.Division(/)\n4.Multiplication(*)")
    ch=int(input("Enter your Choice : "))
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    
    if ch==1:
        print("Result is :",num1+num2)
        calc()
    
    elif ch==2:
        print("Result is :",num1-num2)
        calc()
        
    elif ch==3:
        if num2==0:
            print("Erro:- Denominator can not be zero")
            calc()
        else:
            print("Result is :",num1/num2)
            calc()
    
    elif ch==4:
        print("Result is :",num1*num2)
        calc()
        
    else:
        print("Invalid Choice " )
        exit
calc()
