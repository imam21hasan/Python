'''
*
**
***
'''
n = int(input("Enter the value of n : "))
for i in range(1, n+1):
    print(i*"*")


'''
  *
 **
***
'''
n = int(input("Enter the value of n : "))
for i in range(1, n+1):
    print((n-i)*" "+i*"*")


'''
*
***
*****
'''
n = int(input("Enter the value of n : "))
for i in range(1, n+1):
    print((2*i-1)*"*")


'''
    *
  ***
*****
'''
n = int(input("Enter the value of n : "))
for i in range(1, n+1):
    print((2*n-2*i)*" "+(2*i-1)*"*")


'''
  *
 ***
*****
'''
n = int(input("Enter the value of n : "))
for i in range(1, n+1):
    print((n-i)*" "+(2*i-1)*"*")


'''
*****
 ***
  *
'''
n = int(input("Enter the value of n : "))
for i in range(n, 0, -1):
    print((n-i)*" "+(2*i-1)*"*")
