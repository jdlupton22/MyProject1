import datetime


class Information:
    def __init__(self, info_id: int, related_id: int, destination_id: int, sender_id: int, sender: str,
                 urgent: bool, description: str, request_date_time: datetime):
        self.info_id = int(info_id)
        self.related_id = int(related_id)
        self.destination_id = int(destination_id)
        self.sender_id = int(sender_id)
        self.sender = sender
        self.urgent = bool(urgent)
        self.description = description
        self.request_date_time = request_date_time

    def __repr__(self):
        return str({
            "info_id": self.info_id,
            "related_id": self.related_id,
            "destination_id": self.destination_id,
            "sender_id": self.sender_id,
            "sender": self.sender,
            "urgent": self.urgent,
            "description": self.description,
            "request_date_time": self.request_date_time

        })

    def json(self):
        return {
            "infoId": self.info_id,
            "relatedId": self.related_id,
            "destinationId": self.destination_id,
            "senderId": self.sender_id,
            "sender": self.sender,
            "urgent": self.urgent,
            "description": self.description,
            "requestDateTime": self.request_date_time
        }
