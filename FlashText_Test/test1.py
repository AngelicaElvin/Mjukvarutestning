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
    """
    Since init only does internal things, we cannot test it with black box testing.
    """


# =================================================================== #

class TestFlashtext_contains(unittest.TestCase):


    def setUp(self):
        self.kp = KeywordProcessor()


    def test_contains_simple(self):
        """
        Check if simple words are available in the processor, a typical usage scenario.
        """
        self.kp.add_keyword("a")
        self.kp.add_keyword("House")
        self.assertTrue("a" in self.kp, "cannot find 'a' in 'a'")
        self.assertTrue("House" in self.kp, "House should be part of keywords")
        self.assertFalse("b" in self.kp, "b should not be in 'a'")


    def test_contains_empty(self):
        """
        Borderline test, check if correct behaviour when inputing empty string.
        """
        self.assertTrue("" not in self.kp, "'' cannot be contained")
        self.kp.add_keyword("")
        self.assertTrue("" not in self.kp, "'' cannot be contained")


    def test_contains_extreme(self):
        """
        Check that the contains function correctly handles extreme cases.
        """
        # Borderline: Long string
        self.kp.add_keyword(long_string)
        self.assertTrue(long_string in self.kp, "We can have long keywords")


    def test_contains_clean_words(self):
        """
        Check that the contains function properly adds keywords that have a
        corresponding cleanword and make sure that the cleanwords are not added.
        """
        # Normal: clean words
        self.kp.add_keyword("yellow", "blue")
        self.assertTrue("yellow" in self.kp, "keyword yellow should exist")
        self.assertFalse("blue" in self.kp, "Clean word not part of keywords")


    def test_contains_from_dict(self):
        """
        Does it handle dicts correctly?
        """
        # Normal: clean word using dicts
        keyword_dict = {"color": ["red", "green"]}
        self.kp.add_keywords_from_dict(keyword_dict)
        self.assertTrue("red" in self.kp, "red is a keyword word")
        self.assertTrue("green" in self.kp, "green is a keyword word")


    def test_contains_from_list(self):
        """
        Does it handle lists correctly?
        """
        # Normal: keyword from list
        self.kp.add_keywords_from_list(["brown", "orange"])
        self.assertTrue("brown" in self.kp, "keyword brown from list can be added")
        self.assertTrue("orange" in self.kp, "keyword orange from list can be added")


# =================================================================== #

class TestFlashtext_setitem(unittest.TestCase):


    def setUp(self):
        self.kp = KeywordProcessor()


    def test_setitem_basic(self):
        """
        Test a typical usage scenario.
        """
        self.kp["foo"] = "bar"
        self.assertTrue("foo" in self.kp, "we added a keyword")
        self.assertTrue("bar" is self.kp["foo"], "we can access the clean word")


    def test_setitem_empty(self):
        """
        Borderline test, check if correct behaviour when inputing empty string.
        """
        # Borderline: String of length 0
        self.kp[""] = ""
        self.assertEquals(len(self.kp), 0, "we do not add empty string")
        self.assertEquals(self.kp[""], None, "cannot access with empty string as key")


    def test_setitem_extreme(self):
        """
        Check that it functions correctly with extreme cases.
        """
        # Borderline: Long string
        self.kp[long_string] = long_string
        self.assertEquals(len(self.kp), 1, "we added the long string as keyword")
        self.assertEquals(self.kp[long_string], long_string, "we can access the long string")


# =================================================================== #

class TestFlashtext_set_non_word_boundaries(unittest.TestCase):

    def setUp(self):
        self.kp = KeywordProcessor()

    def test_set_non_word_boundaries_default(self):
        """
        Test the default behaviour, typical usage scenario.
        """
        self.kp.add_keyword("is12")
        self.kp.add_keyword("is")
        found = self.kp.extract_keywords("wow this is12 a sentence")
        self.assertTrue("is12" in found, "keyword can be letters and digits")
        self.assertTrue("is" not in found, "keyword not in sentence")


    def test_set_non_word_boundaries_basic(self):
        """
        Test with a non-default boundary.
        """
        self.kp.set_non_word_boundaries(set(string.letters))
        self.kp.add_keyword("is")
        found = self.kp.extract_keywords("wow this is12 a sentence")
        self.assertTrue("is" in found, "keyword doesnt include numbers")

    # TODO Extreme?

# =================================================================== #

class TestFlashtext_add_get_keyword(unittest.TestCase):


    def setUp(self):
        self.kp = KeywordProcessor()


    def test_add_keyword_basic(self):
        """
        Test a typical usage scenario.
        """
        self.kp.add_keyword("foo")
        self.assertTrue("foo" in self.kp, "can add basic keyword")


    def test_add_keyword_extreme(self):
        """
        Test extreme cases, both empty string and a very long string.
        """
        self.kp.add_keyword("")
        self.assertTrue(len(self.kp) is 0, "did not add empty string")

        self.kp.add_keyword(long_string)
        self.assertTrue(long_string in self.kp, "can add long keywords")


    def test_add_keyword_clean_basic(self):
        """
        Test that the optional feature clean word is working in a typical use case.
        """
        self.kp.add_keyword("foo", "bar")
        self.assertTrue(self.kp["foo"] is "bar", "bar is clean word for foo")


    def test_add_keyword_clean_extreme(self):
        """
        Test that the optional feature clean word is working in an extreme use case.
        """
        self.kp.add_keyword("", "")
        self.assertTrue(len(self.kp) is 0, "cannot add empty string")

        self.kp.add_keyword(long_string)
        self.assertTrue(self.kp[long_string] is long_string, "can access clean word for a long string")


# =================================================================== #

# class TestFlashtext_get_keyword(unittest.TestCase):
"""
Testing this functionallity in the test class TestFlashtext_add_get_keyword above.
"""

# =================================================================== #

class TestFlashtext_add_keywords_from_dict(unittest.TestCase):


    def setUp(self):
        self.kp = KeywordProcessor()


    def test_add_keywords_from_dict_basic(self):
        """
        Test a typical usage scenario.
        """
        self.kp.add_keywords_from_dict({"color": ["yellow", "red"]})
        self.assertTrue("yellow" in self.kp, "yellow was added as a keyword")
        self.assertTrue("red" in self.kp, "red was added as a keyword")
        self.assertTrue(self.kp["yellow"] is "color", "keyword maps to clean word")
        self.assertTrue(self.kp["red"] is "color", "keyword maps to clean word")


    def test_add_keywords_from_dict_empty(self):
        """
        Test for borderline case empty string.
        """
        self.kp.add_keywords_from_dict({"": [""]})
        self.assertTrue(len(self.kp) is 0, "cannot add emtpy string")


    def test_add_keywords_from_dict_extreme(self):
        """
        Test for an extreme usage scenario, long keyword string.
        """
        self.kp.add_keywords_from_dict({long_string: [long_string]})
        self.assertTrue(long_string in self.kp, "keyword added")
        self.assertTrue(self.kp[long_string] is long_string, "long keyword maps to long clean word")


# =================================================================== #

class TestFlashtext_add_keywords_from_list(unittest.TestCase):


    def setUp(self):
        self.kp = KeywordProcessor()


    def test_add_keywords_from_list_basic(self):
        """
        Test a typical usage scenario.
        """
        mlist = ["one", "two", "three", "four", "five"]
        self.kp.add_keywords_from_list(mlist)
        [self.assertTrue(item in self.kp, "keyword not added") for item in mlist]


    def test_add_keywords_from_list_error(self):
        """
        Test that an exception is procuced on wrong input.
        """
        # argument must be a list
        with self.assertRaises(AttributeError):
            self.kp.add_keywords_from_list("im a string")

    def test_add_keywords_from_list_extreme(self):
        """
        Test the borderline case when the string is empty.
        """
        self.kp.add_keywords_from_list(["", ""])
        self.assertTrue(len(self.kp) is 0, "cannot add empty string")


    def test_add_keywords_from_list_extreme(self):
        """
        Test the borderline case when the string is very long.
        """
        mlist = [long_string, long_string + " abc"]
        self.kp.add_keywords_from_list(mlist)
        [self.assertTrue(item in self.kp, "keyword not added") for item in mlist]


# =================================================================== #

class TestFlashtext_get_all_keywords(unittest.TestCase):


    def setUp(self):
        self.kp = KeywordProcessor()


    def test_get_all_keywords_basic(self):
        """
        Test a typical usage scenario.
        """
        basic_list = ["one", "two", "three"]
        self.kp.add_keywords_from_list(basic_list)
        [self.assertTrue(key in basic_list, "keyword was retrived ok") for key in self.kp.get_all_keywords()]


    def test_get_all_keywords_empty(self):
        """
        Test with emtpy string.
        """
        self.kp.add_keyword("")
        self.assertTrue(len(self.kp.get_all_keywords()) is 0, "cannot add empty string")


    def test_get_all_keywords_extreme(self):
        """
        Tests borderline case with a long string.
        """
        self.kp.add_keyword("long", long_string)
        self.assertTrue(long_string == self.kp.get_all_keywords()["long"], "long string as keyword")


# =================================================================== #

class TestFlashtext_replace(unittest.TestCase):


    def setUp(self):
        self.kp = KeywordProcessor()


    def test_replace_normal(self):
        """
        Test a typical usage scenario.
        """
        # Normal: Replace ONE word
        self.kp["Crabs"] = "Trolls"
        str = self.kp.replace_keywords("Crabs live in the forest")
        self.assertTrue(str == "Trolls live in the forest")

        # Normal: Replace multiple words
        self.kp["Gloves"] = "Handskar"
        self.kp["Boots"] = "Stövlar"
        self.kp["Hats"] = "Hattar"
        str = self.kp.replace_keywords(
            "Alway remember to bring Gloves, boots and hats"
        )
        self.assertEqual(
            str,
            "Alway remember to bring Handskar, Stövlar and Hattar"
        )


    def test_replace_case_sensitive(self):
        """
        Test case sensitivity. When the keyword processor is in case sensitive
        mode then only words with a matching case will be regarded as possible
        results. It defaults to case-insensitive where all word regardless of
        case are considered.
        """
        # Normal: Test multi-word replace with case insensitivity
        self.kp["Blue"] = "Purple"
        self.kp["Red"] = "Magenta"
        str = self.kp.replace_keywords("Colors blue and red are nice")
        self.assertEqual(str, "Colors Purple and Magenta are nice")

        # Create case-sensitive keyword processor
        case_kp = KeywordProcessor(case_sensitive=True)

        # Normal: Test multi-word replace with case sensitivity
        case_kp["Blue"] = "Purple"
        case_kp["Red"] = "Magenta"
        str = case_kp.replace_keywords("Colors blue and red are nice")
        self.assertTrue(str, "Colors blue and red are nice")


    def test_replace_dict(self):
        """
        Test that replace works properly with dicts.
        """
        # Add some more keywords from list
        self.kp.add_keywords_from_dict({
            "Rabbits": ["Trolls"],
            "on": ["in"],
            "beach": ["forest"]
        })
        str = self.kp.replace_keywords("Trolls live in the forest")
        self.assertTrue(str == "Rabbits live on the beach")

        # Multiple keyword with same cleanword
        self.kp.add_keywords_from_dict({
            "color": ["yellow", "brown"],
            "fruits": ["oranges", "apples", "pears"]
        })
        str = self.kp.replace_keywords(
            "Colors are yellow, brown or other."
            "While fruits are oranges, apples or pears"
        )
        self.assertTrue(str ==
            "Colors are color, color or other."
            "While fruits are fruits, fruits or fruits"
        )


    def test_replace_extended(self):
        """
        Check replacing for some extended examples where there might be words
        that are connected by a delimiting character.
        """
        # Normal: Test connected words
        self.kp.add_keywords_from_dict({
            "Cannon": ["Water"],
            "balls": ["slides"]
        })
        str = self.kp.replace_keywords("Water-slides are deadly")
        self.assertEqual(str, "Cannon-balls are deadly")


    def test_replace_empty(self):
        """
        Test the borderline case when the string is empty.
        """
        # Borderline: Empty replacement (clean) word
        self.kp.add_keywords_from_dict({
            "": ["red, green, blue, yellow"]
        })
        str = self.kp.replace_keywords(
            "colors still exist, red, yellow, blue and green are all gone"
        )
        self.assertEqual(
            str,
            "colors still exist, red, yellow, blue and green are all gone"
        )


    def test_replace_extreme(self):
        """
        Test bordeline cases such as when replacing words that correspond to a
        long keyword or recursive. When one word to replace is replaced with
        another word that is to be replaced
        """
        # Extreme: Replace two long "keywords"
        self.kp.add_keywords_from_dict({
            "hej": [long_string]
        })
        str = self.kp.replace_keywords(long_string + " " + long_string)
        self.assertEqual(str, "hej hej")

        # Borderline: Replace into replacement word
        self.kp.add_keywords_from_dict({
            "fruit": ["orange", "apple", "pear"],
            "pear": ["fruit"]
        })
        str = self.kp.replace_keywords(
            "Fruits, such as the fruit orange, apple or pear"
        )
        self.assertEqual(
            str,
            "Fruits, such as the pear fruit, fruit or fruit"
        )


# =================================================================== #

if __name__=="__main__":
    unittest.main(verbosity=2)
