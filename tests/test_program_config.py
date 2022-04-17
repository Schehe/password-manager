import unittest
from program_config import ProgramConfig
import pathlib


class TestProgramConfig(unittest.TestCase):

    @classmethod
    def setUp(self):   
        self.datapath = pathlib.Path(__file__).parent.parent.absolute() 
        self.key = 'an_encryption_key='
        self.account = 'mockaccounts'
        self.data = 'C:\Portable\python\pyproj\pwm' + '\\'
        self.db = 'mockaccounts.db'
        self.exit = 'Exit'
        self.view = 'View'
        self.skip_command = '0'
        self.skip_value = 0
        self.mock_json_file = './tests/mock_program_config.json' 
        ProgramConfig.start(self.mock_json_file)        


    def test_start(self):        
        self.assertEqual(ProgramConfig.ENC_KEY, self.key)
        self.assertEqual(ProgramConfig.ACCOUNTS_DB, self.account)
        self.assertEqual(ProgramConfig.DATA_PATH, self.data)
        self.assertEqual(ProgramConfig.DB_FILE, str(self.data) + self.db)
        self.assertEqual(ProgramConfig.DB_FILE, str(self.datapath) + '\\' + self.db)
        self.assertEqual(ProgramConfig.EXIT_COMMAND, self.exit)
        self.assertEqual(ProgramConfig.VIEW_ALL_ACCOUNTS_COMMAND, self.view)
        self.assertEqual(ProgramConfig.SKIP_COMMAND, self.skip_command)
        self.assertEqual(ProgramConfig.SKIP_VALUE, self.skip_value)



if __name__ == '__main__':
    unittest.main()


        
