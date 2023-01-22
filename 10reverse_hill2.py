# it contains 3 triangles
# 1 is simple triangle with no value
# 2 is decreasing reverse triangle with value
# 3 is increasing reverse triangle with value


# taking input for number of rows
n=int(input("Enter the number of rows"))


for i in range(n):

    # simple triangle with no value
    for j in range(i+1):
        print(' ',end="")


    # reversed triangle with having value
    # here we have n-1 so loop will print 1 less star
    for j in range(i,n-1):
        print('*',end="")


    # reversed triangle with some value
    for j in range(i,n):
        print('*',end="")

    print()