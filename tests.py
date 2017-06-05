import unittest
from test import support

import worklogdb

class WorklogTests(unittest.TestCase):


    def test_date_search(self):
        with support.captured_stdin() as stdin, support.captured_stdout() as stdout:
            stdin.write("b\n")
            stdin.seek(0)
            worklogdb.search_menu()
            try:
                assert "Please enter a date" in stdout.getvalue()
            except EOFError:
                pass
            


if __name__ == '__main__':
    unittest.main()