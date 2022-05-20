from abc import ABC, abstractmethod


class UserbaseDao(ABC):

    @abstractmethod
    def create_userbase(self, userbase):
        pass

    @abstractmethod
    def read_userbase(self, user_id):
        pass

    @abstractmethod
    def all_userbases(self):
        pass

    @abstractmethod
    def update_userbase(self, change):
        pass

    @abstractmethod
    def delete_userbase(self, user_id):
        pass

    @abstractmethod
    def login_userbase(self, username, user_password, user_role):
        pass
