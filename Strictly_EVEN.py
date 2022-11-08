n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    if i%2==0 and l[i]%2==0:
        s=s+1
v=[i for i in l if i%2==0]    
if s==len(v):
    print(True)
else:
    print(False)