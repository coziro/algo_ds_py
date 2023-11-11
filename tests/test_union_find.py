from algo_ds_py import UnionFind

"""
def test_union_and_find():
    uf = UnionFind(3)
    uf.union(1, 2)
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 1
"""

def test_union_find():
    uf = UnionFind(3)
    # union
    uf.union(1, 2)
    # find
    assert uf.find(0) != uf.find(1)
    assert uf.find(0) != uf.find(2)
    assert uf.find(1) == uf.find(2)
    # same
    assert uf.same(0, 1) is False
    assert uf.same(0, 2) is False
    assert uf.same(1, 2) is True
    # root
    assert len(uf.roots()) == 2
    assert 1 in uf.roots()

