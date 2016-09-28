import logging

def Logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    fh = logging.FileHandler('output/test.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    formatter = logging.Formatter('*'*100)
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
