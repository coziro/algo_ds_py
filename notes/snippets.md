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

# Initialize
1D list
```python
a_list = [0] * n
```

2D List
```python
a_matrix = [[0] * m for _ in range(n)]
```

# Print Variables

```python
def get_type_name(var):
    return str(type(var)).split("'")[1]

def print_list(symbol, list_):
    print(f'{symbol} ({get_type_name(list_)}):')
    for i, e in enumerate(list_):
        print(f'  {i}: {e}')

def print_var(symbol, value):
    if isinstance(value, list):
        print_list(symbol, value)
    else:
        print(f'{symbol} ({get_type_name(value)}): {value}')

def print_vars(var_name=None):
    if var_name:
        if isinstance(var_name, str):
            var_name = [var_name]
        for symbol in var_name:
            value = globals()[symbol]
            print_var(symbol, value)
    else:
        for symbol, value in globals().items():
            if symbol.startswith('_'):
                continue
            elif callable(value):
                continue
            else:
                print_var(symbol, value)
```