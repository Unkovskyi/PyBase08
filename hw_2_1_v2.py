#Task 2_1_upd


import math #Импорт библиотеки math что бы потом воспользоватся квадратным корнем sqrt

a=float(input('input a: '))
b=float(input('input b: '))
c=float(input('input c: '))

if a==0:
    print('This is a linear equation.Solution of the equation {}x+{}=0'.format(b,c))
    x=(0-c)/b
    print('x =',x)
else:
    D=pow(b,2)-4*a*c
    if D==0:
        print('The equation has only one solution')
        x_1=-b/(2*a)
    elif D>0:
        print('Solution of the equation {}x^2+{}x+{}=0'.format(a,b,c))
        x_1=((-b+math.sqrt(D))/(2*a))
        x_2=((-b-math.sqrt(D))/(2*a))
    else:
        print('The equation has a solution only in the field of complex numbers')
        x_1=((-b+pow(D,0.5))/(2*a))
        x_2=((-b-pow(D,0.5))/(2*a))


    print('Discriminant= ',D)
    print('x1 =',x_1)
    print('x2 =',x_2)
