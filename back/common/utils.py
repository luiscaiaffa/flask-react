from cryptography.fernet import Fernet


class Utils:

    @staticmethod
    def hash_password(password: str):
        f = Fernet(b'APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=')
        return f.encrypt(password.encode())

    @staticmethod
    def check_password(password, hashed_password):
        f = Fernet(b'APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=')
        return password.encode() == f.decrypt(hashed_password)
