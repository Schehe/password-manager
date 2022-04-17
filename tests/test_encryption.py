import unittest
from encryption import Fernet_AES128
from program_config import ProgramConfig

class TestEncryption(unittest.TestCase):

    @classmethod
    def setUpClass(cls):        
        print('setupClass')
        ProgramConfig.start()
        cls.encryption = Fernet_AES128(ProgramConfig.ENC_KEY)
        cls.word = 'milk'
        cls.encrypted_possibility = 'gAAAAABiKk74zkLBudr4onU4nPNRl4rZF-iaXTb_RPYUZGdcNHWZbbNNkELf64ksNXg73GPwwt4CCdpHVnOyrJAYYZctRJBtKg=='
        


    def test_encrypt(self):   
        encrypted_word = self.encryption.encrypt(self.word)
        self.assertEqual(self.encryption.decrypt(encrypted_word), self.word)

    def test_decrypt(self):
        self.assertEqual(self.encryption.decrypt(self.encrypted_possibility), self.word)

if __name__ == '__main__':
    unittest.main()

