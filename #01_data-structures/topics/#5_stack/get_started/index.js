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
    return this.items.length()
  }
}

let s=new Stack()
s.push("John")
s.push("Alisher")
s.push("Umid")

console.log(s.items)