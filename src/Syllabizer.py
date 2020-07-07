from typing import List

class Syllabizer:
    """This class syllabizes words fed into it according to rules it was initiallized with.  Also
    stores some record about the set of words that have been fed into it.
    """

    def __init__(self, rules):
        self._rules = rules
        # using the rules we need to make parsers
        # need a vowel parser
        # need a consonant parser

        # stores every unique syllable ever fed into this 
        self._unique_syllables = set()
        pass

    def syllabize(self, words = List[str]):
        syllables = []
        for word in words:
            word.lower()
            # tokenize into consonants and vowels
            # tokenize into syllables
            # add syllable in to syllables
            # add token to uniques
            pass
        return syllables

    def _tokenize_phonemes(self, word):
        # probably done with regex
        phonemes = []
        # for each vowel rule
            # try to make a token
        # for each consonant rule
            # try to make a token
        pass

    def _tokenize_syllables(self):
        # probaly done with not regex because were going from phonemes to syllables
        # make tokens using every syllable structure
        # if any phonemes are left, give a warning?
        pass


class Syllable:
    """Represents a one unit part of a word, and is made up of phonemes"""
    def __init__(self, nucleus, onset = None, coda = None):
        self._onset = onset
        self._nucleus = nucleus
        self._coda = coda
        pass

    def __str__(self) -> str:
        string = ""
        if self._onset is not None:
            string += str(self._onset)
        string += str(self._nucleus)
        if self._coda is not None:
            string += str(self._coda)
        return string

    def __repr__(self):
        raise NotImplementedError

class Phoneme:
    """A representation of the smallest unit of sound according to the provided rules.  Both 
    consonants and vowels inherit from this."""
    def __init__(self, characters: str, vowel: bool):
        self._characters = characters
        self._vowel = vowel

    def __len__(self):
        return len(self._characters)

    def __str__(self):
        return self._characters

    @property
    def vowel(self):
        return self._characters

    @property
    def consonant(self):
        return not self._vowel


class Rules:
    """A representation of the rules for the syllabizer to use when syllabizing words.  Should 
    include syllable structure, n-phthongs, n-graphs.  The lists should be in the priority order?

    :param vowels: A list of strings that represents all possible vowels for the language.  Should 
        contain all nphthongs as well as any vowel digraphs in the language.
    :param consonants: A list of strings that represents all the possible consonants for the 
        language.  Should also include any digraphs that are considered consonants.
    :param syllable_structures: A list os all valid syllable structures in the language.  This list
        should only consist of the letters 'c' and 'v' ex: ['V'. 'CV', 'CVC']
    """

    def __init__(self,
        vowels: List[str],
        consonants: List[str],
        syllable_structures: List[str], 
    ):
        # store the passed in language rules
        self._consonants = set(consonants)
        self._vowels = set(vowels)
        self._syllable_structures = set(syllable_structures)

    @property
    def consonants(self):
        return self._consonants

    @property
    def vowels(self):
        return self._vowels

    @property
    def syllable_structures(self):
        return self._syllable_structures


if __name__ == "__main__":
    pass