from abc import ABC, abstractmethod


class EmployeeDao(ABC):

    @abstractmethod
    def create_employee(self, employee):
        pass

    @abstractmethod
    def read_employee(self, emp_id):
        pass

    @abstractmethod
    def all_employees(self):
        pass

    @abstractmethod
    def update_employee(self, change):
        pass

    @abstractmethod
    def delete_employee(self, emp_id):
        pass
