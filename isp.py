def cnt_of_factors(a):
    c=0 
    for i in range(1,int(a**0.5)+2):
        if a%i==0:
            if a%i==a:
                c+=1
        else:
            c+=2
    return c 

A=[4,1,2,5,7,9]

for i in A:
    print(cnt_of_factors(i))






# for str(i)  in range(1000,10000):
#     if i[::-1]==i:
#         print(i)








# # def isp(n):
# #     for i in range(2,int(n**(0.5))-1):
# #         if n%i==0:
# #             return False 
        
# #     return True 
# # a=int(input())
# # for i in range(2,a):
# #     if isp(i)==True:
# #         print(i)
# print([i for i in "101"])