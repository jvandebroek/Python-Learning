#Direction words: north, south, east, west, down, up, left, right, back.
#Verbs: go, stop, kill, eat.
#Stop words: the, in, of, from, at, it
#Nouns: door, bear, princess, cabinet.
#Numbers: any string of 0 through 9 characters.

lex = {}
lex.update(dict.fromkeys(['north','east','west','down','south','up','left','right','back'], 'direction'))
lex.update(dict.fromkeys(['take','go','kill','eat','stop','hide','enter','exit','pickup','grab','leave', 'search', 'look','type'], 'verb'))
lex.update(dict.fromkeys(['the','in','of','from','at','it','through','to'], 'stop'))
lex.update(dict.fromkeys(['door','princess','cabinet','bear','closet','scalpel','doorway', 'Escape', 'Office', 'Weaponry', 'pistol', 'machine', 'grenade','escape', 'office', 'computer', 'file', 'weaponry','room'],'noun'))

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
def scan(stuff):        
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

