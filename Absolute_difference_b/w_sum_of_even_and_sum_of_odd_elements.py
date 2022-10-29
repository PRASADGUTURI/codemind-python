n=int(input())
l=list(map(int,input().split()))
m=0
n=0
for i in l:
    if i%2==0:
        m=m+i
        
    else:
        n=n+i
        
print(abs(m-n))        