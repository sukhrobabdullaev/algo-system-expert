// Stack - LIFO

/*
    [1,2,3,4,5]

    5
    4
    3
    2
    1 
*/
class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  peek() {
    this.items[this.items.length - 1];
  }

  pop() {
    return this.items.pop();
  }

  is_empty() {
    return this.items.length() === 0;
  }

  size() {
    return this.items.length();
  }
}

let s = new Stack();
s.push("John");
s.push("Alisher");
s.push("Umid");

console.log(s.items);

class Stack2 {
  constructor(cap) {
    this.cap = cap;
    this.top = -1;
    this.a = new Array(cap);
  }
  push(x) {
    if (this.top >= this.cap - 1) {
      console.log("Stack Overflow");
      return false;
    }
    this.a[++this.top] = x;
    return true;
  }
  pop() {
    if (this.top < 0) {
      console.log("Stack Overflow");
      return 0;
    }
    return this.a[this.top--];
  }

  peek() {
    if (this.top < 0) {
      console.log("Stack is Empty");
      return 0;
    }
    return this.a[this.top];
  }

  isEmpty() {
    return this.top < 0;
  }
}

let s1 = new Stack2(5);
s1.push(10);
s1.push(20);
s1.push(30);
console.log(s1.pop() + " popped from stack");

console.log("Top element is:", s1.peek());

console.log("Elements present in stack:");
while (!s1.isEmpty()) {
  console.log(s1.peek() + " ");
  s1.pop();
}
