# Input

## One Variable
string
```python
S = input()
```
int
```python
N = int(input())
```

## Two Variables
int
```python
N, M = map(int, input().split())
```

## Any Number of Variables
int
```python
A = list(map(int, input().split()))
```

## 2-D List
string
```python
A = [input() for _ in range(H)]
```

# Initialize
1-D list
```python
init_value = 0
a_list = [init_value] * n
```

2-D List
```python
init_value = 0
h = 5
w = 5
a_matrix = [[init_value] * w for _ in range(h)]
```
