import subprocess
import unittest

class TestMatricesMultiplication(unittest.TestCase):
    
    def run_binary(self, input_data):
        process = subprocess.Popen(
            ['./Matrices_multiplication'], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_data)
        return stdout, stderr

    def extract_output(self, stdout):
        lines = stdout.splitlines()
        result_lines = [line for line in lines if all(char.isdigit() or char.isspace() or char == '-' for char in line)]
        return '\n'.join(result_lines) + '\n'

    def test_valid_matrices(self):
        input_data = "2 3\n3 2\n-1 10 3\n-7 4 4\n23 0\n19 -4\n2 21\n"
        expected_output = "173 23 \n-77 68 \n"
        stdout, stderr = self.run_binary(input_data)
        filtered_output = self.extract_output(stdout)
        self.assertEqual(filtered_output, expected_output)
        self.assertEqual(stderr, "")

    def test_invalid_matrix_size(self):
        input_data = "2 2\n3 2\n2 2\n2 2\n2 2 2\n2 2 2\n"
        expected_error = "Error: Matrices cannot be multiplied, size mismatch\n"
        stdout, stderr = self.run_binary(input_data)
        self.assertEqual(stderr, expected_error)
        self.assertEqual(stdout, "")

    def test_single_element_matrices(self):
        input_data = "1 1\n1 1\n5 \n6\n"
        expected_output = "30 \n"
        stdout, stderr = self.run_binary(input_data)
        filtered_output = self.extract_output(stdout)
        self.assertEqual(filtered_output, expected_output)
        self.assertEqual(stderr, "")

    def test_empty_matrices(self):
        input_data = "0 0\n\n0 0\n\n"
        expected_output = "\n"
        stdout, stderr = self.run_binary(input_data)
        filtered_output = self.extract_output(stdout)
        self.assertEqual(filtered_output, expected_output)
        self.assertEqual(stderr, "")

if __name__ == '__main__':
    unittest.main()