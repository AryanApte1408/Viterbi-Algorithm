import nltk
nltk.download('all')
from nltk.grammar import toy_pcfg1
from nltk.parse import ViterbiParser
from nltk import tokenize
import sys,time
from nltk.grammar import PCFG, induce_pcfg

new = PCFG.fromstring("""
     S    -> NP VP         [1.0]
     VP   -> V NP          [.59]
     VP   -> V             [.40]
     VP   -> VP PP         [.01]
     NP   -> Det N         [.41]
     NP   -> Name          [.28]
     NP   -> NP PP         [.31]
     PP   -> P NP          [1.0]
     V    -> 'sat'         [.21]
     V    -> 'went'         [.51]
     V    -> 'eat'         [.28]
     N    -> 'boy'         [.11]
     N    -> 'cookie'      [.12]
     N    -> 'table'       [.13]
     N    -> 'telescope'   [.19]
     N    -> 'chocolates'        [.45]
     Name -> 'Riya'         [.32]
     Name -> 'Lisa'        [.68]
     P    -> 'and'        [.51]
     P    -> 'above'       [.19]
     P    -> 'on'          [.10]
     P    -> 'to'          [.20]
     Det  -> 'the'         [.41]
     Det  -> 'a'           [.31]
     Det  -> 'an'          [.28]
     

     
    """)

demos = [('Lisa and Riya sat on the table to eat chocolates', new)]
sent, grammar = demos[0]
parser = ViterbiParser(grammar)
print('\ns: %s\nparser: %s\ngrammar: %s' % (sent,parser,grammar))

tokens = sent.split()

parser.trace(3)
t = time.time()
parses = parser.parse_all(tokens)

if parses:
  lp = len(parses)
else:
  p=0