from entities.reimbursement import Reimbursement
from daos.implementation_classes.reimbursement_dao_impl import ReimbursementDaoImpl
from enums.event_type import EventType

reimbursement_dao = ReimbursementDaoImpl()
reimbursement1 = Reimbursement(0, 1003, "Online", 30.00, EventType("SEMINAR"), "company suggested",
                               "suggest by management", "Present or Absent", "Present")
reimbursement_update = Reimbursement(4, 1003, "Online", 75.00, EventType("SEMINAR"), "company suggested",
                                     "suggest by management", "Present or Absent", "Present")


def test_dao_create_reimbursement():
    returned_reimbursement = reimbursement_dao.create_reimbursement(reimbursement1)
    assert returned_reimbursement.reimbursement_id != 0


def test_dao_get_reimbursement():
    returned_reimbursement = reimbursement_dao.read_reimbursement(3)
    assert returned_reimbursement[0].reimbursement_id != 0


def test_dao_update_reimbursement():
    updated_reimbursement = reimbursement_dao.update_reimbursement(reimbursement_update)
    assert updated_reimbursement.ev_cost == 75.00


def test_dao_delete_reimbursement():
    returned_bol = reimbursement_dao.delete_reimbursement(5)
    assert returned_bol == bool
