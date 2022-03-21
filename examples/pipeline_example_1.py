from pipeline_functions import PipelineFunctions

def hello(parameter: dict = {}):
    print("Calling hello...")
    parameter.update({ "hello": "Hello!" })
    return parameter


def middle(parameter: dict = {}):
    print("Calling middle...")
    return parameter


def world(parameter: dict = {}):
    print("Calling world...")
    parameter.update({ "world": "World!" })
    return parameter


def finish(parameter: dict = {}):
    print("Calling finish...")
    print(parameter)
    return parameter


if __name__ == "__main__":
    pipeline = PipelineFunctions(
        functions=[hello, middle, world, finish]
    )
    pipeline.execute()
