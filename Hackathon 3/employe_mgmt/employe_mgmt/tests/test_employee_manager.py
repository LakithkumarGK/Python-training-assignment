import unittest
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_and_find_employee(self):
        emp = self.manager.add_employee("Ravi", "Sales", "Executive", 40000, 4000, 2000)
        found = self.manager.search_by_employee_id(emp.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Ravi")

    def test_delete_employee(self):
        emp = self.manager.add_employee("Maya", "Finance", "Analyst", 70000, 7000, 3000)
        deleted = self.manager.delete_employee(emp.id)
        self.assertTrue(deleted)
        self.assertIsNone(self.manager.search_by_employee_id(emp.id))

    def test_to_and_from_dict_list(self):
        emp = self.manager.add_employee("Nina", "IT", "Developer", 55000, 5500, 1500)
        
        # Convert to list of dictionaries
        dict_list = self.manager.to_dict_list()

        # Load into a new manager from that list
        new_manager = EmployeeManager()
        new_manager.load_employees(dict_list)

        # Verify restored employee data
        self.assertEqual(len(new_manager.get_all_employees()), 1)
        restored_emp = new_manager.get_all_employees()[0]
        self.assertEqual(restored_emp.name, "Nina")
        self.assertEqual(restored_emp.net_salary, emp.net_salary)
