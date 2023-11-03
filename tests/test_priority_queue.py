from algo_ds_py import PriorityQueue

def test_push_pop_min_head():
    pq = PriorityQueue()
    pq.push(10)
    pq.push(30)
    pq.push(20)
    assert pq.pop() == 10
    assert pq.pop() == 20
    assert pq.pop() == 30