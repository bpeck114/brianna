# File: average_vowels_solns.py

paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

def counting_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)

def average_vowels_and_consonants(paragraph):
    import re

    # Split into sentences using punctuation as a guide
    sentences = re.split(r'[.!?]', paragraph)
    # Remove any empty strings or spaces
    sentences = [s.strip() for s in sentences if s.strip()]

    total_vowels = 0
    total_consonants = 0

    for sentence in sentences:
        v, c = counting_vowels_and_consonants(sentence)
        total_vowels += v
        total_consonants += c

    num_sentences = len(sentences)
    avg_vowels = total_vowels / num_sentences
    avg_consonants = total_consonants / num_sentences

    return (num_sentences, avg_vowels, avg_consonants)

result = average_vowels_and_consonants(paragraph)
print("Number of sentences:", result[0])
print("Average vowels per sentence:", result[1])
print("Average consonants per sentence:", result[2])