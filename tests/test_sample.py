# content of test_math.py
import math

def test_sqrt():
    assert math.sqrt(4) == 2.0
    assert math.sqrt(25) == 5.0
    assert math.sqrt(9) == 3.0
    
def test_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(4, 2) == 16
    assert math.pow(3, 4) == 81

