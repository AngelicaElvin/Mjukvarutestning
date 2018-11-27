import keywords
import unittest
from keywords import KeywordProcessor


#First test for function __len__

class TestLen(unittest.TestCase):

    def setUp(self):
        print ("Starting...")
        self.kp = KeywordProcessor()


    def tearDown(self):
        print ("Ending.")


    def test_len(self):
        self.kp.add_keywords_from_dict({"add":["one"],"yes":["two"]})
        self.assertEqual(len(self.kp), 2)


    def test_get_item(self):
        self.kp.add_keyword('add','yes')
        self.assertEqual(self.kp["add"], "yes", "Word not in dictionary")

    def test_delitem(self):
        self.kp.add_keywords_from_dict({"numbers":["one","two"],"words":["everybody","loves","snow"]})
        self.assertEqual(self.kp.__delitem__("one"), True, "Unable to delete word")
    def test_add_non_word_boundary(self):
        self.kp.add_keyword('greetings','hello')
        self.assertEqual(self.kp.add_non_word_boundary("s"),"greetingss")

if __name__ =='__main__':
    unittest.main()
