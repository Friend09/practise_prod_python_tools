import logging

logger = logging.getLogger(__name__)

# the handler determines where the log go: stdout/file
shell_handler = logging.StreamHandler()
file_handler = logging.FileHandler("../../logs/debug.log")

# change the line to see different levels of lines being logged
logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

# the formatter determines what our logs will look like
fmt_shell = '[%(levelname)s %(asctime)s] %(filename)s %(funcName)s %(lineno)s %(message)s'
fmt_file = '%'



logger.debug("This is a DEBUG statement")
logger.info("This is a info statement")
logger.warning("This is a warning statement")
logger.error("This is a error statement")
logger.critical("This is a critical statement")
logger.info("---Logging started---")
