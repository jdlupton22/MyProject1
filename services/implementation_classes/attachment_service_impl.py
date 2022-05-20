from daos.abstract_classes.attachment_dao import AttachmentDao
from services.abstract_classes.attachment_service import AttachmentService


class AttachmentServiceImpl(AttachmentService):

    def __init__(self, attachment_dao: AttachmentDao):
        self.attachment_dao = attachment_dao

    def service_create_attachment(self, attachment):
        return self.attachment_dao.create_attachment(attachment)

    def service_read_attachment(self, attach_id):
        return self.attachment_dao.read_attachment(attach_id)

    def service_all_attachments(self):
        return self.attachment_dao.all_attachments()

    def service_update_attachment(self, change):
        return self.attachment_dao.update_attachment(change)

    def service_delete_attachment(self, attach_id):
        return self.attachment_dao.delete_attachment(attach_id)
