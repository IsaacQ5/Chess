import unittest
import os
import sys
from MainChess.main import movePeice

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

class TestChess(unittest.TestCase):
    def setup(self):
        print("THIS IS THE TEST")
        self.move=movePeice(1,0,3,0)
    # Each test method must start with 'test_'
    def test_movePawnTwo(self):
        self.assertTrue(self.move, True)
        
if __name__ == "__main__":
    print('ehre')
    unittest.main()