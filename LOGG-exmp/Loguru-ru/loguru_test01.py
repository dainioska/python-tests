#from link "didzitailizirui"
#pip3 install loguru

from loguru import logger

logger.add("debug.log", format="{time} {level} {message}",
level="DEBUG",rotation="10 KB",compression="zip")

for _ in range(10):
    logger.debug("Hello, (debug)")  

# logger.info("Heloo, (info)")
# logger.error("Hello, (error)")