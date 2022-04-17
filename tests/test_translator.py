import unittest
from program_config import ProgramConfig
from command_line_interface.translator import Translator

class TestTranslator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   
        ProgramConfig.start()
        cls.accounts_db = 'accounts.db'
        cls.menu_list = ['add', 'retrieve', 'delete', 'edit', 'exit', 'e', '5']
        cls.expected_menu_dictionary = {'a': 'add', 'r': 'retrieve', 'd': 'delete', 'e': 'edit', 'x': 'exit', '1': 'e', '5': '5'}
        cls.expected_exit_shortcut = 'x'
        cls.list_accounts = [['15', 'Awezom'], ['40', 'Chi-bay'], ['2', 'Zoom-zoom']]
        cls.expected_account_dictionary = {'1': 'Awezom', '2': 'Chi-bay', '3': 'Zoom-zoom'}
        cls.expected_skip = {'1': 'Awezom', '2': 'Chi-bay', '3': 'Zoom-zoom', '0': 0}


    def test_shortcut_to_command(self):
        self.assertEqual(Translator.shortcut_to_command(self.menu_list), self.expected_menu_dictionary)
        return

    def test_create_number_to_account_name(self):
        self.assertEqual(Translator.create_number_to_account_name(self.list_accounts), self.expected_account_dictionary)
        return

    def setUp(self):
        self.account_dictionary = {'1': 'Awezom', '2': 'Chi-bay', '3': 'Zoom-zoom'}

    def test_add_skip_option_to_dictionary(self):
        self.assertEqual(Translator.add_skip_option_to_dictionary(self.account_dictionary), self.expected_skip)
        return

    def test_get_exit_shortcut(self):
        self.assertEqual(Translator.get_exit_shortcut(self.expected_menu_dictionary), self.expected_exit_shortcut)
        return



if __name__ == '__main__':
    unittest.main()

