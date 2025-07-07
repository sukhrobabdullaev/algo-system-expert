from xxlimited import Null


class Stack: 
    def __init__(self) -> None:
        self.stack=[]

    def push(self, element) -> None: 
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
             return "Stack is empty"
        return self.stack[-1] 
    def isEmpty(self): 
        return len(self.stack)==0
    def size(self): 
        return len(self.stack)

myStack=Stack()

myStack.push("A")
myStack.push("B")
myStack.push("C")

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())


class Stack2: 
    def __init__(self, cap) -> None:
        self.cap=cap;
        self.top=-1
        self.a=[None]*cap
    def push(self, x):
        if self.top >= self.cap - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.a[self.top] = x
    def pop(self):
        if self.top < 0:
            print("Stack Underflow")
            return None
        popped = self.a[self.top]
        self.a[self.top] = None
        self.top -= 1
        return popped
    def peek(self):
        if self.top < 0:
            print("Stack is Empty")
            return None
        return self.a[self.top]
    def isEmpty(self): 
        return self.top<0
    def __repr__(self) -> str:
        return f"{self.a}"

s1 = Stack2(5)
s1.push(10)
s1.push(20)
s1.push(30)

popped = s1.pop()
if popped is not None:
    print(f"{popped} popped from stack")

peeked = s1.peek()
if peeked is not None:
    print(f"Top element is: {peeked}")

print("Elements present in stack:")
while not s1.isEmpty():
    top_elem = s1.peek()
    if top_elem is not None:
        print(f"{top_elem}")
    s1.pop()
print(s1.pop() + " popped from stack");

print("Top element is:", s1.peek());

print("Elements present in stack:");
while not s1.isEmpty():
  print(s1.peek() + " ");
  s1.pop();
