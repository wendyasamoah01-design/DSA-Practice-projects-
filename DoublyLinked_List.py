class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)   

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

head = node1
tail = node3


## Transversal

# Forward Traversal
current = head

while current is not None:
    print(current.data)
    current = current.next
    
#    Backward Transversal
current = tail

while current is not None:
    print(current.data)
    current = current.prev
    
    
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
            ##  Algorithms  ##

    # 1. ListSize(): Returns the number of nodes in the linked list.     
    def list_size(self):
        return self.size
    
    # 2. IsEmpty(): Checks whether the linked list is empty or not.
    def is_empty(self):
        return self.size == 0

    #3. Get(Position): Returns the data of the node at a particular position.
    def get(self, position):
        if position < 1 or position > self.size:
            return "Wrong Position"

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

        return -1


    # 5. Insert(Position, x): Inserts a new node with the value x at a specific position.
    def insert(self, position, x):
        if position < 1 or position > self.size + 1:
            print("Wrong Position")
            return

        new_node = Node(x)
        
        # Case 1: Insert at the beginning
        if position == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node
            else:
                self.tail = new_node

            self.head = new_node
        
        # Case 2: Insert at the end
        elif position == self.size + 1:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        # Case 3: Insert in the middle
        else:
            current = self.head
            count = 1

            while count < position - 1:
                current = current.next
                count += 1

            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

        self.size += 1

    # 6. Delete(Position): Removes a node at a specific position.
    def delete(self, position):
        if position < 1 or position > self.size:
            print("Wrong Position")
            return
        
        # Case 1: Delete the first node
        if position == 1:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
       
        # Case 2: Delete the last node
        elif position == self.size:
            self.tail = self.tail.prev
            self.tail.next = None
        
        # Case 3: Delete from the middle
        else:
            current = self.head
            count = 1

            while count < position - 1:
                current = current.next
                count += 1

            current.next = current.next.next
            current.next.prev = current

        self.size -= 1


    # 7. Output(): Outputs the data of all nodes from left to right.  
    def output(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

    def output_backward(self): #  display the list backwards
        current = self.tail

        while current is not None:
            print(current.data, end=" ")
            current = current.prev

        print()


    
    
# Question: Student Records Management

# Write a Python program using a doubly linked list to store student ID numbers.

# Your program should:
# 1. Create an empty doubly linked list.
# 2. Insert 2001, 2002, 2003, and 2004.
# 3. Display the list from beginning to end.
# 4. Display the list from end to beginning.
# 5. Display the size of the list.
# 6. Search for 2003 and display its position.
# 7. Insert 2005 at position 2.
# 8. Delete the node at position 4.
# 9. Display the final list.
# 10. Check whether the list is empty.    
        
my_list = DoublyLinkedList()

my_list.insert(1, 10)
my_list.insert(2, 20)
my_list.insert(3, 30)
my_list.insert(4, 40)

my_list.output()

my_list.insert(3, 25)
my_list.output()

my_list.delete(2)
my_list.output()

my_list.output_backward()           
