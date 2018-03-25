def minimumTime(x):
    n = len(x)
    n = int(n/2)
    min_dist = 0
    el = x[n]
    for i in x:
        min_dist = min_dist + abs(i-el)
    return min_dist


t = int(input())
while t!=0 :
    n = int(input())
    x = input().split()
    k=0
    for i in x:
        x[k] = eval(i)
        k+=1
    x.sort()
    ans = minimumTime(x)
    print(ans)
    t-=1
    
