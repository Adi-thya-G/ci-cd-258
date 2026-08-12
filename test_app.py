from app import add_number
def test_add_number():
  assert add_number(2,3)==5

def test_add_negative():
  assert add_number(-1,1)==0

  