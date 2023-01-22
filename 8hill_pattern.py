# hill patterns has 3 triangles
# 1 with no value decreasing triangle
# 2  with some sumbol increasing triangle
# 3  with increasing triangle having some value

n = int(input('Enter the number of rows'))


# this code have a little bug which is resolved in the 2nd code

# 1
for i in range(n):

    # for printing reverse triangle having non value
    for j in range(i,n):
        print(' ',end='')


    # for printing triangle
    for j in range(i+1):
        print('*',end='')

    # for printing triangle
    for j in range(i+1):
        print('*',end='')

    print()


# 2 
for i in range(n):

    # for printing reverse triangle having non value
    for j in range(i,n):
        print(' ',end='')


    # for printing triangle
    for j in range(i):
        print('*',end='')

    # for printing triangle
    for j in range(i+1):
        print('*',end='')

    print()
