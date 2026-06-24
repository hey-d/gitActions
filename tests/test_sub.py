from src.main import sub

def test_sub_positive():
    assert sub(6,5)==1
    
def test_sub_negative():
    assert sub(5, 6)==-1
    
def test_one_negative():
    assert sub(-5, 6)==-11

def test_second_negative():
    assert sub(5, -6)==11