class ParseError(Exception):
    pass
class Sentence(object):
    def __init__(self, subject, verb, object):
    # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return 'none'
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
def parse_verb(word_list):
    skip(word_list, 'stop')
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    if peek(word_list) == 'none':
        return ('none', 'none')
    if peek(word_list) == 'number':
        return ('verb', 'enter')
    else:
        raise ParseError("Expected a verb next.")
def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)
    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    if next == 'number':
        return match(word_list, 'number')
    if next == 'none':
        return ('none', 'none')
    else:
        raise ParseError("Expected a noun or direction next.")
def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    sen = Sentence(subj, verb, obj)
    print sen.subject, sen.verb, sen.object
    return sen
def parse_sentence(word_list):
    skip(word_list, 'stop')
    start = peek(word_list)
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    elif start == 'number':
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParseError("Must start with subject, object, or verb not: %s" % start)