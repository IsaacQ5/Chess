import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


# Ensure the project root is in sys.path for module imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from MainChess.main import peices, movePeice, boardlayout  

    
class TestChess(unittest.TestCase):
    def setUp(self):
        peices()
        
        # Initialize the board before each test
    # Each test method must start with 'test_'
    def test_movePawnTwo(self):
        movePeice(1,0,3,0)
        print("Board after test_movePawnTwo:")
        for row in boardlayout:
            print(row)
        # Assert that the pawn moved from (1,0) to (3,0)
        self.assertEqual(boardlayout[1][0], '--')
        self.assertEqual(boardlayout[3][0], 'BP')
        boardlayout[3][0] = '--'  # Reset the move for next test
    
    def test_movePawnOne(self):
        movePeice(1,1,2,1)
        print("Board after test_movePawnOne:")
        for row in boardlayout:
            print(row)
        # Assert that the pawn moved from (1,1) to (2,1)
        self.assertEqual(boardlayout[1][1], '--')
        self.assertEqual(boardlayout[2][1], 'BP')
        boardlayout[2][1] = '--'  # Reset the move for next test
        
if __name__ == "__main__":
    unittest.main()