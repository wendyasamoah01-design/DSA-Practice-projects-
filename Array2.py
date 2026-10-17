num=[]
total=0

print("Enter a set of numbers for list arr")

for i in range(5):
    values = int(input("Enter a set of numbers for list arr"))
    num.append(values)
    
    
for i in range(5):
    total+= total + num[i]    
2

print("Your list is ", num )    

print("Sum : ", total)
    