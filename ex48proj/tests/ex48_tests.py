from nose.tools import *
from ex48 import lexicon
from ex48 import sentence
##This file includes the tests for ex49

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])
def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
    ('error', 'IAS'),
    ('noun', 'princess')])


## EX 49 TESTS:-------------------------------------------------------------
def test_peek():
    assert_equal(sentence.peek([('noun', 'bear'), ('stop', 'the')]), 'noun')
    assert_equal(sentence.peek([('house', 'bear'), ('stop', 'the')]), 'house')
    assert_equal(sentence.peek([('dog', 'bear'), ('stop', 'the')]), 'dog')

def test_match():
    assert_equal(sentence.match([('noun', 'bear'), ('stop', 'the')], 'noun'), ('noun', 'bear'))
    assert_equal(sentence.match([('noun', 'bear'), ('stop', 'the')], 'house'), None)

def test_skip():
    words = [('noun', 'bear'), ('stop', 'the'), ('house','fire')]
    sentence.skip(words, 'noun')
    assert_equal(words, [('stop', 'the'), ('house', 'fire')]) 

def test_parse():
    words = [('noun', 'bear'), ('stop', 'the'), ('verb','run'), ('noun', 'car')]
    testSen = sentence.parse_sentence(words)
    createdSen = sentence.Sentence(('noun', 'bear'),('verb','run'),('noun', 'car'))
    assert_equal(testSen.subject, createdSen.subject)
    assert_equal(testSen.verb, createdSen.verb)
    assert_equal(testSen.object, createdSen.object)
def test_errors():
    assert_raises(sentence.ParseError, sentence.parse_verb, [('noun', 'house')])
    assert_raises(sentence.ParseError, sentence.parse_object, [('verb', 'house')])
    assert_raises(sentence.ParseError, sentence.parse_sentence, [('coolguy', 'house')])

