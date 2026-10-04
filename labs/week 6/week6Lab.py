# Name: Marcus Hernandez
# Assignment: Week 6 Lab (Sequences) PART 2
#
# Description: Reads a sentence and converts every word to Pig Latin.
# If a word starts with a vowel (a, e, i, o, u, y), "way" gets added
# to the end. Otherwise all the consonants at the start of the word are
# moved to the end and "ay" is added. Output is lowercase and punctuation
# is ignored. Keeps asking for sentences until the user just hits ENTER.

vowels = 'aeiouy'
letters = 'abcdefghijklmnopqrstuvwxyz'

def pig_latin_word(word):
    if word[0] in vowels:
        return word + 'way'
    # walk forward until we hit the first vowel (or run out of letters,
    # which handles words like "hmm" that have no vowels at all)
    index = 0
    while index < len(word) and word[index] not in vowels:
        index = index + 1
    # everything from the first vowel on, then the consonants, then "ay"
    return word[index:] + word[:index] + 'ay'

def convert_sentence(sentence):
    sentence = sentence.lower()
    # keep only letters and spaces so punctuation doesn't get in the way
    cleaned = ''.join([ch for ch in sentence if ch in letters or ch == ' '])
    words = cleaned.split()
    return ' '.join([pig_latin_word(w) for w in words])

def main():
    sentence = input('Enter a sentence (or just press ENTER to quit): ')
    while sentence != '':
        print(convert_sentence(sentence))
        sentence = input('Enter a sentence (or just press ENTER to quit): ')
    print('Goodbye!')

main()