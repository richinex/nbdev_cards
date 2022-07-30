# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_deck.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../01_deck.ipynb 2
from .cards import *
from fastcore.utils import patch
import random

# %% ../01_deck.ipynb 4
class Deck:
    """
    A deck of 52 cards, not including jokers
    """
    def __init__(self): self.cards = [Card(s, r) for s in range(4) for r in range(1, 14)]
    def __len__(self): return len(self.cards)
    def __str__(self): return '; '.join(map(str, self.cards))
    def __contains__(self, card): return card in self.cards
    __repr__ = __str__
    
    def shuffle(self):
        "Shuffles the cards in this deck"
        random.shuffle(self.cards)

# %% ../01_deck.ipynb 15
@patch
def pop(self:Deck, 
        idx:int=-1): # The index of the card to remove, defaulting to the last one
    """
    Remove one card from the deck
    """
    return self.cards.pop(idx)

# %% ../01_deck.ipynb 19
@patch
def remove(self:Deck, 
        card:Card): # The index of the card to remove, defaulting to the last one
    """
    Removes `card` from the deck or raises exception if it is not there
    """
    self.cards.remove(card)

# %% ../01_deck.ipynb 21
def draw_n(n:int, # number of cards to draw
          replace:bool=True): # Whether or not to draw with replacement
    """
    Draw `n` cards, with replacement if `replace`
    """
    d = Deck()
    d.shuffle()
    if replace: return [d.cards[random.choice(range(len(d.cards)))] for _ in range]
    else: return d.cards[:n]
