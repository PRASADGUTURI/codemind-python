n=int(input())
l=list(map(int,input().split()))
f=0
x,y=map(int,input().split())
for i in l:
    if x>i or y<i:
        f=1
        print(i,end=" ")
if f==0:
    print(-1)

#print(k)        
        