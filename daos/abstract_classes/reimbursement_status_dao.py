from abc import ABC, abstractmethod


class ReimbursementStatusDao(ABC):

    @abstractmethod
    def read_reimbursement_status(self, request_id):
        pass

    @abstractmethod
    def all_reimbursement_statuses(self):
        pass

    @abstractmethod
    def update_reimbursement_status(self, change):
        pass
