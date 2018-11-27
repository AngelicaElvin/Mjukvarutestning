import unittest
from keywords import *
import string

# =================================================================== #

long_string = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut auctor risus ut tincidunt iaculis. Nullam vestibulum cursus arcu, eleifend tempus ex facilisis vitae. Nullam egestas euismod eros eget egestas. In pulvinar justo sit amet dapibus aliquam. Vivamus tincidunt mi nec iaculis ultrices. Nulla pulvinar et metus nec ullamcorper. Proin bibendum ligula ut auctor laoreet. Curabitur tincidunt, ex non laoreet facilisis, diam odio faucibus ligula, ac commodo lectus nisl ut lacus. Praesent et est ac ipsum vestibulum facilisis sit amet eget justo. Etiam quis felis ut neque consectetur consectetur at sit amet metus. Curabitur molestie justo nec massa tincidunt, condimentum suscipit dui euismod.
"""

# =================================================================== #

class TestFlashtext_init(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_variable_fields_are_set(self):
        """
        """
        self.assertEqual(self.kp._keyword, '_keyword_')


# =================================================================== #

class TestFlashtext_contains(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_contains_simple(self):
        self.kp.add_keyword("a")
        # simple case true
        self.assertTrue("a" in self.kp, "cannot find 'a' in 'a'")
        # simple case false
        self.assertFalse("b" in self.kp, "b should not be in 'a'")

    def test_contains_extreme(self):
        # borderline case
        self.assertTrue("" not in self.kp, "'' cannot be contained")
        global long_string
        # extreme case
        self.kp.add_keyword(long_string)
        self.assertTrue(long_string in self.kp, "We can have long keywords")

    def test_contains_clean_words(self):
        # clean words
        self.kp.add_keyword("yellow", "blue")
        self.assertTrue("yellow" in self.kp, "keyword yellow should exist")
        self.assertFalse("blue" in self.kp, "Clean word not part of keywords")
        # clean word using dicts
        keyword_dict = {"color": ["red", "green"]}
        self.kp.add_keywords_from_dict(keyword_dict)
        self.assertTrue("red" in self.kp, "red is a keyword word")
        self.assertTrue("green" in self.kp, "green is a keyword word")

    def test_contains_from_list(self):
        # keyword from list
        self.kp.add_keywords_from_list(["brown", "orange"])
        self.assertTrue("brown" in self.kp, "keyword brown from list can be added")
        self.assertTrue("orange" in self.kp, "keyword orange from list can be added")


# =================================================================== #

class TestFlashtext_setitem(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_setitem_basic(self):
        self.kp["foo"] = "bar"
        self.assertTrue("foo" in self.kp, "we added a keyword")
        self.assertTrue("bar" is self.kp["foo"], "we can access the clean word")

    def test_setitem_extreme(self):
        # edge case 0 lenth string
        self.kp[""] = ""
        self.assertEquals(len(self.kp), 0, "we do not add empty string")
        self.assertEquals(self.kp[""], None, "cannot access with empty string as key")
        # long string
        global long_string
        self.kp[long_string] = long_string
        self.assertEquals(len(self.kp), 1, "we added the long string as keyword")
        self.assertEquals(self.kp[long_string], long_string, "we can access the long string")


# =================================================================== #

class TestFlashtext_set_non_word_boundaries(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()

    def tearDown(self):
        print "OK"

    def test_set_non_word_boundaries_default(self):
        self.kp.add_keyword("is12")
        self.kp.add_keyword("is")
        found = self.kp.extract_keywords("wow this is12 a sentence")
        self.assertTrue("is12" in found, "keyword can be letters and digits")
        self.assertTrue("is" not in found, "keyword not in sentence")

    def test_set_non_word_boundaries_basic(self):
        self.kp.set_non_word_boundaries(set(string.letters))
        self.kp.add_keyword("is")
        found = self.kp.extract_keywords("wow this is12 a sentence")
        print "HERE IT COMES"
        print found
        self.assertTrue("is" in found, "keyword doesnt include numbers")


# =================================================================== #


if __name__=="__main__":
    unittest.main()
