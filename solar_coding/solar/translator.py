from abc import abstractmethod


class Translator:
    """
    Base Translator Template Class
    """
    def __init__(self, lang_from, lang_to, consonant, vowels,
                 suffix=None):

        args = [lang_from, lang_to, consonant, vowels]

        if any([arg is None for arg in args]):
            raise ValueError('None is not accepted')

        self.lang_from = lang_from
        self.lang_to = lang_to
        self.consonant = consonant
        self.vowels = vowels
        self.suffix = suffix

    @abstractmethod
    def translate(self, string):
        pass

    @classmethod
    def factory(cls):
        pass

    def __repr__(self):
        return f'Translator({self.lang_from}, {self.lang_to})'
