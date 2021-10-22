class Stack:
    def __init__(self, limit):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def isFull(self):
        return len(self.stk) >= self.limit

    def size(self, limit):
        self.limit *= 2

    def push(self, item):
        if self.isFull():
            print("Increasing size of stack")
            self.size(self.limit)
        self.stk.append(item)
        print("Stack currently:", self.stk)

    def pop(self):
        if self.isEmpty():
            print("Error: Stack is Empty")
        else:
            return self.stk.pop()

    def peek(self):
        if self.isEmpty():
            print("Error: Stack is empty")
        else:
            return self.stk[-1]


new_stack = Stack(1)
new_stack.push("1")
new_stack.push("2")
new_stack.push("4")
new_stack.push("5")
new_stack.push("10")

new_stack.push("15")
new_stack.pop()
print(new_stack.peek())

new_stack.push("11")
new_stack.push("hi")
new_stack.push("how")
print(new_stack.isFull())
new_stack.push("are")
print(new_stack.isFull())
print(new_stack.isEmpty())

new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.peek()
new_stack.push("hello")
