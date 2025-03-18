#!/usr/bin/env python3
# tests/test_blackjack.py

"""unit test code"""

import pytest
import sys
from dev.practise_scripts.test_code_for_blackjack import card_score

# # define individual test functions
# def test_simple_usecase():
#     card_score("JK") == 20

# def test_jkq():
#     assert card_score("JKQ") == 0

# def test_ka():
#     assert card_score("KA") == 21

# def test_double_ace():
#     assert card_score("AA") == 12

# parametrize the test function
@pytest.mark.parametrize("cards,score", [("JK",20), ("JKQ",0), ("KA",21), ("AA",12)])
def test_card_score(cards, score):
    """Test card_score function with different inputs."""
    assert card_score(cards) == score

def test_raise_value_error():
    """Test card_score function raises ValueError for invalid input."""
    with pytest.raises(ValueError):
        card_score("")

if __name__ == "__main__":
    # This offers more flexibility than pytest.main(["-v"])
    import subprocess
    try:
        # Try running pytest as a subprocess
        result = subprocess.run([sys.executable, "-m", "pytest", __file__, "-v"], check=True)
    except subprocess.CalledProcessError:
        print("Error running pytest. Try running it directly with:")
        print("python -m pytest tests/test_blackjack.py -v")
        sys.exit(1)
