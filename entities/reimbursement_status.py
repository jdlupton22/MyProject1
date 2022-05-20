import datetime
from enums.app_stage import AppStage
from enums.app_status import AppStatus


class ReimbursementStatus:
    def __init__(self, request_id: int, projected_award: float, urgent: bool, status: AppStatus, stage: AppStage,
                 request_date_time: datetime):
        self.request_id = int(request_id)
        self.projected_award = float(projected_award)
        self.urgent = bool(urgent)
        self.status = AppStatus(status)
        self.stage = AppStage(stage)
        self.request_date_time = request_date_time

    def __repr__(self):
        return str({
            "request_id": self.request_id,
            "projected_award": self.projected_award,
            "urgent": self.urgent,
            "status": self.status,
            "stage": self.stage,
            "request_date_time": self.request_date_time

        })

    def json(self):
        return {
            "requestId": self.request_id,
            "projectedAward": self.projected_award,
            "urgent": self.urgent,
            "status": self.status,
            "stage": self.stage,
            "requestDateTime": self.request_date_time

        }
