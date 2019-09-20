from .translator import Translator
import re


class EngToPiglatinTranslator(Translator):
    """
    implements Base Translator
    English to Pig Latin Translator
    >>> eng_pig = EngToPiglatinTranslator.factory()
    >>> eng_pig.translate('pig') == 'igpay'
    """

    def __init__(self, *args, **kwargs):
        super(EngToPiglatinTranslator, self).__init__(*args, **kwargs)
        self.re = {
            'consonant': re.compile(f"({'|'.join(self.consonant)})*",
                                    flags=re.IGNORECASE),
            'vowels': re.compile(f"({'|'.join(self.vowels)})*",
                                 flags=re.IGNORECASE)
        }

    @classmethod
    def factory(cls):
        consonants = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                      'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z'}
        vowels = {'A', 'E', 'I', 'O', 'U'}

        return cls(lang_from='eng', lang_to='pig latin',
                   consonant=consonants, vowels=vowels,
                   suffix='ay')

    def translate(self, string):

        consonant = self.re['consonant'].match(string)
        vowel = self.re['vowels'].match(string)

        if bool(consonant) and consonant.start() == 0:
            end = consonant.end()
            res = string[end:] + string[:end] + self.suffix

        elif bool(vowel) and vowel.start() == 0:
            res = string + self.suffix
        else:
            res = 'Error occurred'

        return res
