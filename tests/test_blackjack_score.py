from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  # Act
  score = blackjack_score(hand)
  # Assert <-- Write assert statement here
  assert score == 7

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  # Arrange
  hand = ['King', 'Queen']
  # Act
  score = blackjack_score(hand)
  # Assert
  assert score == 20  # King = 10, Queen = 10

# # @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  # Arrange
  hand = ['Ace', 5, 3]  # Ace should be counted as 11
  # Act
  score = blackjack_score(hand)
  # Assert
  assert score == 19  # 11 (Ace) + 5 + 3 = 19


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
    # Arrange
    hand = ['Ace', 10, 5]  # Ace should be counted as 1 to avoid busting
    # Act
    score = blackjack_score(hand)
    # Assert
    assert score == 16  # 1 (Ace) + 10 + 5 = 16

# # @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
    # Arrange
    hand = [3, 4, 'Cat']  # "Cat" is not a valid card
    # Act
    score = blackjack_score(hand)
    # Assert
    assert score == "Invalid card"  # We expect the function to return "Invalid card" for invalid cards


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
    # Arrange
    hand = [2, 3, 4, 5, 6, 'King']  # More than 5 cards
    # Act
    score = blackjack_score(hand)
    # Assert
    assert score == "Invalid hand size"  # We expect an "Invalid hand size" message

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
    # Arrange
    hand = [10, 'King', 5]  # 10 + 10 + 5 = 25 (Over 21)
    # Act
    score = blackjack_score(hand)
    # Assert
    assert score == "Bust"  # The function should return "Bust"

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
    # Arrange
    hand = ['Ace', 'Ace', 'King']  # 11 + 11 + 10 = 22 adjust one Ace to 1, so 12
    # Act
    score = blackjack_score(hand)
    # Assert
    assert score == 12  # The function should return 12

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    # Arrange
    hand = ['Ace', 'Ace', 'Ace', 'Ace']  # 11 + 11 + 11 + 11 = 44, adjust three Aces to 1 each, total = 14
    # Act
    score = blackjack_score(hand)
    # Assert
    assert score == 14  # The function should return 14