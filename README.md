# PIPELINE-FUNCTIONS

Class for manipulating a pipeline of functions, creating chains of functions processing the same context.
In this way it is possible that functions can send information between them through the execution chain.

### Example of how it works
    -> Function one receives a parameter, executes and returns data.
    -> Function two receives as a parameter the result of the previous one, executes and returns data.
    ...
    -> Final function takes data from all previous functions and processes.

### Install

```sh
$ pip install pipeline-functions
```

### Example

```python
from pipeline_functions import PipelineFunctions

def hello(parameter: dict = {}):
    print("Calling hello...")
    parameter.update({ "hello": "Hello!" })
    return parameter


def middle(parameter: dict = {}):
    print("Calling middle...")
    raise Exception()
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
        functions=[hello, middle, world, finish],
        debug_mode=True,
        block_mode=False
    )
    pipeline.execute(param = {"universe": "universe!"})
```

