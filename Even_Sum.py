n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    if i%2==0:
        k=k+i
print(k)        