# from link "molchanov"
import logging
import requests
logging.basicConfig(level='DEBUG')
#logging.basicConfig(level='DEBUG',filename='mylog.log')
logging.getLogger('urlib3').setLevel('CRITICAL')

logger =logging.getLogger()
print(logger)
print()
#logger.setLevel('DEBUG') #logging.DEBUG
print(logger.level)
print()
print(logger.handlers)

# for key in logging.Logger.manager.loggerDict:
#     print(key)

def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')
    r = requests.get('https://www.google.com')


if __name__ == "__main__":
    main("alio")
