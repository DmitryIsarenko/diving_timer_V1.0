import logging

logger = logging.getLogger("src")
logger.setLevel(logging.DEBUG)

format_string = "%(levelname)-8s %(name)s %(lineno)3d %(asctime)s  %(message)s"
formatter = logging.Formatter(format_string)

handler = logging.FileHandler(filename="./logs/master.log",mode="w")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.warning(f"Message 1")
