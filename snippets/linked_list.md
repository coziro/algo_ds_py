# Node Class

```python
class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
```

# Logger

```python
def pprint(node: ListNode, max_nodes: int = 10):
    pointer = node
    values = []
    counter = 0
    while pointer and counter < max_nodes:
        values.append(pointer.val)
        pointer = pointer.next
        counter += 1
    print(values)
```