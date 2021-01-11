from loguru import logger

#logger.info("If python {}, prefer {feature} of course", 3.6, feature="f-strings")

@logger.catch
def fcn(x, y, z):
    return 1/ (x + y + z)

fcn(1,2,-3)
