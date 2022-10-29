n=int(input())
l=list(map(int,input().split()))
s=int(sum(l)/len(l))
if s in l:
    print(True)
else:
    print(False)