#FlashText Test
#
# Authors: Angelica Elvin and Alexander Engberg
# Group 11
# This is a test for Python library FlashText
# https://github.com/vi3k6i5/flashtext
#
# The tests in this file are black box testing.
#
# The functions from Python library FlashText that are tested
# in this file are len, getitem, delitem, add_non_word_boundary, remove_keyword,
# add_keyword_from_file, remove_keywords_from_dict and remove_keywords_from_list.


import keywords
import unittest
import string
from keywords import *

test_dictionary = {"This":["1"], "is":["2"], "for":["3"], "testing":["4"]}
test_list = ["This", "is", "for", "testing"]

# Class Test_len which tests function __len__

class Test_len(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_len_basic(self):
        self.kp.add_keyword("a")
        self.assertEqual(len(self.kp), 1)

    def test_len_dictionary(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertEqual(len(self.kp), 4)

    def test_len_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(len(self.kp),4)


# Class Test_getitem which tests function __getitem__

class Test_getitem(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_getitem_basic(self):
        self.kp.add_keyword('colour','green')
        self.assertEqual(self.kp["colour"], "green", "Word not found")

    def test_getitem_dictionary(self):
        keyword_dict = {"color": ["red"]}
        self.kp.add_keywords_from_dict(keyword_dict)
        #self.assertEqual(self.kp.__getitem__("red"), "colour", "Word not found")


    def test_getitem_dict(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertTrue("1" in self.kp, "keyword This exists")
        #self.assertTrue(self.kp['This'], '1', "Word not found")
        #self.assertEqual(self.kp.__getitem__(),["1", "2", "3", "4"] , "Words not found")

    def test_getitem_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(self.kp.__getitem__("This"), "This", "Word not found")


# Class Test_delitem which tests function __delitem__

class Test_delitem(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_delitem(self):
        self.kp.add_keyword('animal')
        self.assertEqual(self.kp.__delitem__("animal"), True, "Unable to delete word")

    def test_delitem_dict(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertEqual(self.kp.__delitem__("1"), True, "Unable to delete word")

    def test_delitem_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(self.kp.__delitem__("This"), True, "Unable to delete word")

# Class Test_add_non_word_boundary which tests function add_non_word_boundary

class Test_add_non_word_boundary(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()


    def tearDown(self):
        print "OK"

    def test_add_non_word_boundary_basic(self):
        self.kp.add_keyword('succes','work')
        #self.assertEqual(self.kp.add_non_word_boundary("s"), None)

    def test_add_non_word_boundary_dict(self):


# Class Test_remove_keyword which tests function remove_keyword

class Test_remove_keyword(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_remove_keyword(self):
        self.kp.add_keywords_from_dict({"Remove":["one"],"a":["two"], "word":["three"]})
        self.assertEqual(self.kp.remove_keyword("three"), True, "Could not remove word")

# Class Test_add_keyword_from_file which tests function add_keyword_from_file

class Test_add_keyword_from_file(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    #def test_add_keyword_from_file(self):
    #    self.kp.add_keywords_from_dict({"Add":["one"]})
    #    self.assertEqual(self.kp.add_keyword_from_file('keyword_file.txt'), True, "Could not add word from file")

# Class Test_remove_keywords_from_dict which tests function remove_keywords_from_dict

class Test_remove_keywords_from_dict(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

# Class Test_remove_keywords_from_list which tests function remove_keywords_from_list

class Test_remove_keywords_from_list(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"



if __name__ =='__main__':
    unittest.main()
