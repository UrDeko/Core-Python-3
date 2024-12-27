import unittest
from unittest.mock import MagicMock
import sample_functions

class TestSampleFunctions(unittest.TestCase):

    def test_create_object(self):
        self.assertEqual(sample_functions.create_object("John", 15), {"name": "John", "age": 15})

    def test_use_object(self):
        sample_functions.create_object = MagicMock(return_value={"name": "John", "age": 16})
        p = sample_functions.create_object()
        sample_functions.object_info = MagicMock()
        sample_functions.use_object(p['name'], p['age'])
        sample_functions.create_object.assert_called_with(p['name'], p['age'])
        sample_functions.object_info.assert_called_once_with(p)

if __name__ == "__main__":
    unittest.main()