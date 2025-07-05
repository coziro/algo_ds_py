# Input

## One Line

### One Variable
**string**
```python
# input example: 'hello'
s = input()
```

**int**
```python
# input example: '42'
n = int(input())
```

### Two Variables
**int**
```python
# input example: '3 5'
n, m = map(int, input().split())
```

### Any Number of Variables
**int**
```python
# input example: '1 2 3 4 5'
A = list(map(int, input().split()))
```

## Multiple Lines
**string**
```python
# input example:
# 'abc'
# 'def'
# 'gfi'
S = [input() for _ in range(n)]
```

**int**
```python
# input example:
# '10'
# '20'
# '30
A = [int(input()) for _ in range(n)]
```

**2-D integer matrix**
```python
# input example:
# '1 2 3'
# '4 5 6'
M = [list(map(int, input().split())) for _ in range(h)]
```