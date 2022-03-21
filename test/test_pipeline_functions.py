import unittest

from pipeline_functions import PipelineFunctions
from pipeline_functions.exceptions import PipelineFunctionsRuntimeError

from test.fixtures import method_error, method_first, method_second, method_third


class TestPipelineFunctions(unittest.TestCase):
    """Test cases for the PipelineFunctions class."""

    def test_build_response_ok(self):
        """Must return an OK response with no errors."""
        pipeline = PipelineFunctions(
            functions=[method_first, method_second, method_third]
        )
        result: dict = pipeline.execute()
        for key_value in ["first", "second", "third"]:
            self.assertEqual(result.get(key_value), key_value)

    def test_build_response_with_initial_param(self):
        """Must return an OK response with initial parameters."""
        pipeline = PipelineFunctions(
            functions=[method_first, method_second, method_third]
        )
        result: dict = pipeline.execute(param={"genesis": "genesis"})
        for key_value in ["genesis", "first", "second", "third"]:
            self.assertEqual(result.get(key_value), key_value)

    def test_build_response_with_method_error(self):
        """Must return a OK response with errors in execution in some method."""
        pipeline = PipelineFunctions(
            debug_mode=False,
            functions=[method_first, method_error, method_third]
        )
        result: dict = pipeline.execute()
        self.assertEqual(len(result), 2)

    def test_block_with_method_error(self):
        """Must return a exception error when executing a method with problem."""
        pipeline = PipelineFunctions(
            block_mode=True,
            functions=[method_first, method_error, method_third]
        )
        self.assertRaises(PipelineFunctionsRuntimeError, pipeline.execute)

