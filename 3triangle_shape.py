# taking input
n= int(input('Enter the number of rows'))

# here we use 3 for loops 
# first for rows
# inside first 2 for loops which is 
# one is for printing space and other is for printing pattern
 
for i in range(0,n):
    for j in range(0,n-i-1):
        print('*')