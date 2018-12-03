#Task 2_4

d='y'
while d=='y':
    d=input('Want to output Fibonacci number y/n: ')

    if d=='y':
        n=int(input('Input number Fibonacci: '))
        if n<3:
            sum_previous=1
        else:
            first_fibo=1 # первое число Фибоначи
            second_fibo=1 # второе число Фибоначи
            i=2
            while i<n:
                sum_previous=first_fibo+second_fibo
                first_fibo=second_fibo
                second_fibo=sum_previous
                i+=1
        print('The Fibonacci number {} is {}'.format(n,sum_previous))

print('OK, bye')
