import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp = Employee('vikas', 'awasthi', 30000)
    
    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.annual_salary, 35000)
        
    def test_give_custom_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.annual_salary, 40000)
        
unittest.main()