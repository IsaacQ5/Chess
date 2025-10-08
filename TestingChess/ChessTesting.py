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
    
    def test_PawnintoPawn(self):
        movePeice(1,1,3,1)  # Move black pawn forward
        movePeice(6,1,4,1)  # Move white pawn forward
        movePeice(3,1,4,1)  # black should not move 
        movePeice(4,1,3,1)  # white should not move
        print("Board after test_PawnintoPawn:")
        for row in boardlayout:
            print(row)
        # Assert that the black pawn moved from (2,1) to (3,0) and captured the white pawn
        self.assertEqual(boardlayout[4][1], 'WP')
        self.assertEqual(boardlayout[3][1], 'BP')
        boardlayout[3][1] = '--'  # Reset the move for next test
        boardlayout[4][1] = '--'  # Reset the move for next test
    
    def test_BlackpawnTakesWhitepawn(self):
        movePeice(1,1,3,1)  # Move black pawn forward
        movePeice(6,0,4,0)  # Move white pawn forward
        movePeice(3,1,4,0)  # black should take white pawn 
        print("Board after test_BlackpawnTakesWhitepawn:")
        for row in boardlayout:
            print(row)
        # Assert that the black pawn moved from (2,1) to (3,0) and captured the white pawn
        self.assertEqual(boardlayout[3][1], '--')
        self.assertEqual(boardlayout[4][0], 'BP')
        boardlayout[3][0] = '--'  # Reset the move for next test
        boardlayout[4][0] = '--'  # Reset the move for next test
    
    def test_WhitepawnTakesBlackpawn(self):
        movePeice(6,1,4,1)  # Move white pawn forward
        movePeice(1,0,3,0)  # Move black pawn forward
        movePeice(4,1,3,0)  # white should take black pawn 
        print("Board after test_WhitepawnTakesBlackpawn:")
        for row in boardlayout:
            print(row)
        # Assert that the white pawn moved from (4,1) to (3,0) and captured the black pawn
        self.assertEqual(boardlayout[4][1], '--')
        self.assertEqual(boardlayout[3][0], 'WP')
        boardlayout[3][0] = '--'  # Reset the move for next test
        boardlayout[4][1] = '--'  # Reset the move for next test
        
    def test_invalidBlackPawnTakeBlackPawn(self):
        movePeice(1,1,3,1)  # Move black pawn forward
        movePeice(1,0,2,0)  # Move black pawn forward
        movePeice(2,0,3,1)  # black should not take black pawn 
        print("Board after test_invalidBlackPawnTakeBlackPawn:")
        for row in boardlayout:
            print(row)
        # Assert that the black pawn did not move from (2,0) to (3,1)
        self.assertEqual(boardlayout[2][0], 'BP')
        self.assertEqual(boardlayout[3][1], 'BP')
        boardlayout[3][1] = '--'  # Reset the move for next test
        boardlayout[2][0] = '--'  # Reset the move for next test
    
    def test_invalidWhitePawnTakeWhitePawn(self):
        movePeice(6,1,4,1)  # Move white pawn forward
        movePeice(6,0,5,0)  # Move white pawn forward
        movePeice(5,0,4,1)  # white should not take white pawn 
        print("Board after test_invalidWhitePawnTakeWhitePawn:")
        for row in boardlayout:
            print(row)
        # Assert that the white pawn did not move from (5,0) to (4,1)
        self.assertEqual(boardlayout[5][0], 'WP')
        self.assertEqual(boardlayout[4][1], 'WP')
        boardlayout[4][1] = '--'  # Reset the move for next test
        boardlayout[5][0] = '--'  # Reset the move for next test
    
    def test_BlackPawnEnPassant(self):
        movePeice(1,0,3,0)  # Move black pawn forward
        movePeice(6,1,4,1)  # Move white pawn forward
        movePeice(3,0,4,0)  # Move black pawn forward
        movePeice(4,0,5,1)  # black should take white pawn en passant
        print("Board after test_BlackPawnEnPassant:")
        for row in boardlayout:
            print(row)
        # Assert that the white pawn moved from (4,1) to (3,0) and captured the black pawn
        self.assertEqual(boardlayout[5][1], 'BP')
        self.assertEqual(boardlayout[4][1], '--')
        boardlayout[5][1] = '--'  # Reset the move for next test
        boardlayout[4][1] = '--'  # Reset the move for next test
    
    def test_WhitePawnEnPassant(self):
        movePeice(6,1,4,1)  # Move white pawn forward
        movePeice(1,0,3,0)  # Move black pawn forward
        movePeice(4,1,3,1)  # Move white pawn forward
        movePeice(3,1,2,0)  # white should take black pawn en passant
        print("Board after test_WhitePawnEnPassant:")
        for row in boardlayout:
            print(row)
        # Assert that the white pawn moved from (4,1) to (3,0) and captured the black pawn
        self.assertEqual(boardlayout[2][0], 'WP')
        self.assertEqual(boardlayout[3][0], '--')
        boardlayout[2][0] = '--'  # Reset the move for next test
        boardlayout[3][0] = '--'  # Reset the move for next test
    
    def test_invalidBlackPawnMoveTwo(self):
        movePeice(1,0,3,0) # black moves two
        movePeice(3,0,5,0)  # black should not move two
        print("Board after test_invalidBlackPawnMoveTwo:")
        for row in boardlayout:
            print(row)
        # Assert that the pawn did not move from (3,0) to (5,0)
        self.assertEqual(boardlayout[3][0], 'BP')
        self.assertEqual(boardlayout[5][0], '--')
        boardlayout[3][0] = '--'  # Reset the move for next test
        boardlayout[5][0] = '--'  # Reset the move for next test
    
    def test_invalidWhitePawnMoveTwo(self):
        movePeice(6,0,4,0) # white moves two
        movePeice(4,0,2,0)  # white should not move two
        print("Board after test_invalidWhitePawnMoveTwo:")
        for row in boardlayout:
            print(row)
        # Assert that the pawn did not move from (4,0) to (2,0)
        self.assertEqual(boardlayout[4][0], 'WP')
        self.assertEqual(boardlayout[2][0], '--')
        boardlayout[4][0] = '--'  # Reset the move for next test
        boardlayout[2][0] = '--'  # Reset the move for next test
    
    def test_invalidBlackPawnTake(self):
        movePeice(1,0,3,0) # black moves two
        movePeice(3,0,4,1)  # black should not take empty space
        print("Board after test_invalidBlackPawnTake:")
        for row in boardlayout:
            print(row)  
        # Assert that the pawn did not move from (3,0) to (4,1)
        self.assertEqual(boardlayout[3][0], 'BP')
        self.assertEqual(boardlayout[4][1], '--')   
        boardlayout[3][0] = '--'  # Reset the move for next test
        boardlayout[4][1] = '--'  # Reset the move for next test
    
    def test_invalidWhitePawnTake(self):
        movePeice(6,0,4,0) # white moves two
        movePeice(4,0,3,1)  # white should not take empty space
        print("Board after test_invalidWhitePawnTake:")
        for row in boardlayout:
            print(row)  
        # Assert that the pawn did not move from (4,0) to (3,1)
        self.assertEqual(boardlayout[4][0], 'WP')
        self.assertEqual(boardlayout[3][1], '--')   
        boardlayout[4][0] = '--'  # Reset the move for next test
        boardlayout[3][1] = '--'  # Reset the move for next test
        
    def test_invalidBlackPawnMoveBackwards(self):
        movePeice(1,0,3,0) # black moves two
        movePeice(3,0,2,0)  # black should not move backwards
        print("Board after test_invalidBlackPawnMoveBackwards:")
        for row in boardlayout:
            print(row)
        # Assert that the pawn did not move from (3,0) to (2,0)
        self.assertEqual(boardlayout[3][0], 'BP')
        self.assertEqual(boardlayout[2][0], '--')
        boardlayout[3][0] = '--'  # Reset the move for next test
        boardlayout[2][0] = '--'  # Reset the move for next test
    
    def test_invalidWhitePawnMoveBackwards(self):
        movePeice(6,0,4,0) # white moves two
        movePeice(4,0,5,0)  # white should not move backwards
        print("Board after test_invalidWhitePawnMoveBackwards:")
        for row in boardlayout:
            print(row)
        # Assert that the pawn did not move from (4,0) to (5,0)
        self.assertEqual(boardlayout[4][0], 'WP')
        self.assertEqual(boardlayout[5][0], '--')
        boardlayout[4][0] = '--'  # Reset the move for next test
        boardlayout[5][0] = '--'  # Reset the move for next test
    
    def test_WhiteRookMoves(self):
        movePeice(6,0,4,0) # white pawn moves two
        movePeice(7,0,5,0) # white rook move up
        movePeice(5,0,5,4) # white rook moves to the right 
        movePeice(5,4,5,3) # white rook moves back
        movePeice(5,3,3,3) # white rook moves up
        movePeice(3,3,5,3) # white rook moves back
        print("Board after test_WhiteRookMoves:")
        for row in boardlayout:
            print(row)
        # Assert that the rook moved from (7,0) to (5,0)
        self.assertEqual(boardlayout[5][3], 'WR')
        boardlayout[5][3] = '--'  # Reset the move for next test
        boardlayout[4][0] = '--'  # Reset the move for next test
    
    def test_BlackRookMoves(self):
        movePeice(1,0,3,0) # black pawn moves two
        movePeice(0,0,2,0) # black rook move up
        movePeice(2,0,2,4) # black rook moves to the right 
        movePeice(2,4,2,3) # black rook moves back
        movePeice(2,3,4,3) # black rook moves up
        movePeice(4,3,2,3) # black rook moves back
        print("Board after test_BlackRookMoves:")
        for row in boardlayout:
            print(row)
        # Assert that the rook moved from (0,0) to (2,0)
        self.assertEqual(boardlayout[2][3], 'BR')
        boardlayout[2][3] = '--'  # Reset the move for next test
        boardlayout[3][0] = '--'  # Reset the move for next test

    def test_BlackRooktakingPeice(self):
        movePeice(1,0,3,0) # black pawn moves two
        movePeice(0,0,2,0) # black rook move up
        movePeice(2,0,2,4) # black rook moves to the right
        movePeice(2,4,6,4) # black rook takes white pawn
        print("Board after test_BlackRooktakingPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the rook moved from (0,0) to (3,0) taking the pawn
        self.assertEqual(boardlayout[6][4], 'BR')
        boardlayout[3][0] = '--'  # Reset the move for next test
        boardlayout[6][4] = '--'  # Reset the move for next test
    
    def test_WhiteRooktakingPeice(self):
        movePeice(6,0,4,0) # white pawn moves two
        movePeice(7,0,5,0) # white rook move up
        movePeice(5,0,5,4) # white rook moves to the right 
        movePeice(5,4,1,4) # white rook takes black pawn
        print("Board after test_WhiteRooktakingPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the rook moved from (7,0) to (3,0) taking the pawn
        self.assertEqual(boardlayout[1][4], 'WR')
        boardlayout[4][0] = '--'  # Reset the move for next test
        boardlayout[1][4] = '--'  # Reset the move for next test
    
    def test_invalidWhiteRookTakePeiceVertical(self):
        movePeice(7,0,6,0) # white rook doesnt take white pawn
        movePeice(7,0,5,0) # white rook doesnt move up 
        print("Board after test_invalidWhiteRookTakePeiceVertical:")
        for row in boardlayout:
            print(row)
        # Assert that the rook did not move from (7,0) to (6,0) or (5,0)
        self.assertEqual(boardlayout[7][0], 'WR')

    def test_invalidBlackRookTakePeiceVertical(self):
        movePeice(0,0,1,0) # black rook doesnt take black pawn
        movePeice(0,0,2,0) # black rook doesnt move up 
        print("Board after test_invalidBlackRookTakePeiceVertical:")
        for row in boardlayout:
            print(row)
        # Assert that the rook did not move from (0,0) to (1,0) or (2,0)
        self.assertEqual(boardlayout[0][0], 'BR')
    
    def test_invalidWhiteRookTakePeiceHorizontal(self):
        movePeice(7,0,7,1) # white rook doesnt take white knight
        movePeice(7,0,7,2) # white rook doesnt move right (checking off by 1 error)
        print("Board after test_invalidWhiteRookTakePeiceHorizontal:")
        for row in boardlayout:
            print(row)
        # Assert that the rook did not move from (7,0) to (7,1) or (7,2)
        self.assertEqual(boardlayout[7][0], 'WR')
    
    def test_invalidBlackRookTakePeiceHorizontal(self):
        movePeice(0,0,0,1) # black rook doesnt take black knight
        movePeice(0,0,0,2) # black rook doesnt move right (checking off by 1 error)
        print("Board after test_invalidBlackRookTakePeiceHorizontal:")
        for row in boardlayout:
            print(row)
        # Assert that the rook did not move from (0,0) to (0,1) or (0,2)
        self.assertEqual(boardlayout[0][0], 'BR')
    
    def test_invalidWhiteRookMoveDiagonally(self):
        movePeice(7,0,6,1) # white rook doesnt move diagonally
        movePeice(7,0,5,2) # white rook doesnt move diagonally (checking off by 1 error)
        print("Board after test_invalidWhiteRookMoveDiagonally:")
        for row in boardlayout:
            print(row)
        # Assert that the rook did not move from (7,0) to (6,1) or (5,2)
        self.assertEqual(boardlayout[7][0], 'WR')
    
    def test_invalidBlackRookMoveDiagonally(self):
        movePeice(0,0,1,1) # black rook doesnt move diagonally
        movePeice(0,0,2,2) # black rook doesnt move diagonally (checking off by 1 error)
        print("Board after test_invalidBlackRookMoveDiagonally:")
        for row in boardlayout:
            print(row)
        # Assert that the rook did not move from (0,0) to (1,1) or (2,2)
        self.assertEqual(boardlayout[0][0], 'BR')
        
    def test_WhiteBishopMoves(self):
        movePeice(6,1,5,1) # white pawn moves one
        movePeice(7,2,6,1) # white bishop move diagonally left up
        movePeice(6,1,4,3) # white bishop moves diagonally right up
        movePeice(4,3,5,4) # white bishop moves diagonally right down
        print("Board after test_WhiteBishopMoves:")
        for row in boardlayout:
            print(row)
        # Assert that the bishop moved from (7,2) to (3,2)
        self.assertEqual(boardlayout[5][4], 'WB')
        boardlayout[5][1] = '--'  # Reset the move for next test
        boardlayout[5][4] = '--'  # Reset the move for next test
    
    def test_BlackBishopMoves(self):
        movePeice(1,1,2,1) # black pawn moves one
        movePeice(0,2,1,1) # black bishop move diagonally left down
        movePeice(1,1,3,3) # black bishop moves diagonally right down
        movePeice(3,3,2,4) # black bishop moves diagonally right up
        print("Board after test_BlackBishopMoves:")
        for row in boardlayout:
            print(row)
        # Assert that the bishop moved from (0,2) to (2,4)
        self.assertEqual(boardlayout[2][4], 'BB')
        boardlayout[2][4] = '--'  # Reset the move for next test
        boardlayout[2][1] = '--'  # Reset the move for next test
    
    def test_WhiteBishopTakingPeice(self):
        movePeice(6,1,5,1) # white pawn moves one
        movePeice(7,2,6,1) # white bishop move diagonally left up
        movePeice(6,1,4,3) # white bishop moves diagonally right up
        movePeice(4,3,1,0) # white bishop takes black pawn
        print("Board after test_WhiteBishopTakingPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the bishop moved from (7,2) to (1,0) taking the pawn
        self.assertEqual(boardlayout[1][0], 'WB')
        boardlayout[5][1] = '--'  # Reset the move for next test
        boardlayout[1][0] = '--'  # Reset the move for next test
    
    def test_BlackBishopTakingPeice(self):
        movePeice(1,1,2,1) # black pawn moves one
        movePeice(0,2,1,1) # black bishop move diagonally left down
        movePeice(1,1,3,3) # black bishop moves diagonally right down
        movePeice(3,3,6,4) # black bishop takes white pawn
        print("Board after test_BlackBishopTakingPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the bishop moved from (0,2) to (6,4) taking the pawn
        self.assertEqual(boardlayout[6][4], 'BB')
        boardlayout[2][1] = '--'  # Reset the move for next test
        boardlayout[6][4] = '--'  # Reset the move for next test
    
    def test_invalidWhiteBishopHopsPeice(self):
        movePeice(7,2,6,1) # white bishop doesnt move
        movePeice(7,2,5,0) # white bishop doesnt move 
        print("Board after test_invalidWhiteBishopHopsPeice:")
        for row in boardlayout:
            print(row)  
        # Assert that the bishop did not move from (7,2) to (6,1) or (5,0)
        self.assertEqual(boardlayout[7][2], 'WB')
        
    def test_invalidBlackBishopHopsPeice(self):
        movePeice(0,2,1,1) # black bishop doesnt move
        movePeice(0,2,2,0) # black bishop doesnt move 
        print("Board after test_invalidBlackBishopHopsPeice:")
        for row in boardlayout:
            print(row)  
        # Assert that the bishop did not move from (0,2) to (1,1) or (2,0)
        self.assertEqual(boardlayout[0][2], 'BB')
        
    def test_BlackBishopTakingPeice(self):
        movePeice(1,1,2,1) # black pawn moves one
        movePeice(0,2,1,1) # black bishop move diagonally left down
        movePeice(1,1,6,6) # black bishop moves diagonally right down
        print("Board after test_BlackBishopTakingPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the bishop moved from (0,2) to (6,4) taking the pawn
        self.assertEqual(boardlayout[6][6], 'BB')
        boardlayout[2][1] = '--'  # Reset the move for next test
        boardlayout[6][6] = '--'  # Reset the move for next test
    
    def test_WhiteBishopTakingPeice(self):
        movePeice(6,1,5,1) # white pawn moves one
        movePeice(7,2,6,1) # white bishop move diagonally left up
        movePeice(6,1,1,6) # white bishop moves diagonally right up
        print("Board after test_WhiteBishopTakingPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the bishop moved from (7,2) to (1,0) taking the pawn
        self.assertEqual(boardlayout[1][6], 'WB')
        boardlayout[5][1] = '--'  # Reset the move for next test
        boardlayout[1][6] = '--'  # Reset the move for next test

    def test_invalidWhiteBishopMoves(self):
        movePeice(6,1,6,2) # white pawn moves 
        movePeice(7,2,6,1) # white bishop doesnt move
        movePeice(6,1,6,2) # white bishop doesnt move
        movePeice(6,1,5,0) # white bishop doesnt move
        print("Board after test_invalidWhiteBishopMoves:")
        for row in boardlayout:
            print(row)
        # Assert that the bishop did not move from (7,2) to (6,1), (6,2) or (5,0)
        self.assertEqual(boardlayout[7][2], 'WB')
        boardlayout[6][1] = '--'  # Reset the move for next test
        boardlayout[6][2] = '--'  # Reset the move for next test
    
    def test_KnightMoves(self):
        movePeice(7,1,5,2) # white knight moves
        movePeice(5,2,4,0) # white knight moves
        movePeice(4,0,2,1) # white knight moves
        movePeice(2,1,4,2) # white knight moves
        movePeice(0,1,2,2) # black knight moves
        movePeice(2,2,4,1) # black knight moves
        print("Board after test_KnightMoves:")
        for row in boardlayout:
            print(row)
        # Assert that the knight moved from (7,1) to (7,7)
        self.assertEqual(boardlayout[4][2], 'WK')
        self.assertEqual(boardlayout[4][1], 'BK')
        boardlayout[4][1] = '--'  # Reset the move for next test
        boardlayout[4][2] = '--'  # Reset the move for next test
        boardlayout[7][1] = 'WK'  # Reset the move for next test
        boardlayout[0][1] = 'BK'  # Reset the move for next test

    def test_KnightTakingPeice(self):
        movePeice(7,1,5,2) # white knight moves
        movePeice(5,2,4,0) # white knight moves
        movePeice(4,0,2,1) # white knight moves
        movePeice(2,1,1,3) # white knight takes black pawn
        movePeice(0,1,1,3) # black knight moves takes white Knight
        print("Board after test_KnightTakingPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the knight moved from (7,1) to (3,3) taking the pawn and (0,1) to (6,4) taking the pawn
        self.assertEqual(boardlayout[1][3], 'BK')
        self.assertEqual(boardlayout[7][1], '--')
        boardlayout[1][3] = 'BP'  # Reset the move for next test
        boardlayout[7][1] = 'WK'  # Reset the move for next test
        boardlayout[0][1] = 'BK'  # Reset the move for next test

    def test_invalidKnightMovesTakesPeice(self):
        movePeice(7,1,6,3) # white knight doesnt move
        movePeice(0,1,1,3) # black knight doesnt move
        print("Board after test_invalidKnightMovesTakesPeice:")
        for row in boardlayout:
            print(row)
        # Assert that the knight doesnt move
        self.assertEqual(boardlayout[7][1], 'WK')
        self.assertEqual(boardlayout[0][1], 'BK')
if __name__ == "__main__":
    unittest.main()