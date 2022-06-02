def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
a=int(input())    
b=a*a
c=reverse(a)
d=c*c
e=reverse(d)
print(b==e)