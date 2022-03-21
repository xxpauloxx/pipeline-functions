"""Package with methods for tests."""

def method_first(parameter: dict = {}):
    parameter.update({ "first": "first" })
    return parameter


def method_second(parameter: dict = {}):
    parameter.update({ "second": "second" })
    return parameter


def method_third(parameter: dict = {}):
    parameter.update({ "third": "third" })
    return parameter


def method_error(parameter: dict = {}):
    raise Exception("Error on calling method_error")
