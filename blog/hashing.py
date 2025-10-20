from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    @staticmethod
    def bcrypt(password: str):
        return pwd_context.hash(password)
    
    @staticmethod
    def verify(hashed_pass, enterred_pass):
        return pwd_context.verify(enterred_pass, hashed_pass)