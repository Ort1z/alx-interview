# 0x00. Pascal's Triangle

## Algorithm | Python

- **Weight:** 1
- **Project start:** Sep 30, 2024 6:00 AM
- **Project end:** Oct 4, 2024 6:00 AM
- **Checker release:** Oct 1, 2024 6:00 AM
- **Auto review:** Will be launched at the deadline

## Resources

- [What is Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Pascal's Triangle - Numberphile](https://www.youtube.com/watch?v=0iMtlus-afo)
- [What are Python Algorithms](https://www.programiz.com/python-programming/algorithm)

### Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=1qw5ITr3k9E)

## Must Know

To successfully complete this project, you should revise the following Python concepts:

1. **Lists and List Comprehensions**
2. **Functions**
3. **Loops**
4. **Conditional Statements**
5. **Recursion (Optional)**
6. **Arithmetic Operations**
7. **Indexing and Slicing**
8. **Memory Management**
9. **Error and Exception Handling (Optional)**
10. **Efficiency and Optimization**

## Tasks

### 0. Pascal's Triangle
**Mandatory**

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))


