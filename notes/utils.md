# Input

## One Variable
string
```python
s = input()
```
int
```python
n = int(input())
```

## Two Variables
int
```python
n, m = map(int, input().split())
```

## Any Number of Variables
int
```python
a_list = list(map(int, input().split()))
```

# Print Variables

```python
def print_vars():
    for symbol, value in globals().items():
        if symbol.startswith('__'):
            continue
        if callable(value):
            continue
        print(f'{symbol}: {value}')
```