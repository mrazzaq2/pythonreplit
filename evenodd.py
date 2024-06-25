print('lets find the given number is even or odd')

def even_or_odd(Number):
    if Number % 2 == 0:
        print('Even')
    else:
        print('Odd')

num = int(input("Enter a number: "))
result = even_or_odd(num)

