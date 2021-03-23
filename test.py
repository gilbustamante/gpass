"""Tests for gpass.py"""
import unittest
import gpass as gp

class TestGpass(unittest.TestCase):
    """Test class for gpass"""

    def test_generate_pass_length(self):
        """Make sure result is the correct length"""
        result = gp.generate_pass(15)
        self.assertEqual(len(result), 15)

    def test_generate_pass_negative(self):
        """Make sure function returns None if length is < 0"""
        result = gp.generate_pass(-5)
        self.assertIsNone(result)

    def test_alphanumeric_pass_length(self):
        """Make sure result is the correct length"""
        result = gp.generate_alphanumeric_pass(15)
        self.assertEqual(len(result), 15)

    def test_alphanumeric_pass_negative(self):
        """Make sure function returns None if length is < 0"""
        result = gp.generate_alphanumeric_pass(-5)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
