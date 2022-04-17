import os
import json
import pathlib

class ProgramConfig():
    
    APP_PATH = pathlib.Path(__file__).parent.absolute() 
    ACCOUNTS_DB = ''
    DB_FILE = '' 
    EXIT_COMMAND = ''
    VIEW_ALL_ACCOUNTS_COMMAND = ''
    ENC_KEY = ''
    PROMPT = '>'
    SKIP_COMMAND = ''
    SKIP_VALUE = '' 

    @staticmethod
    def start(config_file='program_config.json'):
        with open(os.path.join(ProgramConfig.APP_PATH, config_file), 'r') as fh:
            config = json.load(fh)
            
        ProgramConfig.ENC_KEY = config['ENCRYPTION_KEY'] 
        ProgramConfig.ACCOUNTS_DB = config['ACCOUNTS_DB']
        ProgramConfig.DATA_PATH = os.path.join(ProgramConfig.APP_PATH, config['DATA_FOLDER'])
        ProgramConfig.DB_FILE = os.path.join(ProgramConfig.DATA_PATH, ProgramConfig.ACCOUNTS_DB + '.db')
        ProgramConfig.VIEW_ALL_ACCOUNTS_COMMAND = config['VIEW_ALL_ACCOUNTS_COMMAND']
        ProgramConfig.EXIT_COMMAND = config['EXIT_COMMAND']
        ProgramConfig.PROMPT = config['PROMPT'] 
        ProgramConfig.SKIP_COMMAND = config['SKIP_COMMAND'] 
        ProgramConfig.SKIP_VALUE = config['SKIP_VALUE'] 
        