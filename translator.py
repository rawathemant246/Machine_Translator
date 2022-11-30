
#import dependencies

from translate import Translator




class translation:

    def __init__(self, text):
        self.text = text

    def translate_word(self):
        translator = Translator(from_lang='en', to_lang='hi')
        translation = translator.translate(self.text)
        return translation

#trans = translation("I'm not lying")
#result = trans.translate_word()
#print(result)





