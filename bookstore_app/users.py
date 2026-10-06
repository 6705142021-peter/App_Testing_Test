"""User accounts: registration and login."""


class Users:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        """Register a new user. Return False if the username is taken."""
        if username in self.users:
            return False

        self.users[username] = password
        return True

    def login(self, username, password):
        """Return True if the username exists and the password matches."""
        stored = self.users.get(username)
        return stored is not None and stored == password