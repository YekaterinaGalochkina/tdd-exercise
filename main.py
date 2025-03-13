VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):

    score = 0
    ace = 0
    if len(hand) < 2 or len(hand) > 5:
        return 'Invalid hand size'

    for card in hand:
        if card not in VALID_CARDS:
            return 'Invalid card'
        if card in range(2, 11): 
            score += card
        elif card in ['King', 'Queen', 'Jack']:
            score += 10
        elif card == 'Ace':
            score += 11
            ace += 1

    while score > 21 and ace > 0:
        score -= 10
        ace -= 1

    if score > 21:
        return "Bust"
    
    return score

