from abc import ABC, abstractmethod


class AttachmentDao(ABC):

    @abstractmethod
    def create_attachment(self, attachment):
        pass

    @abstractmethod
    def read_attachment(self, attach_id):
        pass

    @abstractmethod
    def all_attachments(self):
        pass

    @abstractmethod
    def update_attachment(self, change):
        pass

    @abstractmethod
    def delete_attachment(self, attach_id):
        pass
