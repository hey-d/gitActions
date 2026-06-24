from src.main import div

def test_div_positive():
    assert div(6,2)==3
    
def test_div_negative():
    assert div(6, -2)==-3
    
def div_num_small():
    assert div(2, 6)==0
