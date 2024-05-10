import os
import unittest
import main
from unittest.mock import patch
import LocoParts

class TestLocoParts(unittest.TestCase):
    def test_engine(self):
        engine = LocoParts.Engine(10000,100,100)
        expected_output = "10000W engine that consumes 100L/h and weighs 100Kg"
        self.assertEqual(engine, expected_output)

