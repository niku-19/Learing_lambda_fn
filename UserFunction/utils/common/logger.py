import os
import logging
import logging.handlers
from pathlib import Path
import inspect
from colorlog import ColoredFormatter

# Create the logger folder if it doesn't exist
log_folder = Path("/Users/nikhil/Desktop/work/Backend/Learning/Rest API/UserFunction/logger") #FIXME: ABSOLUTE PATH
log_folder.mkdir(exist_ok=True)

# Define a function to get the caller's module name
def get_caller_module_name(): 
    frame = inspect.stack()[2]
    module = inspect.getmodule(frame[0])
    if module:
        module_name = module.__name__.split('.')[-1]
        return module_name
    else:
        return "root"

# Define a function to configure the logger
def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Define a formatter with color and detailed information
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(name)s - %(message)s (%(filename)s:%(lineno)d)%(reset)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    # Define a file handler for each module
    class ModuleFileHandler(logging.FileHandler):
        def __init__(self, module_name):
            log_file = log_folder / f"{module_name}.log"
            super().__init__(log_file)

    # Define a function to get or create a logger for the specific module
    def get_module_logger():
        module_name = get_caller_module_name()
        logger_name = f"{module_name}_logger"

        if logger_name not in logger.manager.loggerDict:
            module_logger = logging.getLogger(logger_name)
            module_logger.setLevel(logging.DEBUG)

            # Add a file handler for this module
            file_handler = ModuleFileHandler(module_name)
            file_handler.setFormatter(formatter)
            module_logger.addHandler(file_handler)

            # Add a stream handler to the root logger for console output
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)
        
        return logging.getLogger(logger_name)

    return get_module_logger

# # Configure the logger at the root level
# get_module_logger = configure_logger()

# # Example usage of the logger
# if __name__ == "__main__":
#     logger = get_module_logger()
#     logger.debug("This is a debug message")
#     logger.info("This is an info message")
#     logger.warning("This is a warning message")
#     logger.error("This is an error message")
#     logger.critical("This is a critical message")
