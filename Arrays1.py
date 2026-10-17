A=[]
B=[]
C=[]

print("Enter 5 numbers for list A:")
for i in range(5):
    num=int(input())
    A.append(num)
    
print("Enter 5 numbers for list B:")
for i in range(5):
    num=int(input())
    B.append(num)    
    
    
for i in range(5):
    C.append(A[i] + B[i]) 
    
print("List A = ", A)    
print("List B = ", B)
print("List C = ", C)       
    
    
    