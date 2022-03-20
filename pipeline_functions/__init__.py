from .exceptions import PipelineFunctionsNotExists


class PipelineFunctions:
    """Class to handle functions the way you want in a chained way."""

    array_functions: list = []
    last_parameter: dict = {}

    def __init__(self, array_functions: list = []):
        if len(array_functions) == 0:
            raise PipelineFunctionsNotExists()
        self.array_functions = array_functions

    def choice_parameter(self, parameter: dict = {}):
        if len(parameter.keys()) != 0 and len(self.last_parameter.keys()) == 0:
            return parameter
        return self.last_parameter

    def execute(self, parameter: dict = {}) -> None:
        for current_function in self.array_functions:
            self.last_parameter = current_function(self.choice_parameter(parameter))

