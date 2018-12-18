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
 __      __  __          __               ____                       ______                __
/\ \  __/\ \/\ \      __/\ \__           /\  _`\                    /\__  _\              /\ \__
\ \ \/\ \ \ \ \ \___ /\_\ \ ,_\    __    \ \ \L\ \    ___   __  _   \/_/\ \/    __    ____\ \ ,_\   ____
 \ \ \ \ \ \ \ \  _ `\/\ \ \ \/  /'__`\   \ \  _ <'  / __`\/\ \/'\     \ \ \  /'__`\ /',__\\ \ \/  /',__\
  \ \ \_/ \_\ \ \ \ \ \ \ \ \ \_/\  __/    \ \ \L\ \/\ \L\ \/>  </      \ \ \/\  __//\__, `\\ \ \_/\__, `\
   \ `\___x___/\ \_\ \_\ \_\ \__\ \____\    \ \____/\ \____//\_/\_\      \ \_\ \____\/\____/ \ \__\/\____/
    '\/__//__/  \/_/\/_/\/_/\/__/\/____/     \/___/  \/___/ \//\/_/       \/_/\/____/\/___/   \/__/\/___/
"""# =================================================================== #


"""
Path 0: [0, 1, 2, 3, 5, 6, 4, 8, 9, 11, 12, 10, 13, 14]
Path 1: [0, 1, 2, 3, 5, 7, 14]
Path 2: [4, 5, 6, 4]
Path 3: [5, 6, 4, 5]
Path 4: [6, 4, 5, 6]
Path 5: [6, 4, 5, 7, 14]
Path 6: [10, 11, 12, 10]
Path 7: [11, 12, 10, 11]
Path 8: [12, 10, 11, 12]
"""


class test_whitebox_delitem(unittest.TestCase):

    def test_path_0(self):
        """
        Test the coverage of Path 0 (specified above). This path goes straight through the functions in the program
        without ever looping more than once in a loop.

        Execution Path:
            0, 1, 2, 3, 5, 6, 4, 8, 9, 11, 12, 10, 13, 14

        Keyword Constraint:
            - Length of keyword matching the keyword to delete must be EXACTLY one letter.
            - Another keyword must be added after that keyword so that the internal Dict is correct.

        Delete Constraint:
            - Length of word must be EXACTLY one letter and must match the first keyword.
        """
        kp = KeywordProcessor(case_sensitive=False)
        kp.add_keywords_from_dict({"P": ["Q"], "T": ["S"]})
        self.assertTrue(kp.__delitem__("Q"), "Keyword was found")
        self.assertFalse("Q" in kp, "Keyword must have been removed")

    def test_path_1(self):
        """
        Test the coverage of Path 1. This path should test the case where there is ONE letter in the word that is being
        deleted but there is no matching keyword in the processor.

        Execution Path:
            0, 1, 2, 3, 5, 7, 14

        Keyword Constraint:
            - There must be no keyword that is matching the word that is being deleted

        Delete Constraint:
            - The word to delete must be EXACTLY one letter long and cannot match on of the keywords in the processor.
        """
        kp = KeywordProcessor(case_sensitive=False)
        kp.add_keyword("P")
        self.assertFalse(kp.__delitem__("Q"), "Keyword could not have been removed")
        self.assertFalse("Q" in kp, "Keyword must still not be in list")

    def test_path_2_3_4(self):
        """
        Test the coverage of Paths 2, 3 and 4. This path should test the first for-loop where each statements is reached
        at least twice (4 back to 4, 5 back to 5 and 6 back to 6). These paths can all be combined by looping at least
        two times.

        Execution Path:
            0, 1, 2, 3, 5, 6, 4, 5, 6, 4, 5, 6, 4, 8, 9, 11, 12, 10, 11, 12, 10, 11, 12, 10, 13, 14

        Keyword Constraint:
            - There must be 1-2 keywords that each contains the first two letters of the word to be deleted.

        Delete Constraint:
            - The word to be delete must either exist in the processor or there must be keywords that cover the first
            two letters of the word.
        """
        kp = KeywordProcessor(case_sensitive=False)
        kp.add_keyword("Win")
        self.assertTrue(kp.__delitem__("Windows"), "The keyword must have been found")
        self.assertFalse("Win" in kp, "Keyword must have been delete")
     
    def test_path_5(self):
        """
        Test the coverage of Paths 5. This path should test exactly one iteration of the first loop followed by breaking
        out of the function.

        Execution Path:
            0, 1, 2, 3, 5, 6, 4, 5, 7, 14

        Keyword Constraint:
            - There must be a keyword of at least size 2, or multiple keywords of combined size 2.
            - The keywords must contains exactly the first character of the word to be deleted

        Delete Constraint:
            - The word to delete must have exactly 2 characters.
            - The word must start with the same character as is contained in one of the keywords.
        """
        kp = KeywordProcessor(case_sensitive=False)
        kp.add_keyword("WI")
        self.assertTrue("WA" not in kp, "Word not a keyword")
        self.assertFalse(kp.__delitem__("WA"), "Keyword could not be deleted")
        self.assertTrue("WA" not in kp, "Word still not a keyword")

    def test_path_6_7_8(self):
        """
        Test the coverage of Paths 6, 7 and 8. This path should test the second for-loop where each statements is
        reached at least twice (10 back to 10, 11 back to 11 and 12 back to 12). These paths can all be combined by
        looping at least two times.

        Execution Path:
            0, 1, 2, 3, 5, 6, 4, 5, 6, 4, 5, 6, 4, 8, 9, 11, 12, 10, 11, 12, 10, 11, 12, 10, 13, 14

        Keyword Constraint:
            - There must be a keyword matching the word to delete.
            - There must be at least 2 letters in the keyword

        Delete Constraint:
            - The word to delete must match one of the added keywords
        """
        kp = KeywordProcessor(case_sensitive=False)
        kp.add_keyword("Win")
        self.assertTrue(kp.__delitem__("Windows"), "The keyword must have been found")
        self.assertFalse("Win" in kp, "Keyword must have been delete")
            



# =================================================================== #

if __name__=="__main__":
    unittest.main(verbosity=2)
