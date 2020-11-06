import math


    a = int(input('выбор действия'))
    if a==1:
    x=int(input('введите x '))
    y=x**3-64*x*(x**3/x**2)
    print(y)
elif a==2:
    x1=int(input("x1="))
    x2=int(input("x2="))
    x3=int(input("x3="))
    z=pow(x1,2)
    x=pow(x2,2)
    c=pow(x3,2)
    v=(z+x+c)-100
    print(v)
  
elif a==3:
    x1=int(input("x1="))
    x2=int(input("x2="))
    z=pow(x1,x2)
    x=pow(x2,x1)
    c=z*x
    y=sqrt(c)
    print(y)
  
else a==4:
    x1 = int(input("введите первое значение ")
    x2 = int(input("введите второе значение "))
    x3 = int(input("введите третье значение "))
    x4 = int(input("введдите четвертое значение "))
    y = ((x1**2)/(x2**4))-pow(x3,x4)
  print(y)

           
