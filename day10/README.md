# Day 10

I used a **stack** to match pairs. Specifically the algorithm goes like this:

```python
stack = []
for char in line:
    if char is opening bracket:
        push char onto stack
    else:
        top = pop top of stack
        
        if top != opening bracket of char:
            mis-matched brackets
```
