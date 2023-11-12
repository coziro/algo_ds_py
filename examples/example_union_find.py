import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from algo_ds_py import UnionFind  # noqa: E402

uf = UnionFind(3)
uf.union(1, 2)

print(f'root of 0: {uf.find(0)}')
print(f'root of 1: {uf.find(1)}')
print(f'root of 2: {uf.find(2)}')

print(f'roots: {uf.get_roots()}')
print(f'group_count: {uf.get_group_count()}')
print(f'all_group_members: {uf.get_group_members()}')
