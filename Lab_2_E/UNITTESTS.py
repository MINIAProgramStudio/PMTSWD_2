import unittest
import main
from unittest.mock import patch
import LocoParts
from Locomotive import Locomotive


class TestLocoPartsEngine(unittest.TestCase):
    def test_positive(self):
        engine = LocoParts.Engine(10000, 100, 100)
        expected_output = "10000W engine that consumes 100L/h and weighs 100Kg"
        self.assertEqual(str(engine), expected_output)

    @patch('sys.stderr.write')
    def test_power_invalid_input_type(self, mock_err):
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


class TestLocoPartsTransmission(unittest.TestCase):
    def test_positive(self):
        transmission = LocoParts.Transmission(1000.0, 100)
        expected_output = "transmission with a 1000.0N resistance and that weighs 100Kg"
        self.assertEqual(str(transmission), expected_output)

    @patch('sys.stderr.write')
    def test_mass_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Transmission(1000.0, 100.0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be int")

    @patch('sys.stderr.write')
    def test_mass_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Transmission(1000.0, 0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be positive")

    @patch('sys.stderr.write')
    def test_resistance_force_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Transmission(10, 1000)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: resistance_force must be float")

    @patch('sys.stderr.write')
    def test_resistance_force_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Transmission(-1.0, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: resistance_force must be positive or zero")


class TestLocoPartsWheels(unittest.TestCase):
    def test_positive(self):
        wheels = LocoParts.Wheels(4, 1000, 1000)
        expected_output = "wheels are located on 4 axels, have 1000mm radius and weigh 1000Kg"
        self.assertEqual(str(wheels), expected_output)

    @patch('sys.stderr.write')
    def test_mass_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Wheels(4, 100, 1.0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be int")

    @patch('sys.stderr.write')
    def test_mass_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Wheels(4, 100, 0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be positive")

    @patch('sys.stderr.write')
    def test_axels_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Wheels(4.0, 100, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: axels_count must be int")

    @patch('sys.stderr.write')
    def test_axels_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Wheels(1, 100, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: axels_count must be greater or equal to 2")

    @patch('sys.stderr.write')
    def test_radius_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Wheels(4, 10.0, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: radius must be int")

    @patch('sys.stderr.write')
    def test_radius_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Wheels(4, 0, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: radius must be positive")


class TestLocoPartsCab(unittest.TestCase):
    def test_positive(self):
        cab = LocoParts.Cab("black", 1000)
        expected_output = "cab is painted in black and weighs 1000Kg"
        self.assertEqual(str(cab), expected_output)

    @patch('sys.stderr.write')
    def test_mass_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Cab("black", 100.0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be int")

    @patch('sys.stderr.write')
    def test_mass_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Cab("black", 0)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: mass must be positive")

    @patch('sys.stderr.write')
    def test_colour_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Cab(10, 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: color must be str")

    @patch('sys.stderr.write')
    def test_colour_invalid_value(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            LocoParts.Cab("red, +10 to the agility", 100)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: car may be painted in any color if the color is black (c) H. Ford")


class TestLocomotive(unittest.TestCase):
    def test_init_positive(self):
        loco = Locomotive("УЗ", "Гр-336")
        self.assertEqual(loco.owner, "УЗ")
        self.assertEqual(loco.name, "Гр-336")

    @patch('sys.stderr.write')
    def test_init_owner_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            Locomotive(10, "Гр-336")
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: owner must be str")

    @patch('sys.stderr.write')
    def test_init_name_invalid_type(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            Locomotive("УЗ", 336)
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: name must be str")

    locomotive = Locomotive("УЗ", "М62")

    def test_set_engine_positive(self):
        engine = LocoParts.Engine(100, 100, 100)
        self.locomotive.set_engine(engine)
        self.assertEqual(self.locomotive.engine, engine)

    @patch('sys.stderr.write')
    def test_set_engine_negative(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            self.locomotive.set_engine("that's not an engine")
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: engine must be Engine")

    def test_set_transmission_positive(self):
        transmission = LocoParts.Transmission(10.0, 100)
        self.locomotive.set_transmission(transmission)
        self.assertEqual(self.locomotive.transmission, transmission)

    @patch('sys.stderr.write')
    def test_set_transmission_negative(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            self.locomotive.set_transmission("still not an engine")
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: transmission must be Transmission")

    def test_set_wheels_positive(self):
        wheels = LocoParts.Wheels(6, 1000, 1000)
        self.locomotive.set_wheels(wheels)
        self.assertEqual(self.locomotive.wheels, wheels)

    @patch('sys.stderr.write')
    def test_set_wheels_negative(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            self.locomotive.set_wheels("definately not an engine")
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: wheels must be Wheels")

    def test_set_cab_positive(self):
        cab = LocoParts.Cab("black", 1000)
        self.locomotive.set_cab(cab)
        self.assertEqual(self.locomotive.cab, cab)

    @patch('sys.stderr.write')
    def test_set_cab_negative(self, mock_err):
        with self.assertRaises(SystemExit) as cm:
            self.locomotive.set_cab("WILL YOU GIVE ME THE ENGINE?!")
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR: cab must be Cab")
