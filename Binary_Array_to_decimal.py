x=int(input())
lst=list(map(int,input().split()))
s=0
for i in lst:
    s=s*10+i
a=str(s)    
print(int(a,2))
