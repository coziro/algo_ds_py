from algo_ds_py import UnionFind


def test_union_find():
    uf = UnionFind(3)
    # union
    uf.union(1, 2)
    # find
    assert uf.find(0) != uf.find(1)
    assert uf.find(0) != uf.find(2)
    assert uf.find(1) == uf.find(2)
    # same
    assert uf.is_connected(0, 1) is False
    assert uf.is_connected(0, 2) is False
    assert uf.is_connected(1, 2) is True
    # root
    assert len(uf.get_roots()) == 2
    assert 1 in uf.get_roots()
    # group counts
    assert uf.get_group_count() == 2
    # all group members
    assert len(uf.get_group_members()) == 2

