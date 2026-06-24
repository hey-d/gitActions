from src.main import mul

def test_mul_positive():
    assert mul(5,6)==30
    
def test_sum_negative():
    assert mul(-5, -6)==30
    
def test_one_negative():
    assert mul(-5, 6)==-30

def test_second_negative():
    assert mul(5, -6)==-30