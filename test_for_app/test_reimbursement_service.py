from service_layer.implementation_classes.reimbursement_service import ReimbursementService
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from custom_exceptions.custom_exception_message import CustomExceptionMessage

redao = ReimbursementDAOImp()
reimbursement_service = ReimbursementService(redao)


def test_dao_update_reimbursement():
    try:
        reimbursement_service.service_update_reimbursement(3, "rejected", "test")
    except CustomExceptionMessage as c:
        assert str(c) == "No Such Reimbursement was found"
