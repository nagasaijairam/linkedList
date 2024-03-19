def reverse_the_array(Array,i,j):
    while(i<j):
        Array[i],Array[j]=Array[j],Array[i]
        i+=1 
        j-=1    
    return Array
      

def main():
    Array=list(map(int,input().split()))
    k=int(input())
    n=len(Array)-1
    k=k%(len(Array))
    reverse_the_array(Array,0,n)
    reverse_the_array(Array,0,k-1)
    reverse_the_array(Array,k,n)
    print(Array)

main()