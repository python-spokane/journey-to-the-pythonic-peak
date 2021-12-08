from typing import Union
from attr import dataclass


@dataclass
class User():
    name: str
    language: str = "Python"


# Pythonic
class UserService:
    def __init__(self, users: list[User]) -> None:
        self.users_by_name = {
            user.name: user
            for user
            in users
        }

    def get_user(self, name: str) -> User:
        return self.users_by_name[name]

users = [
    User("Joseph Riddle"),
    User("Meghan Woodford", "PowerShell"),
]
user_service = UserService(users)
joseph = user_service.get_user("Joseph Riddle")
print(joseph.language)
meghan = user_service.get_user("Meghan Woodford")
print(meghan.language)


# Less Pythonic
class UserService:
    def __init__(self, users: list[User]) -> None:
        self.users_by_name = {
            user.name: user
            for user
            in users
        }

    def get_user(self, name: str) -> Union[User, None]:
        return self.users_by_name.get(name, None)

users = [
    User("Joseph Riddle"),
    User("Meghan Woodford", "PowerShell"),
]
user_service = UserService(users)
joseph = user_service.get_user("Joseph Riddle")
print(joseph.language) # <-- Uh-oh 😦
meghan = user_service.get_user("Meghan Woodford")
print(meghan.language)
