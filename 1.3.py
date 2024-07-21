n=int(input())
y=5
c=1
for x in range(1,n):
    y=5-x
    if c>n:
        break
    for y in range(y,0,-1):
        print(" ",end=" ")
        y=y-1
    j=0
    for j in range(j,x) :
        if c>n:
          break
        print(" ",c,end=" ")
        c=c+1
        j=j+1
    print("")
    x=x+1