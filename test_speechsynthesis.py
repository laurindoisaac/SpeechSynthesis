# test_speechsynthesis.py
"""
Tests for SpeechSynthesis module.
"""

import unittest
from speechsynthesis import SpeechSynthesis

class TestSpeechSynthesis(unittest.TestCase):
    """Test cases for SpeechSynthesis class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SpeechSynthesis()
        self.assertIsInstance(instance, SpeechSynthesis)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SpeechSynthesis()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
