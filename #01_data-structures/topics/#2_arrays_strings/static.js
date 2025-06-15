arr = [30, -20, 70, 0, 60]; // n/2 -> 0.5n -> n

// access - read
console.log(arr[2]); // 30 -> O(1)
// search - find -> O(n): worst-case. 30: O(1) -> best-case
// Insertion:
// insert_at_the_beginning(specific index): O(n) insert_at_the_end: O(1)
// Deletion: 
// delete_at_the_beginning(speific index): O(n), delete_at_the_end: O(1)

// Space Complexity: 
// access - read -> O(1) -> search
// insertion - deletion -> O(n) 