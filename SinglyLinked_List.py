class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3 

head = node1  
 
current = head

while current is not None:
    print(current.data)
    current = current.next
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
  

  
    ## ALGORITHMS ##
    
# 1. ListSize(): Returns the number of nodes in the linked list.
def list_size(self):
    return self.size

# 2. IsEmpty(): Checks whether the linked list is empty or not.
def is_empty(self):
    if self.size == 0:
        return True
    else:
        return False
    
# def is_empty(self):
#     return self.size == 0

# 3. Get(Position): Returns the data of the node at a particular position.    
def get(self, position):
    current = self.head
    count = 1

    while count < position:
        current = current.next
        count += 1

    return current.data

# 4. PositionOf(x): Searches for a node with a specific value and returns its position.
def position_of(self, x):
    current = self.head
    count = 1

    while current is not None:
        if current.data == x:
            return count
        
        current = current.next
        count += 1

    return -1  # Value not found


## Insertion ##
# Case 1: Insert at the beginning of the linked list.

def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

#case 2: Insert at the end of the linked list.
def insert_at_end(self, data):
    new_node = Node(data)      
    
    current = self.head
    
    while current.next is not None:
        current = current.next
    
    current.next = new_node
    self.size += 1  
    
#case 3: Insert at a specific position in the linked list.
def insert_at_position(self, position, data):
    if position < 1 or position > self.size + 1:
        print("Invalid position")
        return

    new_node = Node(data)

    if position == 1:
        new_node.next = self.head
        self.head = new_node
    
    else:
        current = self.head
        count = 1

        while count < position - 1:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node

    self.size += 1  
    
    
    
## Deletion ##
def delete(self, position):

    if position < 1 or position > self.size:
        print("Wrong Position")
        return

    # Case 1: Delete the first node
    if position == 1:
        self.head = self.head.next

    # Case 2: Delete the last node
    elif position == self.size:
        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    # Case 3: Delete from the middle
    else:
        current = self.head
        count = 1

        while count < position - 1:
            current = current.next
            count += 1

        current.next = current.next.next

    self.size -= 1
    

## Output ##
def output(self):
    current =self.head
   
    while current is not None:
        print(current.data)
        current = current.next  
        
    print()      
      

my_list = LinkedList()

my_list.insert(1, 10)
my_list.insert(2, 20)
my_list.insert(3, 30)
my_list.insert(4, 40)

my_list.output()

my_list.insert(3, 25)
my_list.output()

my_list.delete(2)
my_list.output()