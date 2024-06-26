import os
import unittest
import main
from unittest.mock import patch
import io


class TestGA(unittest.TestCase):

    def test_no_flags_input(self):
        input_string = "this is a random gibberish"
        expected_top_path = main.DEFAULT_TOP_PATH
        self.assertEqual(main.get_args(input_string), [input_string, expected_top_path])

    def test_only_file_flag(self):
        input_string = "-f example.file;"
        expected_filename = "example.file"
        expected_top_path = main.DEFAULT_TOP_PATH
        self.assertEqual(main.get_args(input_string), [expected_filename, expected_top_path])

    def test_file_and_path_flags(self):
        input_string = "-f example.file; -p \\Users;"
        expected_filename = "example.file"
        expected_top_path = "\\Users"
        self.assertEqual(main.get_args(input_string), [expected_filename, expected_top_path])

    def test_file_and_wrong_path_flags(self):
        input_string = "-f example.file; -p le folder;"
        expected_filename = "example.file"
        expected_top_path = "le folder"
        self.assertEqual(main.get_args(input_string), [expected_filename, expected_top_path])

    def test_file_and_path_and_default_flags(self):
        input_string = "-f example.file; -p \\Users; -d C:\\;"
        expected_filename = "example.file"
        expected_top_path = "\\Users"
        expected_DTP = "C:\\"
        self.assertEqual(main.get_args(input_string), [expected_filename, expected_top_path])
        self.assertEqual(main.DEFAULT_TOP_PATH, expected_DTP)

    def test_fail_default_flags(self):
        input_string = "-f example.file; -p le folder; -d A:\\;"
        expected_filename = "example.file"
        expected_top_path = "le folder"
        expected_DTP = main.DEFAULT_TOP_PATH
        with self.assertRaises(SystemExit) as cm:
            main.get_args(input_string)
        self.assertEqual(cm.exception.code, -1)
        self.assertEqual(main.DEFAULT_TOP_PATH, expected_DTP)


class TestFF(unittest.TestCase):

    def test_only_filename(self):
        os.mkdir("/temppp")
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        file = open("/temppp/"+file_name, "w")
        file.close()
        self.assertEqual(main.find_file(file_name), ["\\temppp\\gibberishfiiiiiiilleeeeeeeee.file"])
        os.remove("/temppp/gibberishfiiiiiiilleeeeeeeee.file")
        os.rmdir("/temppp")

    def test_filename_and_path(self):
        os.mkdir("/temppp")
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        file = open("/temppp/" + file_name, "w")
        file.close()
        self.assertEqual(main.find_file(file_name, "\\temppp"), ["\\temppp\\gibberishfiiiiiiilleeeeeeeee.file"])
        os.remove("/temppp/gibberishfiiiiiiilleeeeeeeee.file")
        os.rmdir("/temppp")

    def test_for_no_such_file(self):
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        with self.assertRaises(SystemExit) as cm:
            main.find_file(file_name)
        self.assertEqual(cm.exception.code, -1)

class TestProcessing(unittest.TestCase):

    def test_zero(self):
        os.mkdir("/temppp")
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        file = open("/temppp/" + file_name, "w")
        file.close()
        self.assertEqual(main.processing([file_name, "\\temppp"]), 0)
        os.remove("/temppp/gibberishfiiiiiiilleeeeeeeee.file")
        os.rmdir("/temppp")

    def test_for_no_such_file(self):
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        with self.assertRaises(SystemExit) as cm:
            main.processing([file_name, main.DEFAULT_TOP_PATH])
        self.assertEqual(cm.exception.code, -1)

    def test_args_check(self):
        with self.assertRaises(SystemExit) as cm:
            main.processing("le_file.file")
        self.assertEqual(cm.exception.code, -1)

class TestLeMain(unittest.TestCase):
    def test_normal(self):
        os.mkdir("/temppp")
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        file = open("/temppp/" + file_name, "w")
        file.close()
        with self.assertRaises(SystemExit) as cm:
            main.le_main(file_name)
        self.assertEqual(cm.exception.code, 0)
        os.remove("/temppp/gibberishfiiiiiiilleeeeeeeee.file")
        os.rmdir("/temppp")

    def test_exit(self):
        with self.assertRaises(SystemExit) as cm:
            main.le_main("Exit")
        self.assertEqual(cm.exception.code, 0)

class TestMAIN(unittest.TestCase):

    @patch('sys.stderr.write')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['gibberishfiiiiiiilleeeeeeeee.file'])
    def test_raw_file_path(self,_,mock_out, mock_err):
        os.mkdir("/temppp")
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        file = open("/temppp/" + file_name, "w")
        file.close()

        expected = "C:\\temppp\\"+file_name
        with self.assertRaises(SystemExit) as cm:
            main.le_main()
        mock_out.assert_called_with(expected)
        self.assertEqual(cm.exception.code,0)
        os.remove("/temppp/gibberishfiiiiiiilleeeeeeeee.file")
        os.rmdir("/temppp")

    @patch('sys.stderr.write')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['-f gibberishfiiiiiiilleeeeeeeee.file;'])
    def test_file_flag(self,_,mock_out, mock_err):
        os.mkdir("/temppp")
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        file = open("/temppp/" + file_name, "w")
        file.close()

        expected = "C:\\temppp\\" + file_name
        with self.assertRaises(SystemExit) as cm:
            main.le_main()
        mock_out.assert_called_with(expected)
        self.assertEqual(cm.exception.code, 0)
        os.remove("/temppp/gibberishfiiiiiiilleeeeeeeee.file")
        os.rmdir("/temppp")

    @patch('sys.stderr.write')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['-f faultygibberishfiiiiiiilleeeeeeeee.file;'])
    def test_faulty_filename(self, _, mock_out, mock_err):
        with self.assertRaises(SystemExit) as cm:
            main.le_main()
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR_FF_1: No such file in the directory")

    @patch('sys.stderr.write')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['-f gibberishfiiiiiiilleeeeeeeee.file; -p \\temppp;'])
    def test_file_and_path_flag(self, _, mock_out, mock_err):
        os.mkdir("/temppp")
        file_name = "gibberishfiiiiiiilleeeeeeeee.file"
        file = open("/temppp/" + file_name, "w")
        file.close()

        expected = "\\temppp\\" + file_name
        with self.assertRaises(SystemExit) as cm:
            main.le_main()
        mock_out.assert_called_with(expected)
        self.assertEqual(cm.exception.code, 0)
        os.remove("/temppp/gibberishfiiiiiiilleeeeeeeee.file")
        os.rmdir("/temppp")

    @patch('sys.stderr.write')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['-f gibberishfiiiiiiilleeeeeeeee.file; -p \\tempppfaulty'])
    def test_file_and_faulty_path_flag(self, _, mock_out, mock_err):
        with self.assertRaises(SystemExit) as cm:
            main.le_main()
        self.assertEqual(cm.exception.code, -1)
        mock_err.assert_called_with("ERR_Processing_1: Arguments check failed")



if __name__ == '__main__':
    unittest.main()