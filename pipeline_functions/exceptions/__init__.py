"""Package with exception class definitions."""

class PipelineFunctionsNotExistsError(Exception):
    """Exception class for situations where there is no function injected into
       the PipelineFunctions class to process."""

    def __init__(self):
        message = 'No functions to process.'
        super().__init__(message)


class PipelineFunctionsRuntimeError(Exception):
    """Class exception when an error occurs in the function pipeline runtime."""

    def __init__(self, message: str = ""):
        super().__init__(message)

