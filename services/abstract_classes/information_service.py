from abc import ABC, abstractmethod


class InformationService(ABC):
    @abstractmethod
    def service_create_information(self, information):
        pass

    @abstractmethod
    def service_read_information(self, info_id):
        pass

    @abstractmethod
    def service_all_informations(self):
        pass

    @abstractmethod
    def service_update_information(self, change):
        pass

    @abstractmethod
    def service_delete_information(self, info_id):
        pass
