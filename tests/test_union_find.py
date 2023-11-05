from algo_ds_py import UnionFind


def test_union_and_find():
    uf = UnionFind(3)
    uf.union(1, 2)
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 1
