from pipeline_functions import PipelineFunctions

def hello(parameter: dict = {}):
    parameter.update({ "hello": "Hello!" })
    return parameter


def world(parameter: dict = {}):
    parameter.update({ "world": "World!" })
    return parameter

def finish(parameter: dict = {}):
    print(parameter)
    return parameter


if __name__ == "__main__":
    pipeline = PipelineFunctions([hello, world, finish])
    pipeline.execute()
