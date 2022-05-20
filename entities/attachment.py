import data


class Attachment(object):
    def __init__(self, attach_id: int, request_id: int, file_type: str, file: data):
        self.attach_id = int(attach_id)
        self.request_id = int(request_id)
        self.file_type = file_type
        self.file = file

    def __repr__(self):
        return str({
            "attach_id": self.attach_id,
            "request_id": self.request_id,
            "type_of_file": self.file_type,
            "file": self.file
        })

    def json(self):
        return {
            "attachId": self.attach_id,
            "requestId": self.request_id,
            "fileType": self.file_type,
            "file": self.file
        }
