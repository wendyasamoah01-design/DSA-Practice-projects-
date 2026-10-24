# Write a program that uses all the operations of Lists.The operations include: len(), Insert(index,x), pop(),, Display() 

num=[2,4,6,8,10]
print(num)

print(not num) # Isempty(): Checks whether the list is empty or not

print(len(num)) #ListSize(): returns the number of elements in the list

print(num.index(8)) #indexOf(x): returns the index of the value "8"

print(num[4]) #get(index): returns the element in the position of index

num.pop(4-2+1)  # delete(index): removes or deletes the element in the position of index
print(num)

num.insert(3,7) # insert(index,x): inserts the element x in the position of the index
print(num)

print("The final list is" , num) #output(): Outputs the list elements from left to right


