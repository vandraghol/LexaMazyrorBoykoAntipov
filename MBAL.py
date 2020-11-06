import math

a = int(input('выбор действия'))
if a==1:
x=int(input('введите x '))
y=x**3-64*x*(x**3/x**2)
print(y )
elif a==2:
  
elif a==3:
    x1 = int(input("введите первое число:" ) )
    x2 = int(input("введите второе число:" ) )
    x3 = int(input("введите третье число:") )
    z=pow(x1,2)
    c=pow(x2,2)
    b=pow(x3,2)
    i=(z+c+b)-100
    print(i)
  
else a==4:
  x1 = int(input("введите первое значение ")
  x2 = int(input("введите второе значение "))
  x3 = int(input("введите третье значение "))
  x4 = int(input("введдите четвертое значение "))
  y = ((x1**2)/(x2**4))-pow(x3,x4)
  print(y)
