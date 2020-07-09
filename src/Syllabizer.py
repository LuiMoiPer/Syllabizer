from typing import List
from lark import Lark

class Syllabizer:
    """This class syllabizes words fed into it according to rules it was initiallized with.  Also
    stores some record about the set of words that have been fed into it.
    """

    def __init__(self, rules):
        self._rules = rules
        # using the rules we need to make parsers
        grammar = self._make_grammar(rules.syllable_structures, rules.consonants, rules.vowels)
        self._parser = Lark(grammar)

        # make the sets that store syllable stats/info
        self._unique_syllables = set()
        self._begining_syllables = set()
        self._ending_syllables = set()
        # probally want the following stats
        # max sylls
        # min sylls
        # ave len sylls
        # std len sylls

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

    def _make_grammar(syllable_structures, consonants, vowels) -> str:
        consonant_str = ""
        for index, consonant in enumerate(consonants):
            if index > 0:
                consonant_str += "| "
            consonant_str += consonant + "\n"
            if index != len(consonants) - 1:
                consonant_str += "\t"
            
        vowel_str = ""
        for index, vowel in enumerate(vowels):
            if index > 0:
                consonant_str += "| "
            vowel_str += vowel + "\n"
            if index != len(vowels) - 1:
                vowel_str += "\t"

        grammar = f"""start: word
        word: syllables
        ?syllables: syllable
            | syllables syllable
        syllable: vowel
            | consonant vowel
            | consonant vowel consonant
        consonant: {consonant_str}
        vowel: {vowel_str}
        %import common.WS_INLINE
        """

        return grammar

    def syllabize(words: List[str]) -> List[List[str]]:
        output = []
        for word in words:
            syllables = []
            # have to worry about words that dont parse
            # parse the word
            # update start, end, and unique sylls
            # update number stats
            # append a list of sylls to out
            pass
        pass


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