import random

RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITS = ['♥','♦','♠','♣']

def build_deck():
    deck = [(r, s) for s in SUITS for r in RANKS]
    random.shuffle(deck)
    return deck

def hand_value(hand):
    value, aces = 0, 0
    for rank, _ in hand:
        if rank in ('J', 'Q', 'K'):
            value += 10
        elif rank == 'A':
            value += 11
            aces += 1
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def player_turn(hand, deck):
    while True:
        move = input('(H)it or (S)tand? ').upper()
        if move == 'H':
            hand.append(deck.pop())
            print('You drew', hand[-1])
            if hand_value(hand) > 21:
                print('Bust! You lose.')
                return hand
        else:
            return hand

def dealer_turn(hand, deck):
    while hand_value(hand) < 17:
        hand.append(deck.pop())
    return hand

def decide_winner(player, dealer):
    p, d = hand_value(player), hand_value(dealer)
    if p > 21:
        return 'Dealer wins'
    if d > 21 or p > d:
        return 'Player wins'
    if p == d:
        return 'Push'
    return 'Dealer wins'

def main():
    deck = build_deck()
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    print('Your hand:', player, '=', hand_value(player))
    print('Dealer shows:', dealer[0])
    player = player_turn(player, deck)
    if hand_value(player) <= 21:
        dealer = dealer_turn(dealer, deck)
    print('Dealer hand:', dealer, '=', hand_value(dealer))
    print(decide_winner(player, dealer))

if __name__ == '__main__':
    main()
