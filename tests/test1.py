from src.main import sum

def test_sum_positive():
    assert sum(5,6)==11
    
def test_sum_negative():
    assert sum(-5, -6)==-11
    
def test_one_negative():
    assert sum(-5, 6)==1

def test_second_negative():
    assert sum(5, -6)==-1