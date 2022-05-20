from abc import ABC, abstractmethod


class ReimbursementStatusService(ABC):

    @abstractmethod
    def service_read_reimbursement_status(self, request_id):
        pass

    @abstractmethod
    def service_all_reimbursement_statuses(self):
        pass

    @abstractmethod
    def service_update_reimbursement(self, change):
        pass
