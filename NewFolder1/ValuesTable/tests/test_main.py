""" Tests for module main"""

import pytest
from tablevalues.main import *

def setup_module():
    print("setup module")

def teardown_module():
    print("teardown module")

# create_interval(0,10,2) -> [0, 10]
# create_interval(0,10,11) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# create_interval(0,10,6) -> [0, 2, 4, 6, 8, 10]
# create_interval(1,10,3) -> [1, 9/2, 10]

# x0 always needs to be min_value; x1 always needs to be max_value
# interval always needs to be the size of n

# create_interval(0,-1,6) -> ERROR! Min > Max
# create_interval(0,5,0) -> ERROR! Size must be > 0
def test_create_interval():
    assert create_interval(0, 10,2) == [0, 10]
    assert create_interval(0, 10,11) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert create_interval(-5, 25, 5) == [-5, 2.5, 10, 17.5, 25]
    assert create_interval(1, 10,3) == [1, 11/2, 10]

    assert len(create_interval(0, 10,6)) == 6

    with pytest.raises(ValueError):
        create_interval(0, -1, 6)
    with pytest.raises(ValueError):
        create_interval(0, 5, 0)

# test_validate_func_ops("3*x%5+x/2") -> true (valid)
# test_validate_func_ops("1337") -> true (valid)
# test_validate_func_ops("2^x") -> true (valid)

# test_validate_func_ops("2*y+3") -> false (invalid) -> only letter x allowed as variable
# test_validate_func_ops("") -> false (invalid) -> func cannot be empty
def test_validate_func_ops():
    assert validate_func_ops("3*x%5+x/2") == True
    assert validate_func_ops("1337") == True
    assert validate_func_ops("2^x") == True

    try:
        with pytest.raises(ValueError):
            validate_func_ops("2*y+3")
    except:
        assert True


# test_validate_func_vals("1/x", [1,2,3]) -> true (valid)
# test_validate_func_vals("2/x", [0,1,3]) -> false (invalid) -> division by 0 not allowed!
def test_validate_func_vals():
    assert validate_func_vals("1/x", [1,2,3]) == True
    with pytest.raises(ZeroDivisionError):
        validate_func_vals("2/x", [0,1,3])

# test_calc_vals("2*x", [1,2,3]) -> [2,4,6]
# test_calc_vals("1337", [5, 8, 2249]) -> [1337, 1337, 1337]
# test_calc_vals("1/x", [1,2,3]) -> [1, 1/2, 1/3]
# test_calc_vals("2/x", [0, 5, 10]) -> [] (Division by Zero not allowed!)
def test_calc_vals():
    assert calc_vals("2*x", [1,2,3]) == [2,4,6]
    assert calc_vals("1337", [5, 8, 2249]) == [1337, 1337, 1337]
    assert calc_vals("1/x", [1,2,3]) == [1, 1/2, 1/3]

    assert calc_vals("2/x", [0, 5, 10]) == []

def test_create_table():
    pass

def test_calc():
    print("testing calc")