import logging

logger = logging.getLogger("src")
logger.setLevel(logging.DEBUG)

format_string = "%(asctime)s %(levelname)-8s --- %(message)s --- %(name)s:%(lineno)d"
formatter = logging.Formatter(format_string, datefmt="%Y-%m-%d %H:%M:%S")

handler = logging.FileHandler(filename="../logs/log.log",mode="w")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.warning(f"Message!")
