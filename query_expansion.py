import nltk
import string

# Preprocessing
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Correct spellings
from nltk.corpus import words
from nltk.metrics.distance import edit_distance

# Synonyms
from nltk.wsd import lesk
from nltk.corpus import wordnet

import nltk
import string

# Preprocessing
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Correct spellings
from nltk.corpus import words
from nltk.metrics.distance import edit_distance

# Synonyms
from nltk.corpus import wordnet

import enchant

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('words')


def preprocess_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word.lower(
    ) not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    keys = ["photo", "image", "picture"]
    words = [lemmatizer.lemmatize(word) for word in words]
    words = [word for word in words if word not in keys]
    return text, words


def correct_spellings(processed_text, base_query):
    correct_words = words.words()
    for i in range(0, len(processed_text)):
        word = processed_text[i]
        temp = [(edit_distance(word, w), w)
                for w in correct_words if w[0] == word[0]]
        corrected_word = sorted(temp, key=lambda val: val[0])[0][1]
        base_query = base_query.replace(word, corrected_word)
        processed_text[i] = corrected_word
    return base_query, processed_text



# def find_synonyms(processed_text, base_query):
#     context = base_query
#     expanded_query = []
#     for word in processed_text:
#         wsd = lesk(context.split(), word, 'n')
#         if wsd is not None:
#             print(wsd.name(), wsd.definition())
#             expanded_query += [syn.name() for syn in wsd.lemmas()]
#     return " ".join(expanded_query)

def find_synonyms(processed_text, base_query, num_synonyms=10):
    expanded_query = []
    for word in processed_text:
        # Attempt to correct spelling
        suggestions = enchant.Dict("en_US").suggest(word)
        if suggestions:
            corrected_word = suggestions[0]
        else:
            corrected_word = word
        
        # Get synonyms
        synonyms = wordnet.synsets(corrected_word)
        if synonyms:
            # Get synonyms relevant to the context
            relevant_synonyms = [lemma.name() for synset in synonyms for lemma in synset.lemmas() if lemma.name() != word]
            # Limit to the desired number of synonyms or all available synonyms, whichever is smaller
            num_syn = min(num_synonyms, len(relevant_synonyms))
            expanded_query.extend(relevant_synonyms[:num_syn])
    return " ".join(expanded_query)



def expand_query(base_query):
    print("Base query", base_query)
    base_query, processed_text = preprocess_text(base_query)
    print("Processed text", processed_text)
    base_query, processed_text = correct_spellings(processed_text, base_query)
    print("Spellings corrected", processed_text)
    expanded_query = find_synonyms(processed_text, base_query)
    return expanded_query

def main():
    print(expand_query("happy faces"))

if __name__ == "__main__":
    main()
