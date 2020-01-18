#!/usr/bin/env python3

import unittest
from fibonacci import fibonacci, getSequence

class TestUserInputs(unittest.TestCase):
    def testCorrectArguments(self):
        arguments = [4, 20]
        fibonacci(arguments)

    # This is suposed to fail to showcase the unit test functionality
    def testIncorrectArguments(self):
        arguments = ["a", "b"]
        # This will return ValueError not RuntimeError
        with self.assertRaises(RuntimeError):
            fibonacci(arguments)

class TestSequence(unittest.TestCase):
    def testStartingValue(self):
        start, length = 4, 10
        result = getSequence(start, length)
        self.assertTrue(result[0] > start)

    def testLengthValue(self):
        start, length = 4, 10
        result = getSequence(start, length)
        self.assertEqual(length, len(result))

class TestOutput(unittest.TestCase):
    def testFileoutput(self):
        arguments = [0, 4]
        correctResult = "1,1,2,3"
        fibonacci(arguments)
        with open('fib_sequence.txt', "r") as file:
            content = file.read()
            file.close()
            self.assertEqual(correctResult, content)
