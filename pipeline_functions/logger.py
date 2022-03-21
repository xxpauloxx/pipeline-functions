import logging

class Logger:
    """Class that will handle the logs based on the debug mode setting."""

    __logger = logging.getLogger(__name__)
    __debug_mode = False

    def __init__(self, debug_mode: bool = False):
        self.__debug_mode = debug_mode

    def info(self, message: str = "") -> None:
        """Method to log info pipeline information if in debug mode."""
        if self.__debug_mode is True:
            self.__logger.info(message)

    def warn(self, message: str = "") -> None:
        """Method to log warn pipeline information if in debug mode."""
        if self.__debug_mode is True:
            self.__logger.warn(message)

    def error(self, message: str = "") -> None:
        """Method to log error pipeline information if in debug mode."""
        if self.__debug_mode is True:
            self.__logger.error(message)
