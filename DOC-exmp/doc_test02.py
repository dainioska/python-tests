'''
Sample test cases with doctest
python -m doctest -v doc_test02.py
'''

def mul(a, b):
    '''
    >>> mul(3, 4)
    12
    >>> mul('b',  6)
    'bbbbbb'
    '''
    return a * b

def add(a, b):
    '''
    >>> add(3, 4)
    7
    >>> add('b', 'c')
    'bc'
    '''
    return a + b