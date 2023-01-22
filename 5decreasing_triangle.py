# taking input from the user
n=int(input('Enter the number of rows'))

for i in range(n):
    # using i and n here
    for j in range(i,n):
        print('*',end=' ')
    print()