## 1.IsEmpty(): Checks whether the list is empty or not
# def is_empty(stack):
#     return len(stack) == 0

# # 2. Push(x): Adds an element x to the top of the stack
# def push(stack, x):
#     stack.append(x)
    
# # 3. Pop(): Removes and returns the top element of the stack
# def pop(stack):
#     if len(stack) == 0:
#         print("Stack Underflow")
#         return

#     return stack.pop()    


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"

        return self.items.pop()

    def output(self):
        print(self.items)
        


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.output()

print(s.pop())

s.output()        