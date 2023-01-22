# this triangle also have 2 triangles 
# 1 is triangle having no value
# 2 is triangle having given value

n=int(input("Enter the number of rows"))


# 
for i in range(n):
    
    # triangle having no value
    for j in range(i+1):
        print('',end=' ')

    # reverse triangle having given value
    # starting with i to n
    for j in range(i,n):
        print('*',end='')

    print()