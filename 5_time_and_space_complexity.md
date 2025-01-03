# Time and Space Complexity

## Time complexity
### A. basic operations 
1. Assignment
2. Comparision
3. Arithmatic operation
4. Calling or returning function

### Examples
1. Example 1
``` Python
   for i in range(n):
       print(i)
```

answer O(n)

2. Example 2
``` Python
n = 500
while n > 0:
    n = n//2
    print(n)
```

answer log(n) with base 2 as it's getting 1/2 in each iteration, in case n = n//3 then log(n) with base 3.

3. Example 3
``` Python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Answer O(n * n),  in word log n square. 


