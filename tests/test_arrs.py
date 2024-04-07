from utils import arrs
from utils.arrs import my_slice


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], 0, "test") == 1


def test_get_negative_index():
    assert arrs.get([1, 2, 3], -1) == None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4],0, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], 1, 4) == [2, 3]

def test_my_slice_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], None, -2) == [1, 2, 3]


def test_slice_negative_end():
    assert arrs.my_slice([1, 2, 3], 1, -1) == [2]
def test_slice_zero_coll():
    assert arrs.my_slice([]) == []
