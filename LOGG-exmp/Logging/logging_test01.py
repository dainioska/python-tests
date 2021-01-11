# from link "SF Python"
#
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)

print('Enter the first number: ')
first = input()
logging.debug(type(first))
print('Enter the second number: ')
second = input()
logging.debug(type(second))
print('The sum of ', first, 'and', second, 'is', (first+second))5
7