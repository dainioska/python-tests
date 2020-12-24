import math_func

def test_add():
   assert math_func.add(7, 3) == 10
   assert math_func.add(7) == 9

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10

def test_add_strings():
   result = math_func.add('Hello', ' labas')
   assert result == 'Hello labas'
   assert type(result) is str
   assert 'Heldlo' not in result

def test_product_strings():
   assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
   result = math_func.product('Hello ')
   assert result == 'Hello Hello '
   assert type(result) is str
   assert 'Hello' in result