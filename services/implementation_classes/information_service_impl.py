from daos.abstract_classes.information_dao import InformationDao


class InformationServiceImpl:
    def __init__(self, information_dao: InformationDao):
        self.information_dao = information_dao

    def service_create_information(self, information):
        return self.information_dao.create_information(information)

    def service_read_information(self, info_id):
        return self.information_dao.read_information(info_id)

    def service_all_informations(self):
        return self.information_dao.all_informations()

    def service_update_information(self, change):
        return self.information_dao.update_information(change)

    def service_delete_information(self, info_id):
        return self.information_dao.delete_information(info_id)