import unittest

from .dummy_main import *

class TestInfection(unittest.TestCase):
    def test_infect_result(self):
        self.assertEqual(infect({'health': 80, 'protein': "A"}), True)
        self.assertEqual(infect({'health': 95, 'protein': "A"}), False)
        self.assertEqual(infect({'health': 95, 'protein': "B"}), False)
        self.assertEqual(infect({'health': 10, 'protein': "B"}), False)

        self.assertIsNone(infect({'health': 10}))
        self.assertIsNone(infect({'protein': "B"}))
        self.assertEqual(infect({'protein': "A"}), None)


if __name__ == "__main__":
    unittest.main()