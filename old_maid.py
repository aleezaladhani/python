# Python variation of the card game: Old Maid

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)


def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     dealer=deck[1::2]
     other=deck[0::2]
    
     return (dealer, other)
 

def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    for x in range(len(l)):
      pairs=[]
      last=-1

      for y in range(len(l)):
        if (x != y) and (l[x][:-1] == l[y][:-1]):
          if pairs.count(x) == 0: pairs.append(x)
          if pairs.count(y) == 0: pairs.append(y)

      if len(pairs) > 0 and len(pairs) % 2 == 1:
        pairs.sort()
        last = pairs[len(pairs)-1]

      if len(pairs) == 0:
        no_pairs.append(l[x])
      elif (last == x):
        no_pairs.append( l[last] )

    
    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    
    string_deck = ' '.join(str(card) for card in deck)

    print("\n"+string_deck+"\n")

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     valid_input = int(input("Give me an integer between 1 and " + str(n) + ": "))

     while valid_input<1 or valid_input>n:
         valid_input = int(input("Invalid number. Please enter integer between 1 and " + str(n) + ": "))

     return valid_input


def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     while (len(dealer)>=0 and len(human)>=0):
         print("***********************************************************")

         print("Your turn.\n")
         print("Your current deck of cards is:")
         print_deck(human)
         
         print("I have", str(len(dealer)), "cards. If 1 stands for my frst card and")
         print(str(len(dealer)), "for my last card, which of my cards would you like?")

         other_wanted_card = get_valid_input(len(dealer))

         if other_wanted_card == 1:
             super_script = "st"
         elif other_wanted_card == 2:
             super_script = "nd"
         elif other_wanted_card == 3:
             super_script = "rd"
         else:
             super_script = "th"

         print("You asked for my", str(other_wanted_card)+super_script, "card.")
         print("Here it is. It is", dealer[other_wanted_card-1])

         print("\nWith", dealer[other_wanted_card-1], "added, your current deck of cards is:")
         human.append(dealer[other_wanted_card-1])
         dealer.pop(other_wanted_card-1)
         print_deck(human)

         print("And after discarding pairs and shuffling, your deck is:")
         human=remove_pairs(human)
         print_deck(human)

         wait_for_player()
         
         
         print("***********************************************************")

         if len(dealer)==0:
             print("Ups. I do not have any more cards")
             print("You lost! I, Robot, win")
             return

         print("My turn.\n")
         dealer_wanted_card = random.randint(1,len(human))

         if dealer_wanted_card == 1:
             d_super_script = "st"
         elif dealer_wanted_card == 2:
             d_super_script = "nd"
         elif dealer_wanted_card == 3:
             d_super_script = "rd"
         else:
             d_super_script = "th"
         print("I took your " + str(dealer_wanted_card) + d_super_script + " card.")
         dealer.append(human[dealer_wanted_card-1])
         human.pop(dealer_wanted_card-1)

         dealer=remove_pairs(dealer)
         
         wait_for_player()

         if len(human)==0:
            print("Ups. You do not have any more cards")
            print("Congratulations! You, Human, win")
            return

    
# Main
play_game()
