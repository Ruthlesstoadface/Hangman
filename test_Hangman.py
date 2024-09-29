from Hangman import wordFunction
from Hangman import letterCheck
def test_wordFunction():
    result = wordFunction("water")
    for char in result:
        assert char["isGuessed"] == False
    print(result)
    assert len(result)== len("water")

def test_letterCheck():
    result = wordFunction("water")
    letterCheck("a", result)
    for char in result:
        if char["char"] == "a":
            assert char["isGuessed"] == True
        else:
            assert char["isGuessed"] == False