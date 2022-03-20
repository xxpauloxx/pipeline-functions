class PipelineFunctionsNotExists(Exception):
    """Exception class for situations where there is no function injected into
       the PipelineFunctions class to process."""

    def __init__(self):
        message = 'No functions to process.'
        super().__init__(message)

