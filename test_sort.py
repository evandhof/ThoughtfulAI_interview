import pytest
from sort import sort 

def test_standard():
    width = 149.999 
    height = 10
    length = 1
    mass = 19.999

    result = sort(width, height, length, mass)

    assert(result == "STANDARD")

def test_bulky_dimension():
    bulky_dim = 150 
    not_bulky_dim = 1
    mass = 19.999

    assert(sort(bulky_dim, not_bulky_dim, not_bulky_dim, mass) == "SPECIAL")
    assert(sort(not_bulky_dim, bulky_dim, not_bulky_dim, mass) == "SPECIAL")
    assert(sort(not_bulky_dim, not_bulky_dim, bulky_dim, mass) == "SPECIAL")

def test_bulky_volume():
    dim = 100 
    mass = 10

    assert(sort(dim, dim, dim, mass) == "SPECIAL")

def test_heavy():
    dim = 1
    mass = 20

    assert(sort(dim, dim, dim, mass) == "SPECIAL")

def test_bulky_and_heavy():
    dim = 100
    mass = 20 

    assert(sort(dim, dim, dim, mass) == "REJECTED")

def test_exceptions():
    bad_dim = -1 
    bad_mass = -1 
    dim = 1
    mass = 1

    with pytest.raises(Exception):
        sort(bad_dim, dim, dim, mass)
    
    with pytest.raises(Exception):
        sort(dim, dim, dim, bad_mass)