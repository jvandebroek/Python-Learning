#ill do something a little less tedious and make a quick functional blackjack game
import random
def fresh_deck():  
    """generates a new deck of cards replacing all J,Q,K with 10 and A with 1"""
    deck = sorted(range(13)*4)
    for i in range(52):
        deck[i] += 1
    for i in range(12):
        deck[-(i+1)] = 10
    return deck  
def deal():
    """Deals two cards to start a hand, also removes those cards from the deck"""
    your_first_card = deck[random.randint(1, len(deck))]
    deck.remove(your_first_card)
    your_second_card = deck[random.randint(1, len(deck))]
    deck.remove(your_second_card)
    hand = [your_first_card, your_second_card]
    return hand
def hit():
    """generates another card randomly from the deck and removes it from deck"""
    new_card = deck[random.randint(1, len(deck))]
    deck.remove(new_card)
    return new_card
def value(x):
    """calculates and returns the value of a hand"""
    val = 0
    ace_count = 0;
    for i in range(len(x)):
        if x[i] == 1:
            ace_count += 1
            val += 11
        else:
            val += x[i]
    while val > 21 and ace_count != 0:
        val -= 10
        ace_count -= 1
    return val                        
            
    
def play_blackjack():
    """plays blackjack"""
    deck = fresh_deck()
    hand = deal()
    val = value(hand)
    dealer_val = 0 
    print "You have %d and %d making your hand value %d would you like another card? Y/N" % (hand[0], hand[1], val)
    while val < 21:
        choice = raw_input("> ")
        if choice == "Y" or choice == "y":
            new_card = hit()
            hand.append(new_card)
            val = value(hand)
            if val > 21:
                print "You drew a %d and now have %d so you bust and lose!" % (new_card, val)
            elif val == 21:
                print "You drew a %d, Black Jack! you win!" % new_card
            else:
                print "You drew a %d, you now have %d would you like another card? Y/N" % (new_card, val)
        elif choice == "N" or choice == "n": 
            dealer_hand = deal()
            dealer_val = value(dealer_hand)
            print "The dealer drew %d and %d for a value of %d" % (dealer_hand[0], dealer_hand[1], dealer_val)
            while dealer_val < 17:
                new_card = hit()
                dealer_hand.append(new_card)
                dealer_val = value(dealer_hand)
                print "the dealer drew another card %d and now has value %d" % (new_card, dealer_val)
            if dealer_val <= 21 and dealer_val > val:
                print "The dealer wins with %d to your %d" % (dealer_val, val)
                val = 99999999
            elif dealer_val < val:
                print "You win with %d to the dealers %d" % (val, dealer_val)
                val = 99999999
            else:
                print "the dealer busts, you win!"
                val = 9999999     
        else:
            print "please enter Y/N"
deck = fresh_deck()  
play_blackjack()
       
        

    
