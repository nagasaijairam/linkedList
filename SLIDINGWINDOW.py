A=list(map(int,input().split()))
B=int(input())
res=0
summ=0
for i in range(B) :
    summ+=A[i]
n=len(A)
min_sum=summ
for i in range(B,n) :
    summ+=A[i]-A[i-B]
    if(summ<min_sum) :
        min_sum=summ
        res=i-B+1
print(res)