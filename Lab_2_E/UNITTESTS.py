import os
import unittest
import main
from unittest.mock import patch
import LocoParts


class TestLocoPartsEngine(unittest.TestCase):
    def test_positive(self):
        engine = LocoParts.Engine(10000, 100, 100)
        expected_output = "10000W engine that consumes 100L/h and weighs 100Kg"
        self.assertEqual(str(engine), expected_output)

    @patch('sys.stderr.write')
    def test_power_invalid_input_type(self,mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Engine(10000.0, 100, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: power must be int")

    @patch('sys.stderr.write')
    def test_power_invalid_input_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Engine(0, 100, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: power must be positive")

    @patch('sys.stderr.write')
    def test_fuel_consumption_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Engine(10000, 100.0, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: fuel_consumption must be int")

    @patch('sys.stderr.write')
    def test_fuel_consumption_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Engine(10000, 0, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: fuel_consumption must be positive")

    @patch('sys.stderr.write')
    def test_mass_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Engine(10000, 100, 100.0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be int")

    @patch('sys.stderr.write')
    def test_mass_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Engine(10000, 100, 0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be positive")
