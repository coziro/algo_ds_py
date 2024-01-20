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
def print_list(symbol, list_):
    print(f'{symbol}:')
    for e in list_:
        print(f'  {e}')

def print_var(symbol, value):
    if isinstance(value, list):
        print_list(symbol, value)
    else:
        print(f'{symbol}: {value}')

def print_vars(var_name=None):
    if isinstance(var_name, str):
        var_name = [var_name]

    for symbol, value in globals().items():
        if var_name:
            for v in var_name:
                if symbol == v:
                    print_var(symbol, value)
        else:
            if symbol.startswith('_'):
                continue
            elif callable(value):
                continue
            else:
                print_var(symbol, value)
```