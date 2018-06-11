import uuid
from back.common.db import Db
from back.common.utils import Utils


class User:
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def find_email(cls, email):
        return cls(**Db.find_one('users', {'email': email}))

    def save(self):
        self.__dict__['password'] = Utils.hash_password(self.password)
        Db.insert("users", self.__dict__)

    def __str__(self):
        return f"{self.email}"
