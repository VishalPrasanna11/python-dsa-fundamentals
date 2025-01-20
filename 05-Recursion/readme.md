# Recursion

## What is Recursion?

Recursion is a programming technique where a function calls itself to solve a smaller instance of a larger problem. It breaks a problem into smaller sub-problems, solving each one until the simplest form of the problem, known as the base case, is reached. 

### Key Features of Recursion:
- **Self-referential**: A recursive function calls itself.
- **Base Condition**: Ensures the recursion stops by defining the simplest case to solve directly.
- **Recursive Call**: Reduces the problem in size or complexity with each function call.

### Example:
```python
def factorial(n):
    if n == 0:  # Base condition
        return 1
    return n * factorial(n - 1)  # Recursive call
```

---

## When to Use Recursion?

Recursion is ideal when:
1. **Problem Can Be Divided**: Problems can be broken into smaller, similar sub-problems, e.g., tree traversal, divide-and-conquer algorithms like merge sort.
2. **Data Structures with Hierarchical Nature**: When working with trees, graphs, or nested structures.
3. **Mathematical Problems**: Such as calculating factorials, Fibonacci sequences, or solving Tower of Hanoi.
4. **Elegant Solutions**: When recursion provides a more intuitive or shorter solution than iteration.

### When NOT to Use Recursion:
- **Performance Sensitive Applications**: Recursion can lead to higher memory usage due to stack calls.
- **Large Input Sizes**: Recursive depth can cause stack overflow errors for extensive problems.
- **Iterative Alternatives Exist**: When iteration is more straightforward or efficient.

---

## Recursion vs. Iteration

| Aspect              | Recursion                          | Iteration                              |
|---------------------|------------------------------------|---------------------------------------|
| **Definition**      | Function calling itself            | Repeatedly executing a set of statements |
| **State**           | Uses call stack to maintain state  | Uses loop variables for state         |
| **Performance**     | Higher memory usage (call stack)   | Lower memory usage                    |
| **Readability**     | Concise and intuitive for some problems | Explicit and straightforward          |
| **Use Cases**       | Tree traversal, Divide-and-Conquer | Simple loops, counting, traversals    |

---

## Ways to Write a Base Condition

The base condition is the termination point of a recursive function. It ensures that the function does not enter an infinite loop. Here are common strategies:

1. **Handle Simplest Case First**:
   Define the smallest problem that can be solved directly.
   ```python
   def factorial(n):
       if n == 0:  # Base case
           return 1
       return n * factorial(n - 1)
   ```

2. **Empty Input**:
   Check for null, empty, or undefined inputs.
   ```python
   def reverse_string(s):
       if len(s) == 0:  # Base case
           return ""
       return s[-1] + reverse_string(s[:-1])
   ```

3. **Boundary Conditions**:
   Use conditions that restrict recursion to valid ranges.
   ```python
   def fibonacci(n):
       if n <= 1:  # Base cases
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)
   ```

4. **Error Handling**:
   Prevent recursion for invalid inputs.
   ```python
   def search(arr, index):
       if index < 0 or index >= len(arr):  # Base case
           return None
       return arr[index]
   ```

---

## Recursion Leap of Faith

The "Leap of Faith" is the approach of trusting that the recursive function works correctly for smaller sub-problems without needing to mentally trace every recursive call. Focus on:
1. Solving the current step based on the assumption that the recursive step solves the smaller problem.
2. Writing a proper base case to guarantee termination.

### Example:
```python
def sum_of_array(arr):
    if len(arr) == 0:  # Base case
        return 0
    # Trust that sum_of_array(arr[1:]) correctly computes the sum of the rest of the array
    return arr[0] + sum_of_array(arr[1:])
```

---

## Recursion Relation

The recursion relation is the mathematical relationship that expresses how a larger problem can be solved using smaller sub-problems. This forms the core logic of the recursive function.

### Steps to Formulate Recursion Relation:
1. Identify the larger problem and its sub-problems.
2. Derive how the solution to the larger problem depends on the solutions to the sub-problems.
3. Define the base case.

### Example:
**Factorial Relation**:
Factorial of `n` is `n * factorial(n-1)`.
```math
factorial(n) = n * factorial(n - 1)
Base case: factorial(0) = 1
```

**Fibonacci Relation**:
The nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers.
```math
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
Base case: fibonacci(0) = 0, fibonacci(1) = 1