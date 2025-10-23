"""
Unit tests for Rock Paper Scissors Game
Run with: python -m pytest test_rock_paper_scissors.py
or: python test_rock_paper_scissors.py
"""

import unittest
import sys
from io import StringIO

# Import functions from the Rock,Paper,Scissors.py file
# Note: The comma in the filename might cause import issues, so we handle it dynamically
import importlib.util
spec = importlib.util.spec_from_file_location("rps", "Rock,Paper,Scissors.py")
rps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rps)

class TestRockPaperScissors(unittest.TestCase):
    """Test cases for Rock Paper Scissors game functions."""
    
    def test_get_choice_name(self):
        """Test that choice numbers convert to correct names."""
        self.assertEqual(rps.get_choice_name(0), "Rock")
        self.assertEqual(rps.get_choice_name(1), "Paper")
        self.assertEqual(rps.get_choice_name(2), "Scissors")
        self.assertEqual(rps.get_choice_name(99), "Invalid")
    
    def test_determine_winner_tie(self):
        """Test tie scenarios."""
        self.assertEqual(rps.determine_winner(0, 0), "tie")  # Rock vs Rock
        self.assertEqual(rps.determine_winner(1, 1), "tie")  # Paper vs Paper
        self.assertEqual(rps.determine_winner(2, 2), "tie")  # Scissors vs Scissors
    
    def test_determine_winner_player_wins(self):
        """Test scenarios where player wins."""
        self.assertEqual(rps.determine_winner(0, 2), "win")  # Rock beats Scissors
        self.assertEqual(rps.determine_winner(1, 0), "win")  # Paper beats Rock
        self.assertEqual(rps.determine_winner(2, 1), "win")  # Scissors beats Paper
    
    def test_determine_winner_player_loses(self):
        """Test scenarios where player loses."""
        self.assertEqual(rps.determine_winner(0, 1), "lose")  # Rock loses to Paper
        self.assertEqual(rps.determine_winner(1, 2), "lose")  # Paper loses to Scissors
        self.assertEqual(rps.determine_winner(2, 0), "lose")  # Scissors loses to Rock
    
    def test_get_valid_choice_valid_input(self):
        """Test that valid input is accepted."""
        # Simulate user input
        for valid_choice in [0, 1, 2]:
            sys.stdin = StringIO(str(valid_choice))
            result = rps.get_valid_choice()
            self.assertIn(result, [0, 1, 2])
    
    def test_get_valid_choice_invalid_then_valid(self):
        """Test that invalid input is rejected and valid input is accepted."""
        # Simulate user entering invalid input first, then valid input
        sys.stdin = StringIO("5\n1\n")
        result = rps.get_valid_choice()
        self.assertEqual(result, 1)
    
    def test_play_round_returns_valid_result(self):
        """Test that play_round returns a valid result."""
        # Simulate user input
        sys.stdin = StringIO("0\n")
        result = rps.play_round()
        self.assertIn(result, ["win", "lose", "tie"])

def run_tests():
    """Run all tests and display results."""
    print("Running Rock Paper Scissors Tests...")
    print("=" * 50)
    
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestRockPaperScissors)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed.")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    # Reset stdin to default for test execution
    import sys
    sys.stdin = sys.__stdin__
    
    success = run_tests()
    sys.exit(0 if success else 1)

