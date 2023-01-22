# specify the number of rows
# by taking input 
n = int(input("Enter the number of rows"))

# looping upto number of rows
for i in range(0,n):
    for j in range(0,i+1):
        print('e',end=' ')
    print()