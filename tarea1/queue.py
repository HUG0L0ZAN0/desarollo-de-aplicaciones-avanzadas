class Queue:
    def __init__ (self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("la queue esta vacia")
        return self.data.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("la queue esta vacia")
        return self.data[0]
    
    def is_empty(self):
        return len(self.data) == 0
    

queue = Queue()

print("esta vacio?", queue.is_empty())

queue.enqueue(5)
queue.enqueue(10)
print("el arreglo despues del enqueue", queue.data)
print("el front del queue:", queue.peek())
print("el dequeue:", queue.dequeue())
print("despues del dequeue:", queue.data)
print("esta vacio?", queue.is_empty())
