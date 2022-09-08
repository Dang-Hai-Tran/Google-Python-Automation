#!/usr/bin/env python3

import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Hayes", "Delgado"]
        expected = "nonummy@abc.edu"
        self.assertEqual(find_email(testcase), expected)
    
    def test_one_name(self):
        testcase = [None, "Petra"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)

    def test_two_name(self):
        testcase = [None, "Dang", "Hai"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)

if __name__ == "__main__":
    unittest.main()
