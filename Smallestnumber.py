A=int(input('Enter the first numbers:'))
B=int(input('Enter the second numbers:'))
C=int(input('Enter the third numbers:'))

if A<B and A<C:
    print('A is the smallest number', A)
          
elif B<C and B<A:
    print('B is the smallest number', B)

else:
    print('C is the smallest number', C)


