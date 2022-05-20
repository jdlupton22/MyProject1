from daos.abstract_classes.attachment_dao import AttachmentDao
from entities.attachment import Attachment
from exceptions.no_attachments_found import NoAttachmentsFound
from exceptions.resource_not_found import ResourceNotFound
from util.database_connection import connection


def _build_attachment(profile):
    if profile:
        return Attachment(attach_id=profile[0], request_id=profile[1], file_type=profile[2], file=profile[3])
    else:
        return None


class AttachmentDaoImpl(AttachmentDao):
    def create_attachment(self, attachment):
        sql = "INSERT INTO attachments VALUES (DEFAULT, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [attachment.request_id, attachment.file_type, attachment.file])

        connection.commit()
        profile = cursor.fetchone()

        return _build_attachment(profile)

    def read_attachment(self, attach_id):
        sql = "SELECT * FROM attachments WHERE attach_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [attach_id])

        profile = cursor.fetchone()

        if profile:
            return _build_attachment(profile)
        else:
            raise ResourceNotFound(f"No attachment with id: {attach_id} - has been located!")

    def all_attachments(self):
        sql = "SELECT * FROM attachments"

        cursor = connection.cursor()
        cursor.execute(sql)

        profiles = cursor.fetchall()

        attachment_list = [_build_attachment(profile) for profile in profiles]
        if profiles:
            return attachment_list
        else:
            raise NoAttachmentsFound(f"No attachments found!")

    def update_attachment(self, change):
        sql = "UPDATE attachments SET request_id = %s, file_type = %s, file = %s WHERE" \
              "attach_id = %s  RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [change.request_id, change.file_type, change.file, change.attach_id])

        connection.commit()
        profile = cursor.fetchone()

        return _build_attachment(profile)

    def delete_attachment(self, attach_id):
        sql = "DELETE FROM attachments WHERE attach_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [attach_id])
        connection.commit()


def _test():
    ad = AttachmentDaoImpl()
    attach = ad.read_attachment(1)
    print(attach)
    print("------------------")
    print(ad.all_attachments())


if __name__ == '__main__':
    _test()
