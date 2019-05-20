from idna import unicode
from wordfreq import tokenize, zipf_frequency
from PyDictionary import PyDictionary
from translate import Translator
import rtfunicode

from_language = 'en'
to_language = 'ar'

# To find WordNet meaning of a word
dictionary = PyDictionary()

# To provide multiple translations for a word
translator = Translator(to_lang=to_language)

# Open a text file
story = open('Stories/example.txt', 'r')

# The following line is to find the rtf unicode for any char
# print(u'RTF and unicode mix just fine! \🕵 '.encode('rtfunicode'))

story_title = story.readline().strip().strip('— ')
print(story_title)

# split text to words list
text = tokenize(story.read(), 'en')

# create output file which contains word, frequency score, meaning, arabic translation
output_file = open('TranslatedStoryWords/1.' + story_title + '.rtf', 'w')

output_file.write('{\\rtf1')
output_file.write(story_title + '\\u10')
i = 0

# iterate though words of the text
for word in text:
    # find zipf_frequency of the word to determine familiarity of the word
    zipf = zipf_frequency(word, from_language)
    if zipf <= 4.5:
        i += 1
        output_file.write('\\b ' + str(i) + '.' + word + ' ' + str(zipf) + ' \\b0')
        meaning = dictionary.meaning(word)
        if type(meaning) is dict:
            for k, v in meaning.items():
                output_file.write(' \\b ' + k + ": " + ' \\b0 ' + ', '.join(v))
            # f.write(str(meaning))
        else:
            print(meaning)

        output_file.write(((' ترجمة قوقل: ' + str(dictionary.translate(word, to_language)) + ' ').encode('rtfunicode')).decode())

        translation = translator.translate(word)
        if 'MEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY.' in translation:
            output_file.write('$' * 30)
            break
        else:
            output_file.write(translation.encode('rtfunicode').decode() + ' ')
            output_file.write('🎩🧥🔍🎩🧥🔍🎩🧥🔍\n'.encode('rtfunicode').decode())

output_file.write('}')

output_file.close()

