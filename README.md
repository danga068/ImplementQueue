# ImplementQueue

1. Implementing Queue using 2 Satcks.
2. Enqueue element does 2 push and 2 pop operations in 2 stacks. One enqueue element does 4 push/pop operation until dequeue.
3. Suppose X element Enqueue and Y element Dequeue then total operations 4X + 4Y.
4. Code will print Number of operation by `print NumberOfOprations()` statement.
5. Code will Execute by command `python zimmber.py`

```
Example
  Opearation: 
    Enqueue(1)
    Enqueue(2)
    Enqueue(3)
    Dequeue()
    Enqueue(4)
    Enqueue(5)
    Dequeue()
    Dequeue()
    Dequeue()
    Dequeue()


Solution: 
  Step 1:
    Enqueue(1), Enqueue(2), Enqueue(3)
    Push element to stack1
    Push operation = 3, Pop operation 0
    stack1 = [1, 2, 3]
    stack2 = []
    Total push operation = 3, Total pop operation 0
  
  Step 2:
    Dequeue()
    Stack2 is empty move element into stack 2
    Push operation = 3, Pop operation 3
    stack1 = []
    stack2 = [3, 2, 1]
    Total push operation = 6, Total pop operation 3
    
    Pop top element 
    Push operation = 0, Pop operation 1
    stack1 = []
    stack2 = [3, 2]
    Total push operation = 6, Total pop operation 4
    
  Step 3:
    Enqueue(4), Enqueue(5)
    push element to stack1
    Push operation = 2, Pop operation 0
    stack1 = [4, 5]
    stack2 = [3, 2]
    Total push operation = 8, Total pop operation 4
    
  Step 4:
    Dequeue(), Dequeue()
    Pop elements from stack2.
    Push operation = 0, Pop operation 2
    stack1 = [4, 5]
    stack2 = []
    Total push operation = 8, Total pop operation 6
    
  Step 5:
    Step 4:
    Dequeue(), Dequeue()
    Stack2 is empty. Move element from stack1 to stack2 
    Push operation = 2, Pop operation 2
    stack1 = []
    stack2 = [5, 4]
    Total push operation = 10, Total pop operation 8
    
    Pop elements from stack2
    Push operation = 0, Pop operation 2
    stack1 = []
    stack2 = []
    Total push operation = 10, Total pop operation 10 ```
    
    
