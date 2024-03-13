A=int(input())
ans=[i for i in range(A+1)] 
ans[0],ans[1]=-1,-1
           
c=0
for  i in range(2,A+1):
    if ans[i]==i:
        c+=1
        for j in range(i*i,A+1,i):
            ans[j]=-1
ansf=[]
for i in range(0,A,2):
    if ans[i+1] != -1 :
        ansf.append(ans[i+1])
print(ansf)  