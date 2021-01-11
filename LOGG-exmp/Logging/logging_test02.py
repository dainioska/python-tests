# from link "SF Python" 
#
import logging, time, random
logging.basicConfig(level='DEBUG',filename='testlog.log')

while True:
    logging.debug(random.choice(['hello','hola','hi','ho']))
    time.sleep(1)