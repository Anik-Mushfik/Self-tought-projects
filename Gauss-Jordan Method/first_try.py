""" 
This program works like a calculator of Gauss-Jordan Method. 
It conducts the method to get the row echelon form and 
the reduced row echelon form. 

There is already a library called sympy which does those methods and other features.

This progarm does almost the same but will be making it from scratch.
"""

n,m=map(int,input().split())
a=n*[m*[0]]
j=0
for i in range (0,n):
    a[i][j]=map(int,input().split())
    j+=1
j=0
for i in range (0,n):
    print(a[i][j])
    j+=1