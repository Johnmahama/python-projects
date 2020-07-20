from googletrans import Translator


class Simple_Translator(object):
    def __init__(self,word,language):
        self.word  = word
        self.language= language
        self.cursor = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        translator = self.cursor.translate(self.word,dest=self.language)
        return translator.text


if __name__=="__main__":
    sentence = input(str("Enter string to translate: \n\t"))
    translate = Simple_Translator(sentence,"en")
    print(translate)
