class Stack:
    def __init__(self): 
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("el stack esta vacio")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("el stack esta vacio")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0
    


stack = Stack()

print("esta vacio?", stack.is_empty())  

stack.push(5)
stack.push(10)

print("el arreglo despues del push", stack.data)

print("el top del stack:", stack.peek())

print("el pop:", stack.pop())

print("despues del pop:", stack.data)

print("esta vacio?", stack.is_empty())
