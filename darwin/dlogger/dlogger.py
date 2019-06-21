
import logging

# get the logger based on this file's name
dlogger = logging.getLogger(__name__)

# create handlers
cmd_handler = logging.StreamHandler()
file_handler = logging.FileHandler('darwin.log')
cmd_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# create formatters
cmd_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fileformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
cmd_handler.setFormatter(cmd_format)
file_handler.setFormatter(file_format)

# add handlers to logger
dlogger.addHandler(cmd_handler)
dlogger.addHandler(file_handler)


