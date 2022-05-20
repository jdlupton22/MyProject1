from abc import ABC, abstractmethod


class ReimbursementDao(ABC):

    @abstractmethod
    def create_reimbursement(self, reimbursement):
        pass

    @abstractmethod
    def read_reimbursement(self, request_id):
        pass

    @abstractmethod
    def all_reimbursements(self):
        pass

    @abstractmethod
    def update_reimbursement(self, change):
        pass

    @abstractmethod
    def delete_reimbursement(self, request_id):
        pass
