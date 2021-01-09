import logging, time, random

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='logfile.txt', level=logging)

while True:
    logging.debug(random.choice(['hello','hola','hi','ho']))
    time.sleep(1)