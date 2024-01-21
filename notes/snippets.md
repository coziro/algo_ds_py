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