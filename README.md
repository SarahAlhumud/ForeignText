## ForeignText
ForeignText is a python script to extract difficult words in a text and find meaning and multiple translations of these words.

**For example:** 
```
Right Mind:
I am the right brain. I am creativity. A free spirit. I am passion. Yearning. Sensuality, I am the sound of roaring laughter. I am taste. The feeling of sand beneath bare feet.
I am movement. Vivid colors. I am the urge to paint on an empty canvas. I am boundless imagination. Art. Poetry. I sense. I feel.
I am everything I wanted to be.
```
when previous text is processed in ForeignText, the output -as text file- will be:

```
1.creativity 4.02 
Noun:  the ability to create
ترجمة قوقل: None
الإبداع
2.passion 4.45 
Noun:  a strong feeling or emotion, the trait of being intensely emotional, something that is desired intensely, an irrational but irresistible motive for a belief or action, a feeling of strong sexual desire, any object of warm affection or devotion, the suffering of Jesus at the Crucifixion
ترجمة قوقل: None
عاطفة
3.yearning 3.18 
Noun:  prolonged unfulfilled desire or need 
Verb:  desire strongly or persistently, have a desire for something or someone who is not present, have affection for; feel tenderness for 
ترجمة قوقل: None
متلهف
....
18.poetry 4.4 
Noun:  literature in metrical form, any communication resembling poetry in beauty or the evocation of feeling 
ترجمة قوقل: None
شعر, أشعار, الصفة الشعرية, الإحساس الشعري
```

## Motivation
I wrote this script to simplify reading Sherlock Holmes stories and novels.

## Python Modules Used
**Module to find frequencies of words:**

[wordfreq](https://pypi.org/project/wordfreq/)
> wordfreq is a Python library for looking up the frequencies of words in many languages, based on many sources of data.

**Module to get meanings and google translations of words:**

[PyDictionary](https://pypi.org/project/PyDictionary/)
> PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses WordNet for getting meanings and Google for translations.

**Module to get multiple translations of words:**

[translate](https://pypi.org/project/translate/)
> Translate is a simple but powerful translation tool written in python with with support for multiple translation providers.

## Getting started
1. Download ForeignText.
2. Change the directory to ForeignText.
`cd ForeignText`
3. Install the required [modules](#python-modules-used).
4. Modify script to what you want. see [Usage](#usage) section.
5. Run the script
`python main.py`
6. The output file will be exist in `TranslatedStoryWords`.
7. Hope you enjoy in reading :)

## Usage
**`main.py` file:**

To set text's language and translation's language, in line 7,8:
```
from_language = 'en'
to_language = 'ar'
```

To set file path of a text, in line 17:
```
story = open('Stories/example.txt', 'r')
```

To change output's name and title, in line 22. Change it to string:
``` 
story_title = story.readline().strip().strip('— ')
```
<br>

**`TextExtraction.py` file:**

This file extracts stories in this [page](http://freeread.com.au/@RGLibrary/ArthurConanDoyle/SherlockHolmes/RETU.html) to 14 text files. These files exist in `Stories` directory.






