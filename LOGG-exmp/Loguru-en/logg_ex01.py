from loguru import logger
import sys

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level='INFO')

logger.add("file_{time}.log")

logger.add("file_1.log", rotation="500 MB") #Automatically rotate two big file
logger.add("file_2.log", rotation="12:00") #New file is created each day at noon
logger.add("file_3.log", rotation="1 week") #Once file is too old, it's rotated

logger.add("file_X.log", retention="10 days") #Clear after some time
logger.add("file_Y.log", compression="zip") #Save some space