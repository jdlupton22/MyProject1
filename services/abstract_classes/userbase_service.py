from abc import ABC, abstractmethod


class UserbaseService(ABC):

    @abstractmethod
    def service_validate_userbase(self, username, user_password, user_role):
        pass

    @abstractmethod
    def service_create_userbase(self, userbase):
        pass

    @abstractmethod
    def service_read_userbase(self, user_id):
        pass

    @abstractmethod
    def service_all_userbases(self):
        pass

    @abstractmethod
    def service_update_userbase(self, change):
        pass

    @abstractmethod
    def service_delete_userbase(self, user_id):
        pass
