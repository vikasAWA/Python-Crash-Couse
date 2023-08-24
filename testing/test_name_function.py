import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""
    
    def test_first_last_name(self):
        """Do names like 'Janis Japlin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, "Janis Joplin")
        
    def test_first_last_middle_name(self):
        """Do name Like 'Raj Kumar Yadav' works."""
        formatted_name = get_formatted_name('Raj', 'Yadav', 'kumar')
        self.assertEqual(formatted_name, 'Raj Kumar Yadav')
        
unittest.main()