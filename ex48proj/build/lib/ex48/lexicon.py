#Direction words: north, south, east, west, down, up, left, right, back.
#Verbs: go, stop, kill, eat.
#Stop words: the, in, of, from, at, it
#Nouns: door, bear, princess, cabinet.
#Numbers: any string of 0 through 9 characters.

lex = {
    'north':'direction',
    'south':'direction',
    'east':'direction',
    'west':'direction',
    'down':'direction',
    'up':'direction',
    'left':'direction',
    'right':'direction',
    'back':'direction',
    'go':'verb',
    'kill':'verb',
    'eat':'verb',
    'stop':'verb',
    'the':'stop',
    'in':'stop',
    'of':'stop',
    'from':'stop',
    'at':'stop',
    'it':'stop',
    'door':'noun',
    'princess':'noun',
    'cabinet':'noun',
    'bear':'noun',
    }
    
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
def scan():        
    stuff = raw_input('> ')
    words = stuff.split()
    sentence = []
    for x in words:
        if x in lex:
            word = (lex[x], x)
            sentence.append(word)
        elif convert_number(x) != None:
            word = ('number', int(x))
            sentence.append(word)
        else:
            word = ('error', x)
            sentence.append(word)
    return sentence
    

