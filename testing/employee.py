class Employee():
    """Create an instance Employee."""
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name =last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, raise_amount=5000):
        """Method to give a raise in annual salary."""
        self.annual_salary += raise_amount
        