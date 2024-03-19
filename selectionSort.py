A = list(map(int, input().split()))

for i in range(0, len(A)):
    index = -1
    maxi = 63 ** 10  
    for j in range(i, len(A)):
        if A[j] < maxi:
            maxi = A[j]
            index = j
    A[i], A[index] = A[index], A[i]

print(A)











# print(A)    
