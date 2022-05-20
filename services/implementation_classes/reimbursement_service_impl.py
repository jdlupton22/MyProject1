from daos.abstract_classes.reimbursement_dao import ReimbursementDao


class ReimbursementServiceImpl:
    def __init__(self, reimbursement_dao: ReimbursementDao):
        self.reimbursement_dao = reimbursement_dao

    def service_create_reimbursement(self, reimbursement):
        return self.reimbursement_dao.create_reimburse_request(reimbursement)

    def service_read_reimbursement(self, request_id):
        return self.reimbursement_dao.read_reimbursement(request_id)

    def service_all_reimbursements(self):
        return self.reimbursement_dao.all_reimbursements()

    def service_update_reimbursement(self, change):
        return self.reimbursement_dao.update_reimbursement(change)

    def service_delete_reimbursement(self, request_id):
        return self.reimbursement_dao.delete_reimbursement(request_id)
