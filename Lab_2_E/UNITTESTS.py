import os
import unittest
import main
from unittest.mock import patch
import LocoParts

class TestLocoPartsEngine(unittest.TestCase):
    def test_positive(self):
        engine = LocoParts.Engine(10000,100,100)
        expected_output = "10000W engine that consumes 100L/h and weighs 100Kg"
        self.assertEqual(str(engine), expected_output)
    def test_power_invalid_input_type(self):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Engine(10000.0, 100, 100)
        self.assertEqual(cm.exception.code,-1)
    