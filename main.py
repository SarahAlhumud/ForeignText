from idna import unicode
from wordfreq import tokenize, zipf_frequency
from PyDictionary import PyDictionary
from translate import Translator
import rtfunicode

# To find WordNet meaning of a word
dictionary = PyDictionary()

# To provide multiple translations for a word
translator = Translator(to_lang="Arabic")

# Open a text
story = open('1.txt', 'r')

# The following line is to find the rtf unicode for any char
# print(u'RTF and unicode mix just fine! \🕵 '.encode('rtfunicode'))

story_title = story.readline().strip().strip('— ')
print(story_title)

# split text to words list
text = tokenize(story.read(), 'en')

# create output file which contains word, frequency score, meaning, arabic translation
words_file = open("1." + story_title + '.rtf', 'w')

words_file.write('{\\rtf1')
words_file.write(story_title + '\\u10 \\u10')
i = 0


for word in text:
    zipf = zipf_frequency(word, 'en')
    if zipf <= 4.5:
        i += 1
        words_file.write('\\b ' + str(i) + '.' + word + ' ' + str(zipf)+' \\b0  \\u10')
        meaning = dictionary.meaning(word)
        if type(meaning) is dict:
            for k, v in meaning.items():
                words_file.write(' \\b ' + k + ": " + ' \\b0 ' + ', '.join(v)+'  \\u10')
            # f.write(str(meaning))
        else:
            print(meaning)

        translation = translator.translate(word) + ' \n'
        if translation.find('YMEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY.'):
            words_file.write('$'*30)
            break
        else:
            words_file.write(translation.encode('rtfunicode').decode())
            # 🕵
            words_file.write('\\u-10179\\u-8843\\u-497 '*30 + '\\u10\\u10')

        # words_file.write((u'ترجمة قوقل:' + str(dictionary.translate(word,'ar')) + u' \n'))
        words_file.write(
            (('ترجمة قوقل: ' + str(dictionary.translate(word, 'ar')) + ' \n').encode('rtfunicode')).decode())

words_file.write('}')

words_file.close()

