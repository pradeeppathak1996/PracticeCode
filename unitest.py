# -- app.py --

def add(a, b):
    return a + b

# ----------- test_user.py ------------ manddatory to strat the file class and function name by "test"

import unittest
from app import add

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()

# --- Github action yml file ---

# - name: Run Unit Tests
#   run: |
#     python -m unittest discover       # -- command
