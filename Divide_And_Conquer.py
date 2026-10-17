#Sort the given unsorted list.

def merge_sort(numbers):
    if len(numbers) <=1: #Base Case
        return numbers
    
    mid= len(numbers)//2 # Divide
    
    left = numbers[:mid]
    right= numbers[mid:]
    
    left = merge_sort(left) # Conquer
    right = merge_sort(right)
    
    return merge(left,right) #Combine
    
def merge(left,right):
    result=[]
    
    i,j= 0,0
    
    while i < len(left)and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])     
            i +=1
            
        else:
            result.append(right[j])
            j +=1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result           

numbers=[38,27,43,3,9,82,10]

sorted_numbers=merge_sort(numbers)

print("Original list:", numbers)
print("Sorted list:", sorted_numbers)