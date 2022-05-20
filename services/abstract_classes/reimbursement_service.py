from abc import ABC, abstractmethod


class ReimbursementService(ABC):

    @abstractmethod
    def service_create_reimbursement(self, reimbursement):
        pass

    @abstractmethod
    def service_read_reimbursement(self, request_id):
        pass

    @abstractmethod
    def service_all_reimbursements(self):
        pass

    @abstractmethod
    def service_update_reimbursement(self, change):
        pass

    @abstractmethod
    def service_delete_reimbursement(self, request_id):
        pass
