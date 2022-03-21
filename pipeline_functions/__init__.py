"""Package with class that will handle the functions pipeline."""

from .exceptions import PipelineFunctionsNotExistsError, PipelineFunctionsRuntimeError
from .logger import Logger


class PipelineFunctions:
    """Class to handle functions the way you want in a chained way."""

    __logger = Logger()
    __block_mode = False
    __functions: list = []
    __response: dict = {}

    def __init__(self, functions: list = [], debug_mode: bool = True, block_mode: bool = False):
        """Constructor that receives the functions that will be processed in the pipeline."""
        if len(functions) == 0:
            raise PipelineFunctionsNotExistsError()
        self.__response.clear()
        self.__logger = Logger(debug_mode)
        self.__block_mode = block_mode
        self.__functions = functions

    def choice_parameter(self, param: dict = {}) -> dict:
        """Method that checks when the parameter is in the pipeline."""
        if len(param.keys()) != 0 and len(self.__response.keys()) == 0:
            return param
        return self.__response

    def execute(self, param: dict = {}) -> dict:
        """Method that executes all functions in the pipeline, receiving
           parameters and returning information to the next function."""
        for fn in self.__functions:
            try:
                self.__logger.info("Calling function {} with {}.".format(fn.__name__,  param))
                self.__response = fn(self.choice_parameter(param))
            except Exception as error:
                if self.__block_mode is True:
                    raise PipelineFunctionsRuntimeError(str(error))
                self.__logger.warn("Function {} runtime error: {}".format(fn.__name__, error))
        return self.__response
