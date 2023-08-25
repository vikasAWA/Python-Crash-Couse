import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for class AnonumousSurvey"""
    
    def setUp(self):
        """
        Create a Survey question and store reponse to use them in test methods.
        """
        question = "What is your favourite language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Hindi', 'Python']
    
    def test_store_single_response(self):
        """Test that a single response is stored propery."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_response(self):
        """Test that three individual responses is stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
            
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            
        
           
    
        
    
unittest.main()
        