# it is the collection of up hill and down hill

n=int(input("Enter the number of rows"))


# up hill
for i in range(n):

    for j in range(i,n):
        print(' ',end='')


    for j in range(i):
        print('*',end='')

    for j in range(i+1):
        print('*',end='')

    print()


# down hill
for i in range(n):


    for j in range(i+1):
        print(' ',end='')


    for j in range(i,n-1):
        print('*',end='')


    for j in range(i,n):
        print('*',end='')    

    print()

# in the above program we donot get a diamond with left and right corners




# for that the second program is given below
# in this we have changed the row condition to n-1 

# up hill
for i in range(n-1):

    for j in range(i,n):
        print(' ',end='')


    for j in range(i):
        print('*',end='')

    for j in range(i+1):
        print('*',end='')

    print()


# down hill
for i in range(n):


    for j in range(i+1):
        print(' ',end='')


    for j in range(i,n-1):
        print('*',end='')


    for j in range(i,n):
        print('*',end='')    

    print()
