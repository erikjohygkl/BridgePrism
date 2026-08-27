# test_bridgeprism.py
"""
Tests for BridgePrism module.
"""

import unittest
from bridgeprism import BridgePrism

class TestBridgePrism(unittest.TestCase):
    """Test cases for BridgePrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BridgePrism()
        self.assertIsInstance(instance, BridgePrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BridgePrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
