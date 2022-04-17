import unittest
from program_config import ProgramConfig
from command_line_interface.translator import Translator
from factory import Factory


class TestFactory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   
        cls.factory = Factory(command=MockCommand)
        cls.expected_builders = {'Add': MockCommand.__subclasses__()[0], 'Retrieve': MockCommand.__subclasses__()[1],
            'Edit': MockCommand.__subclasses__()[2], 'Exit': MockCommand.__subclasses__()[3]}

    def test_create(self):
        self.assertEqual(type(self.factory.create('Add')), type(Add()))
        with self.assertRaises(ValueError):
            self.factory.create('Wrong')

    def test_builders(self):
        self.assertEqual(self.factory.builders, self.expected_builders) 


class MockCommand():

    def __init__(self):
        self.created_class_name = str(self.__class__.__name__).lower()

    def execute(self):
        pass


class Add(MockCommand):

    def execute(self):
        return True


class Retrieve(MockCommand):

    def execute(self):
        return True

class Edit(MockCommand):

    def execute(self):
        return True


class Exit(MockCommand):

    def execute(self):
        return True


if __name__ == '__main__':
    unittest.main()

