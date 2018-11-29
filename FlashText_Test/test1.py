# coding: utf-8

"""# =================================================================== #
 ____    ___                     __      ______                __        ______                __
/\  _`\ /\_ \                   /\ \    /\__  _\              /\ \__    /\__  _\              /\ \__
\ \ \L\_\//\ \      __      ____\ \ \___\/_/\ \/    __   __  _\ \ ,_\   \/_/\ \/    __    ____\ \ ,_\
 \ \  _\/ \ \ \   /'__`\   /',__\\ \  _ `\ \ \ \  /'__`\/\ \/'\\ \ \/      \ \ \  /'__`\ /',__\\ \ \/
  \ \ \/   \_\ \_/\ \L\.\_/\__, `\\ \ \ \ \ \ \ \/\  __/\/>  </ \ \ \_      \ \ \/\  __//\__, `\\ \ \_
   \ \_\   /\____\ \__/.\_\/\____/ \ \_\ \_\ \ \_\ \____\/\_/\_\ \ \__\      \ \_\ \____\/\____/ \ \__\
    \/_/   \/____/\/__/\/_/\/___/   \/_/\/_/  \/_/\/____/\//\/_/  \/__/       \/_/\/____/\/___/   \/__/
"""# =================================================================== #

"""
@author Christoffer Gustfsson, Filip Björklund
@group  11
@desc   This is a test of the Python library FlashText:
        https://github.com/vi3k6i5/flashtext
"""


"""# =================================================================== #
 ______                                     __
/\__  _\                                   /\ \__
\/_/\ \/     ___ ___   _____     ___   _ __\ \ ,_\
   \ \ \   /' __` __`\/\ '__`\  / __`\/\`'__\ \ \/
    \_\ \__/\ \/\ \/\ \ \ \L\ \/\ \L\ \ \ \/ \ \ \_
    /\_____\ \_\ \_\ \_\ \ ,__/\ \____/\ \_\  \ \__\
    \/_____/\/_/\/_/\/_/\ \ \/  \/___/  \/_/   \/__/
                         \ \_\
                          \/_/
"""# =================================================================== #

import unittest
from keywords import *
import string


"""# =================================================================== #
 __  __  __         ___
/\ \/\ \/\ \__  __ /\_ \
\ \ \ \ \ \ ,_\/\_\\//\ \
 \ \ \ \ \ \ \/\/\ \ \ \ \
  \ \ \_\ \ \ \_\ \ \ \_\ \_
   \ \_____\ \__\\ \_\/\____\
    \/_____/\/__/ \/_/\/____/
"""# =================================================================== #

long_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a iaculis diam. Sed et ante ante. Aliquam quis turpis iaculis, vehicula nisl non, mollis elit. In hac habitasse platea dictumst. Nulla vestibulum lorem facilisis porta laoreet. Duis vulputate eros ac augue maximus, et bibendum dui luctus. Aliquam nisl lorem, pulvinar at turpis a, tempus porta est. Cras risus mi, fermentum laoreet tempor vitae, scelerisque a turpis. Donec eu interdum ligula, vel ullamcorper arcu. Nam facilisis urna ultricies nunc iaculis, quis volutpat urna aliquet. Duis in felis sit amet tortor rutrum facilisis. Donec non pellentesque elit. Sed sit amet gravida lorem. Mauris odio ante, interdum eu convallis eu, volutpat malesuada velit. Aliquam sed tincidunt justo.
"""

"""# =================================================================== #
 ____    ___                    __          ____                       ______                __
/\  _`\ /\_ \                  /\ \        /\  _`\                    /\__  _\              /\ \__
\ \ \L\ \//\ \      __      ___\ \ \/'\    \ \ \L\ \    ___   __  _   \/_/\ \/    __    ____\ \ ,_\   ____
 \ \  _ <'\ \ \   /'__`\   /'___\ \ , <     \ \  _ <'  / __`\/\ \/'\     \ \ \  /'__`\ /',__\\ \ \/  /',__\
  \ \ \L\ \\_\ \_/\ \L\.\_/\ \__/\ \ \\`\    \ \ \L\ \/\ \L\ \/>  </      \ \ \/\  __//\__, `\\ \ \_/\__, `\
   \ \____//\____\ \__/.\_\ \____\\ \_\ \_\   \ \____/\ \____//\_/\_\      \ \_\ \____\/\____/ \ \__\/\____/
    \/___/ \/____/\/__/\/_/\/____/ \/_/\/_/    \/___/  \/___/ \//\/_/       \/_/\/____/\/___/   \/__/\/___/
"""# =================================================================== #

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
        self.assertTrue("is" in found, "keyword doesnt include numbers")


# =================================================================== #

class TestFlashtext_add_get_keyword(unittest.TestCase):
    """
    this allowed, have two functions tested in one test?
    """
    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()


    def tearDown(self):
        print "OK"


    def test_add_keyword_basic(self):
        self.kp.add_keyword("foo")
        self.assertTrue("foo" in self.kp, "can add basic keyword")

    def test_add_keyword_extreme(self):
        self.kp.add_keyword("")
        self.assertTrue(len(self.kp) is 0, "did not add empty string")

        self.kp.add_keyword(long_string)
        self.assertTrue(long_string in self.kp, "can add long keywords")

    def test_add_keyword_clean_basic(self):
        self.kp.add_keyword("foo", "bar")
        self.assertTrue(self.kp["foo"] is "bar", "bar is clean word for foo")

    def test_add_keyword_clean_extreme(self):
        self.kp.add_keyword("", "")
        self.assertTrue(len(self.kp) is 0, "cannot add empty string")

        self.kp.add_keyword(long_string)
        self.assertTrue(self.kp[long_string] is long_string, "can access clean word for a long string")


# =================================================================== #

"""
Can we skip this and use the test above for both functions?
"""
# class TestFlashtext_get_keyword(unittest.TestCase):

#     def setUp(self):
#         print "run " + self._testMethodName
#         self.kp = KeywordProcessor()


#     def tearDown(self):
#         print "OK"


#     def test_get_keyword_basic(self):
#         pass


# =================================================================== #

class TestFlashtext_add_keywords_from_dict(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()


    def tearDown(self):
        print "OK"


    def test_add_keywords_from_dict_basic(self):
        self.kp.add_keywords_from_dict({"color": ["yellow", "red"]})
        self.assertTrue("yellow" in self.kp, "yellow was added as a keyword")
        self.assertTrue("red" in self.kp, "red was added as a keyword")
        self.assertTrue(self.kp["yellow"] is "color", "keyword maps to clean word")
        self.assertTrue(self.kp["red"] is "color", "keyword maps to clean word")


    def test_add_keywords_from_dict_extreme(self):
        self.kp.add_keywords_from_dict({"": [""]})
        self.assertTrue(len(self.kp) is 0, "cannot add emtpy string")

        self.kp.add_keywords_from_dict(
            {long_string: [long_string]}
        )
        self.assertTrue(long_string in self.kp, "keyword added")
        self.assertTrue(self.kp[long_string] is long_string, "long keyword maps to long clean word")


# =================================================================== #

class TestFlashtext_add_keywords_from_list(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()


    def tearDown(self):
        print "OK"


    def test_add_keywords_from_list_basic(self):
        mlist = ["one", "two", "three", "four", "five"]
        self.kp.add_keywords_from_list(mlist)
        [self.assertTrue(item in self.kp, "keyword not added") for item in mlist]


    def test_add_keywords_from_list_error(self):
        # argument must be a list
        with self.assertRaises(AttributeError):
            self.kp.add_keywords_from_list("im a string")


    def test_add_keywords_from_list_extreme(self):
        self.kp.add_keywords_from_list(["", ""])
        self.assertTrue(len(self.kp) is 0, "cannot add empty string")

        mlist = [long_string, long_string + " abc"]
        self.kp.add_keywords_from_list(mlist)
        [self.assertTrue(item in self.kp, "keyword not added") for item in mlist]


# =================================================================== #

class TestFlashtext_get_all_keywords(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor()


    def tearDown(self):
        print "OK"


    def test_get_all_keywords_basic(self):
        basic_list = ["one", "two", "three"]
        self.kp.add_keywords_from_list(basic_list)
        [self.assertTrue(key in basic_list, "keyword was retrived ok") for key in self.kp.get_all_keywords()]

    def test_get_all_keywords_extreme(self):
        self.kp.add_keyword("")
        self.assertTrue(len(self.kp.get_all_keywords()) is 0, "cannot add empty string")

        self.kp.add_keyword("long", long_string)
        self.assertTrue(long_string == self.kp.get_all_keywords()["long"], "long string as keyword")


"""# =================================================================== #
 __      __  __          __               ____                       ______                __
/\ \  __/\ \/\ \      __/\ \__           /\  _`\                    /\__  _\              /\ \__
\ \ \/\ \ \ \ \ \___ /\_\ \ ,_\    __    \ \ \L\ \    ___   __  _   \/_/\ \/    __    ____\ \ ,_\   ____
 \ \ \ \ \ \ \ \  _ `\/\ \ \ \/  /'__`\   \ \  _ <'  / __`\/\ \/'\     \ \ \  /'__`\ /',__\\ \ \/  /',__\
  \ \ \_/ \_\ \ \ \ \ \ \ \ \ \_/\  __/    \ \ \L\ \/\ \L\ \/>  </      \ \ \/\  __//\__, `\\ \ \_/\__, `\
   \ `\___x___/\ \_\ \_\ \_\ \__\ \____\    \ \____/\ \____//\_/\_\      \ \_\ \____\/\____/ \ \__\/\____/
    '\/__//__/  \/_/\/_/\/_/\/__/\/____/     \/___/  \/___/ \//\/_/       \/_/\/____/\/___/   \/__/\/___/
"""# =================================================================== #





# =================================================================== #

if __name__=="__main__":
    unittest.main()