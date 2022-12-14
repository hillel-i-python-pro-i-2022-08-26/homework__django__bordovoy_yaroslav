from typing import NamedTuple


class GeneratedUserInfo(NamedTuple):
    username: str
    email: str
    password: str

    def __str__(self):
        return (
            f"Username: {self.username}, email: {self.email}, password: {self.password}"
        )
