from abc import ABC, abstractmethod


class InformationDao(ABC):

    @abstractmethod
    def create_information(self, information):
        pass

    @abstractmethod
    def read_information(self, info_id):
        pass

    @abstractmethod
    def all_informations(self):
        pass

    @abstractmethod
    def update_information(self, change):
        pass

    @abstractmethod
    def delete_information(self, info_id):
        pass
