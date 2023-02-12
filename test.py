def maxdivpos(k):
    res=0
    n = int(input())
    if(n==0): return 0
    while(n!=0):
        n=int(input())
        if (n>0 and k%n==0 and n>res):
            res=n
    return res