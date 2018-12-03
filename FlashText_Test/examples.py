"""
These examples will be used in the latex document.
"""

from keywords import *


def find():
    flashtext = KeywordProcessor()
    flashtext.add_keyword("hello")
    found = flashtext.extract_keywords("hello world!")
    print found # "hello"


def replace():
    flashtext = KeywordProcessor()
    flashtext.add_keyword("hello", "hej")
    result = flashtext.replace_keywords("hello world!")
    print result # "hej world!"


def find_adv():
    flashtext = KeywordProcessor()
    flashtext.add_keyword("hello")
    found = flashtext.extract_keywords("hello world!", span_info=True)
    print found # ("hello", 0, 5)


find_adv()
