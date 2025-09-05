import unittest

from Journal_Practice import AnonymousSurvey

class AnonymousSurveyTest(unittest.TestCase):

    def setUp(self):
        question = "What is your name? "
        self.survey1 = AnonymousSurvey(question)
        self.responses = ["Arsalan", "Mueed", "Saim"]


    def test_single_response(self):
        question = "What is your name? "
        survey1 = AnonymousSurvey(question)
        survey1.store_response("Arsalan")
        self.assertIn("Arsalan", survey1.response)

    def test_multiple_response(self):
        question = "What is your name? "
        survey1 = AnonymousSurvey(question)
        responses = ["Arsalan", "Mueed", "Saim"]
        for i in responses:
            survey1.store_response(i)
        for j in responses:
            self.assertIn(j, survey1.response)

if __name__ == "__main__":
    unittest.main()

