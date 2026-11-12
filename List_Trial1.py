# Write a Python program that manages a list of students' marks using the seven functions we have studied.
# Your program must do the following:
# 1. Check whether the list is empty using is_empty().
# 2. Display the number of marks using list_size().
# 3. Display the mark at index 2 using get().
# 4. Search for the mark 55 using index_of().
# 5. Insert the mark 75 at index 3 using insert().
# 6. Delete the mark at index 1 using delete().
# 7. Display all the marks using output().


marks = [65,70,80,55,90]

def is_empty(marks):
    return not marks

print(is_empty(marks))

#print(len(marks))

def list_size(marks):
    size = 0
    
    for i in range (len(marks)):
        size +=1
        
    return size

print(list_size(marks))   

def get(marks,index):
    if index >= 0 and index < len(marks):
        return marks[index]
    
    else:
        return "Wrong Index"
    
print (get(marks,2))  


def index(marks , x): 
    for i in range(len(marks)) :
        if marks[i] == x:
            return i
        
        
    return " Wrong Index"
        
print(index(marks ,65))   


def insert(marks, index ,x):
    if index < 0 or index > len(marks) :
          print("Wrong index")
          return
          
    marks.append(None)   
    
    for i in range(len(marks) - 1 , index ,- 1):
       marks[i] = marks[i-1] 
       
    marks[index] = x
    
print(insert(marks, 3, 75))
print(marks)   


def delete(marks,index):
    if index < 0 or index >= len(marks):
            print("Wrong index")
            return
        
    for i in range (index,len(marks)-1):
        marks[i] = marks[i+1]
        
    marks.pop()  
    
print(delete(marks ,1))     
    
    
def output(marks):
    for i in range(len(marks)):
        print(marks[i], end=" ")    
        
output(marks)  
          

    
       
          
        

