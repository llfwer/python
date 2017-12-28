import nltk


# C:\Users\John Smith\AppData\Roaming\nltk_data 占空间

def sentences():
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    paragraph = 'The first time I heard that song was in Hawaii on radio.  I was just a kid, and loved it very much! What a fantastic song!'
    sentences = sent_tokenizer.tokenize(paragraph)
    print(sentences)


def word():
    sentence = 'Are you old enough to remember Michael Jackson attending the Grammys with Brooke Shields and Webster sat on his lap during the show?'
    words = nltk.WordPunctTokenizer().tokenize(sentence)
    print(words)


def special_word():
    text = 'That U.S.A. poster-print costs $12.40...'
    pattern = r"""(?x)                   # set flag to allow verbose regexps 
              (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A. 
              |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages 
              |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe 
              |\.\.\.                # ellipsis 
              |(?:[.,;"'?():-_`])    # special characters with meanings 
            """
    words = nltk.regexp_tokenize(text, pattern)
    print(words)


sentences()
