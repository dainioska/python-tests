#from link "didzitailizirui
from loguru import logger

logger.add("debug.log", format="{time} {level} {message}",
level="DEBUG",rotation="10 KB",compression="zip")

def dev(a, b):
    return a / b

@logger.catch
def main():
    dev(1, 0)

main()