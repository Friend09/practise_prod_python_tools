import logging
from rich.logging import RichHandler

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
shell_handler = RichHandler()
file_handler = logging.FileHandler("/Users/vamsi_mbmax/Library/CloudStorage/OneDrive-Personal/01_vam_PROJECTS/LEARNING/proj_Productivity/dev_proj_Productivity/practise_prod_python_tools/logs/debug.log")

# set the logging level
logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# define the log format
fmt_shell = '%(message)s'
fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'

# initiate the formatter
shell_formatter = logging.Formatter(fmt_shell)
file_formatter = logging.Formatter(fmt_file)

# use the formatter w/ logger
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

# start logging
logger.addHandler(shell_handler)
logger.addHandler(file_handler)
