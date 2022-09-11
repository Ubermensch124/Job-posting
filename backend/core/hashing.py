from passlib.context import CryptContext

pwd_context = CryptContext(schemes='bcrypt', deprecated='auto')

class    Hasher:
    @staticmethod
    def check_pass_hash(password: str, hash_password) -> bool:
        return pwd_context.verify(secret=password, hash=hash_password)

    @staticmethod
    def get_hash_from_pass(password: str) -> str:
        return pwd_context.hash(secret=password)

# print(Hasher.get_hash_from_pass(password='123456789'))
# print(Hasher.check_pass_hash(password='123456789', hash_password='$2b$12$82mmNJucMfEkSWwsXMe62e3JDWNecwvd7USOKC7SQduCMcHAdDPja'))