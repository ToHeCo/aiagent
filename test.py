#packages
import unittest
from functions.get_files_info import get_files_info 

#Testing different scenarios
class test_get_files(unittest.TestCase):

    def test_dot(self):
        result = get_files_info("calculator", ".")
        self.assertRegex(result, r"- main.py: file_size=\d+ bytes, is_dir=False")
        self.assertRegex(result, r"- tests\.py: file_size=\d+ bytes, is_dir=False")
        self.assertRegex(result, r"- pkg: file_size=\d+ bytes, is_dir=True")


    def test_pkg(self):
        result = get_files_info("calculator", "pkg")
        self.assertRegex(result, r"- calculator\.py: file_size=\d+ bytes, is_dir=False")
        self.assertRegex(result, r"- render\.py: file_size=\d+ bytes, is_dir=False")
        self.assertRegex(result, r"- __pycache__: file_size=\d+ bytes, is_dir=True")


    def test_bin(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_dotdot(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')
    

if __name__ == "__main__":
    unittest.main()