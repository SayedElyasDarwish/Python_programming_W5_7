import unittest
import subprocess
import sys

class TestMainProgram(unittest.TestCase):
    def test_word_analysis(self):
        user_input = "sky\nis\nblue\n\n"
        result = subprocess.run(
            [sys.executable, "main.py"],
            input=user_input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode()

        self.assertIn("Program starting.", output)
        self.assertIn("- 3 Words", output)
        self.assertIn("- 9 Characters", output)
        self.assertIn("- 3.00 Average word length", output)
        self.assertIn("Program ending.", output)

if __name__ == "__main__":
    unittest.main()
