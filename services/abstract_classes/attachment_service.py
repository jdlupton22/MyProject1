from abc import ABC, abstractmethod


class AttachmentService(ABC):

    @abstractmethod
    def service_create_attachment(self, attachment):
        pass

    @abstractmethod
    def service_read_attachment(self, attach_id):
        pass

    @abstractmethod
    def service_all_attachments(self):
        pass

    @abstractmethod
    def service_update_attachment(self, change):
        pass

    @abstractmethod
    def service_delete_attachment(self, attach_id):
        pass
