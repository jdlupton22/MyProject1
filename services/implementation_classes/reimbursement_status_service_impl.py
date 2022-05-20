from daos.abstract_classes.reimbursement_status_dao import ReimbursementStatusDao


class ReimbursementStatusServiceImpl:
    def __init__(self, reimbursement_status_dao: ReimbursementStatusDao):
        self.reimbursement_status_dao = reimbursement_status_dao

    def service_read_reimbursement_status(self, request_id):
        return self.reimbursement_status_dao.read_reimbursement_status(request_id)

    def service_all_reimbursement_statuses(self):
        return self.reimbursement_status_dao.all_reimbursement_statuses()

    def service_update_reimbursement_status(self, change):
        return self.reimbursement_status_dao.update_reimbursement_status(change)
