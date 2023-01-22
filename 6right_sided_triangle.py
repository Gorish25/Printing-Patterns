# the right sided triangel have 2 triangles
# 1 is the triangle with having no value
# 2 is the triangle have value


# taking input
n = int(input('Enter the number of rows'))

for i in range(n):

    # reverse triangle having no value
    for j in range(i,n):
        print('',end=' ')

    # triangle having value
    for j in range(i+1):
        print('*',end='')

    print()