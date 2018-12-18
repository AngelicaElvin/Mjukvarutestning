"""
FlashText Test

Authors: Angelica Elvin & Alexander Engberg
Group 11
This is a test for Python library FlashText
https://github.com/vi3k6i5/flashtext

The tests in this file are black box testing.

The functions from Python library FlashText that are tested
in this file are len, getitem, delitem, add_non_word_boundary, remove_keyword,
add_keyword_from_file, remove_keywords_from_dict, remove_keywords_from_list and extract_keywords.
"""

import keywords
import unittest
import string
from keywords import *

"""
Test dictionary,list and string. These are reused for the test cases.
"""
test_dictionary = {"This":["1"], "is":["2"], "for":["3"], "testing":["4"]}
test_list = ["This", "is", "for", "testing"]
test_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a iaculis diam. Sed et ante ante. Aliquam quis turpis iaculis, vehicula nisl non, mollis elit. In hac habitasse platea dictumst. Nulla vestibulum lorem facilisis porta laoreet. Duis vulputate eros ac augue maximus, et bibendum dui luctus. Aliquam nisl lorem, pulvinar at turpis a, tempus porta est. Cras risus mi, fermentum laoreet tempor vitae, scelerisque a turpis. Donec eu interdum ligula, vel ullamcorper arcu. Nam facilisis urna ultricies nunc iaculis, quis volutpat urna aliquet. Duis in felis sit amet tortor rutrum facilisis. Donec non pellentesque elit. Sed sit amet gravida lorem. Mauris odio ante, interdum eu convallis eu, volutpat malesuada velit. Aliquam sed tincidunt justo.
"""

"""
Class Test_len which tests function __len__. Len() calculates the number of terms present in a dictionary.
"""
class Test_len(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"
        """
        Test case basic where we only put in one keyword. It is suppose to give 1 since the number of terms is one.
        """
    def test_len_basic(self):
        self.kp.add_keyword("keyword")
        self.assertEqual(len(self.kp), 1, "The length did not match")

        """
        Test case normal with dictionary. Make sure that having dictionary as input calculates the right amount of terms.
        """
    def test_len_dictionary(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertEqual(len(self.kp), 4, "The length did not match")

        """
        Test case normal with list. Make sure that having list as input calculates the right amount of terms.
        """
    def test_len_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(len(self.kp),4, "The length did not match")

        """
        Test case normal from file. Make sure that having a file as input calculates the right amount of terms.
        """
    def test_len_file(self):
        self.kp.add_keyword_from_file('keyword_file.txt')
        self.assertEqual(len(self.kp), 1,"The length did not match")

        """
        Test case extreme with an empty string. Making sure that the amount of terms is 0.
        """
    def test_len_empty(self):
        self.kp.add_keyword('')
        self.assertEqual(len(self.kp),0, "The length did not match")

        """
        Test case extreme with a long string. The string has 114 words, but should be calculated as one term (one string).
        """
    def test_len_extreme(self):
        self.kp.add_keyword(test_string)
        self.assertEqual(len(self.kp), 1, "The length did not match")

"""
Class Test_getitem which tests function __getitem__. Getitem() fetches a keyword and returnes its clean word
if the word is present in KeywordProcessor.
"""
class Test_getitem(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """
        Test case basic having only one keyword with its additional clean word. Making sure that the function
        finds the word present in KeywordProcessor and returns its clean word.
        """
    def test_getitem_basic(self):
        self.kp.add_keyword('colour','green')
        self.assertEqual(self.kp.__getitem__("colour"), "green", "Word not found")

        """
        Test case normal with a dictionary. Having several words in the dictionary and making sure that the function
        """
    def test_getitem_dict(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertTrue("1" in self.kp, "keyword <This> exists")
        self.assertEqual(self.kp.__getitem__("1"), "This", "Word not found")

        """
        Test case normal with a list. Having several words in the list and making sure that the function is able
        to find it.
        """
    def test_getitem_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(self.kp.__getitem__("This"), "This", "Word not found")

        """
        Test case normal with a file. Having one keyword in the file and making sure that the function returns its
        clean word.
        """
    def test_getitem_file(self):
        self.kp.add_keyword_from_file("keyword_file.txt")
        self.assertEqual(self.kp.__getitem__("keyword"), "file", "Word not found")

        """
        Test case with empty string.
        """
    def test_getitem_empty(self):
        self.kp.add_keyword(' ',' ')
        self.assertEqual(self.kp.__getitem__(' '), ' ', "Could not get empty string")

        """
        Test case with empty string extreme. Asserting False, could not add totaly
        empty string.
        """
    def test_getitem_empty_extreme(self):
        self.kp.add_keyword('')
        self.assertFalse(self.kp.__getitem__(''), "Could add empty string")

"""
Class Test_delitem which tests function __delitem__. Delitem() takes the argument keyword
and the clean name for it and removes it from the dictionary.
"""
class Test_delitem(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """
        Test case basic. Takes one word and removes it from dictionary.
        """
    def test_delitem(self):
        self.kp.add_keyword('animal')
        self.assertEqual(self.kp.__delitem__("animal"), True, "Unable to delete word")

        """
        Test case normal. Takes one dictionary and removes one keyword when giving the
        clean name for it.
        """
    def test_delitem_dict(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertEqual(self.kp.__delitem__("1"), True, "Unable to delete word")

        """
        Test case normal. Takes one list and removes one word.
        """
    def test_delitem_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(self.kp.__delitem__("This"), True, "Unable to delete word")

        """
        Test case with empty string. This should return false.
        """
    def test_delitem_empty(self):
        self.kp.add_keyword('')
        self.assertEqual(self.kp.__delitem__(''), False, "Unable to delete word")

        """
        Test case extreme. Removing a word that is not found within the dictionary.
        """
    def test_delitem_extreme(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertEqual(self.kp.__delitem__("item"), False, "Able to delete word")

"""
Class Test_add_non_word_boundary which tests function add_non_word_boundary.
Add_non_word_boundary()
"""
class Test_add_non_word_boundary(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """
        Test case default. Testing
        """
    def test_add_non_word_boundary_default(self):
        self.kp.add_keyword("is12")
        self.kp.add_keyword("is")
        found = self.kp.extract_keywords("wow this is12 a sentence")
        self.assertTrue("is12" in found, "keyword can be letters and digits")
        self.assertTrue("is" not in found, "keyword not in sentence")

        """

        """
    def test_add_non_word_boundary_basic(self):
        self.kp.set_non_word_boundaries(set())
        self.kp.add_non_word_boundary(string.letters)
        self.kp.add_keyword("is")
        found = self.kp.extract_keywords("wow this is12 a sentence")
        self.assertTrue("is" in found, "keyword doesnt include numbers")


"""
Class Test_remove_keyword which tests function remove_keyword
"""
class Test_remove_keyword(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """

        """
    def test_remove_keyword_basic(self):
        self.kp.add_keyword('animal')
        self.assertEqual(self.kp.remove_keyword("animal"), True, "Could not remove word")

        """

        """
    def test_remove_keyword_empty(self):
        self.kp.add_keyword(' ')
        self.assertEqual(self.kp.remove_keyword(" "), True, "Could not remove empty string")

        """

        """
    def test_remove_keyword_empty_extreme(self):
        self.kp.add_keyword('')
        self.assertEqual(self.kp.remove_keyword(''), False, "Could remove empty string")

    def test_remove_keyword_dict(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertEqual(self.kp.remove_keyword("1"), True, "Could not remove word")

        """

        """
    def test_remove_keyword_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(self.kp.remove_keyword("This"), True, "Could not remove word")

"""
Class Test_add_keyword_from_file which tests function add_keyword_from_fileself.
add_keyword_from_file() takes the path to keywords file which has keyword and clean name:
keyword=>clean_name format. Could also contain only a keyword.
"""
class Test_add_keyword_from_file(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """
        Test case basic. Adds a keyword with its clean name from a file.
        """
    def test_add_keyword_from_file_basic(self):
        self.kp.add_keyword_from_file('keyword_file.txt')
        self.assertTrue("keyword" in self.kp, "Could not add word from file")
        self.assertFalse("keyword" not in self.kp, "Could not add word from file")

        """
        Test case basic. Add only a keyword from a file.
        """
    def test_add_keyword_from_file_basic_extended(self):
        self.kp.add_keyword_from_file('keyword_file_basic.txt')
        self.assertTrue("keyword" in self.kp, "Could not add word from file")

        """
        Test case empty. Adds an empty file (having only space).
        """
    def test_add_keyword_from_file_empty(self):
        self.kp.add_keyword_from_file('empty_file.txt')
        self.assertTrue(" " in self.kp, "Could not add space from file")
        self.assertFalse(" " not in self.kp, "Could not add space from file")

"""
Class Test_remove_keywords_from_dict which tests function remove_keywords_from_dictself.
remove_keywords_from_dict() takes a dictionary with a 'str' key and a list as value.
Raises error if value for key is a list.
"""
class Test_remove_keywords_from_dict(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """
        Test case basic. First add one dictionary only containing one word (with value)
        and then remove it from the dictionary.
        """
    def test_remove_keywords_from_dict_basic(self):
        self.kp.add_keyword('red','colour')
        self.kp.remove_keywords_from_dict({'red':['colour']})
        self.assertFalse('colour' in self.kp, "Could not remove keyword from dictionary")
        self.assertTrue('colour' not in self.kp, "Could not remove keyword from dictionary")

        """
        Test case normal. Adding one dictionary and then remove one word from it.
        """
    def test_remove_keywords_from_dict_normal(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.kp.remove_keywords_from_dict({"This":["1"]})
        self.assertFalse("This" in self.kp, "Could not remove keyword from dictionary")
        self.assertTrue("This" not in self.kp, "Could not remove keyword from dictionary")

        """
        Test case empty. Remove an empty string. This should assert False since no word is
        removed.
        """
    def test_remove_keyword_dict_empty(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertFalse(self.kp.remove_keywords_from_dict({"":[""]}),"Could not remove empty string.")

        """
        Test case extreme. Removing a keyword but only giving one of the clean names.
        """
    def test_remove_keyword_dict_extreme(self):
        self.kp.add_keywords_from_dict({'A':['first','letter']})
        self.kp.remove_keywords_from_dict({'A':['first']})
        self.assertTrue('A' not in self.kp, "Could not remove keyword from dictionary")

        """
        Test case extreme. Removing two keywords from a dictionaryself.
        """
    def test_remove_keyword_dict_extreme_two(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.kp.remove_keywords_from_dict({'This':['1'],'is':['2']})
        self.assertTrue('This' not in self.kp, "Could not remove keyword from dictionary")
        self.assertTrue('is' not in self.kp, "Could not remove keyword from dictionary")


"""
Class Test_remove_keywords_from_list which tests function remove_keywords_from_list.
remove_keywords_from_list() takes a list and removes words from current list.
"""
class Test_remove_keywords_from_list(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """
        Test case basic. Has one keyword and removes it.
        """
    def test_remove_keyword_from_list_basic(self):
        self.kp.add_keyword('keyword')
        self.kp.remove_keywords_from_list(['keyword'])
        self.assertTrue('keyword' not in self.kp, "Could not remove keyword from list")

        """
        Test case normal. Adds a list and removes one of the words.
        """
    def test_remove_keyword_from_list_normal(self):
        self.kp.add_keywords_from_list(test_list)
        self.kp.remove_keywords_from_list(["This"])
        self.assertTrue("This" not in self.kp, "Could not remove keyword from list")
        self.assertFalse("This" in self.kp, "Could not remove keyword from list")

        """
        Test case normal extended. Removes two words from a list.
        """
    def test_remove_keyword_from_list_extended(self):
        self.kp.add_keywords_from_list(test_list)
        self.kp.remove_keywords_from_list(["This","is"])
        self.assertTrue("This" not in self.kp, "Could not remove keyword from list")
        self.assertFalse("This" in self.kp, "Could not remove keyword from list")
        self.assertTrue("is" not in self.kp, "Could not remove keyword from list")
        self.assertFalse("is" in self.kp, "Could not remove keyword from list")

        """
        Test case normal with dictionary. Removes a word from a dictionary with having
        the clean name as input.
        """
    def test_remove_keyword_list(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.kp.remove_keywords_from_list(['1'])
        self.assertTrue('This' not in self.kp, "Could not remove keyword from list")

        """
        Test case empty. Removes a empty word and does not affect the list.
        """
    def test_remove_keyword_from_list_empty(self):
        self.kp.add_keywords_from_list(test_list)
        self.kp.remove_keywords_from_list([''])
        self.assertTrue("This" in self.kp, "Could not remove empty list")

"""
CLass Test_extract_keywords which tests function extract_keywords. extract_keywords() searches in a
string for all keywords present. If keyword is detected it is added to a list which is returned.
"""
class Test_extract_keywords(unittest.TestCase):

    def setUp(self):
        print "run " + self._testMethodName
        self.kp = KeywordProcessor() #Creates object KeywordProcessor

    def tearDown(self):
        print "OK"

        """
        Test case basic. Checks if one keyword is found in the sentence.
        """
    def test_extract_keywords_basic(self):
        self.kp.add_keyword('cats')
        self.assertEqual(self.kp.extract_keywords('I love cats and dogs.'), ['cats'], "Could not extract keywords")

        """
        Test case basic with keyword and clean name. Returns the clean name if keyword is found in sentence.
        """
    def test_extract_keywords_basic_extended(self):
        self.kp.add_keyword('dogs','animal')
        self.assertEqual(self.kp.extract_keywords('I love cats and dogs.'), ['animal'], "Could not extract keywords")

        """
        Test case normal with dictionary. Checks if words are present from a dictionary. Will search for clean name and not keywordself.
        This case is in fact found odd, should it not be the other way around?
        """
    def test_extract_keywords_dict(self):
        self.kp.add_keywords_from_dict(test_dictionary)
        self.assertEqual(self.kp.extract_keywords('I have the numbers 1 2 4'), ['This','is','testing'], "Could not extract keywords from dictionary")
        """
        An extention of the test case, will not find keywords and therefore return nothing. 
        """
        self.assertEqual(self.kp.extract_keywords('This is testing on a dictionary'), [], "Could not extract keywords from dictionary")

        """
        Test case normal with list. Has a list and checks for multiple words.
        """
    def test_extract_keywords_list(self):
        self.kp.add_keywords_from_list(test_list)
        self.assertEqual(self.kp.extract_keywords('This could be for testing list'), ['This','for','testing'], "Could not extract from list")

        """
        Test case normal with file. Finds the keyword in file and returns its clean name.
        """
    def test_extract_keywords_file(self):
        self.kp.add_keyword_from_file('keyword_file.txt')
        self.assertEqual(self.kp.extract_keywords('This is a keyword'), ['file'], "Could not extract word from file")
        """
        Test case empty. Checks fo an empty string in the sentence. Returns nothing.
        """
    def test_extract_keywords_empty(self):
        self.kp.add_keyword('')
        self.assertEqual(self.kp.extract_keywords('Keyword'), [], "Could not extract keyword from empty list")

        """
        Test case empty but the oppisite as above. Has a word and checks for empty. Returns nothing.
        """
    def test_extract_keywords_empty_extended(self):
        self.kp.add_keyword('empty')
        self.assertEqual(self.kp.extract_keywords(''), [], "Could not extract empty list")


if __name__ =='__main__':
    unittest.main()
