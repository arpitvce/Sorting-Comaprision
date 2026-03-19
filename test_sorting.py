from mergesort import sort
from bubble import bubblesort

def test_basic():
    arr=[3,2,1]
    assert bubblesort(arr())==[1,2,3]
    assert sort(arr.copy())==[1,2,3]

