import logging.handlers

format_string_logfile = "%(asctime)s %(levelname)-8s --- %(message)s --- %(name)s:%(lineno)s"
format_string_console = "%(levelname)s --- %(message)-100s --- %(name)s:%(lineno)s"
date_format = "%Y-%m-%d %H:%M:%S"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename="../logs/log.log",
                                   mode="w")
rotating_handler = logging.handlers.RotatingFileHandler(filename="../logs/rotating_log.log",
                                                        maxBytes=10 ** 6,
                                                        backupCount=2)

formatter_logfile = logging.Formatter(fmt=format_string_logfile, datefmt=date_format)
formatter_console = logging.Formatter(fmt=format_string_console, datefmt=None)

console_handler.setFormatter(formatter_console)
file_handler.setFormatter(formatter_logfile)
rotating_handler.setFormatter(formatter_logfile)

console_handler.setLevel(level=logging.DEBUG)
file_handler.setLevel(level=logging.DEBUG)
rotating_handler.setLevel(level=logging.WARNING)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(rotating_handler)

logger.info(f"Logger <<{__name__}>> started.")
