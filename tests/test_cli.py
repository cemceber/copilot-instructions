import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC))

from python_app.cli import main


class CliTests(unittest.TestCase):
    def test_main_prints_ready_message(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue().strip(), "Python app is ready.")

    def test_version_flag_prints_version(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main(["--version"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue().strip(), "0.1.0")


if __name__ == "__main__":
    unittest.main()
