from abc import ABC, abstractmethod
from cryptography.fernet import Fernet


class Encryption(ABC):
    def __init__(self, enc_key: str):
        self.enc_key = enc_key.encode() 
    
    @abstractmethod
    def encrypt(text: str) -> str:        
        '''abstract method''' 
        
    @abstractmethod
    def decrypt(cyphered_text: str) -> str:
        '''abstract method''' 


# =============================================================================
# Concrete implementations for different Encryption Methods
# =============================================================================
class Fernet_AES128(Encryption):
    def encrypt(self, text) -> str:
        symmetric_function = Fernet(self.enc_key)
        cyphered_text = symmetric_function.encrypt(text.encode())
        return cyphered_text.decode()
    
    def decrypt(self, cyphered_text) -> str:
        symmetric_function = Fernet(self.enc_key)
        text = symmetric_function.decrypt(cyphered_text.encode())
        return text.decode()
