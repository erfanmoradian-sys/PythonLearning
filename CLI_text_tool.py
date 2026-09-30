import argparse
import string
from text_analysis_utils import normalize_words, word_counter, char_cuonter, no_space_char_counter, line_counter, sentence_counter, five_common_words, word_average 

parser = argparse.ArgumentParser(description="Text analyzer program")

group = parser.add_mutually_exclusive_group()
group.add_argument("-uc", "--uppercase", action="store_true", help="Choose the option to change the text to uppercase letters")
group.add_argument("-lo", "--lowercase", action="store_true", help="Choose the option to change the text to lowercase letters")
group.add_argument("-ca", "--capitalize", action="store_true", help="Choose the option to change the text to capitalize")

parser.add_argument("filename", help="Enter the file name")
parser.add_argument("-wc", "--word_counter", action="store_true", help="Choose the option to count the words in the text")
parser.add_argument("-cc", "--char_counter", action="store_true", help="Choose the option to count characters including spaces")
parser.add_argument("-ns", "--no_space_char_counter", action="store_true", help="Choose the option to count characters without spaces")
parser.add_argument("-lc", "--line_counter", action="store_true", help="Choose the option to count lines in the text")
parser.add_argument("-sc", "--sentence_counter", action="store_true", help="Choose the option to count sentences in the text")
parser.add_argument("-fw", "--five_common_words", action="store_true", help="Choose the option to show five common words")
parser.add_argument("-wa", "--word_average", action="store_true", help="Choose the option to count and show word average")
parser.add_argument("-cp", "--clean_punctuation", action="store_true", help="Choose the option to clean punctuations")

args = parser.parse_args()

with open(args.filename) as file:
    text = file.read()

#Define uppercase function
def upper_case():
    upper_text = text.upper()
    print(upper_text)

#Define lowercase function
def lower_case():
    lower_text = text.lower()
    print(lower_text)

#Define capitalizing function
def capitalized():
    capitalized_text = text.capitalize()
    print(capitalized_text) 

#Define clean punctuation function 
def clean_punctuation():
    words = []
    for to_be_stripped in text.split():
        word = to_be_stripped.strip(string.punctuation)
        if word:
            words.append(word)
    new_text = " ".join(words)
    return new_text
    

if __name__ == "__main__":
    if args.word_counter:
        wc = word_counter(normalize_words(text))
        print(f"The text contains {wc} words")
    if args.char_counter:
        cc = char_cuonter(text)
        print(f"The text contains {cc} characters including spaces")
    if args.no_space_char_counter:
        ns = no_space_char_counter(text)
        print(f"The text contains {ns} characters excluding spaces")
    if args.line_counter:
        lc = line_counter(text)
        print(f"The text contains {lc} lines")
    if args.sentence_counter:
        sc = sentence_counter(text)
        print(f"The text contains {sc} sentences")
    if args.five_common_words:
        fw = five_common_words(normalize_words(text))
        print("Five common words of the text are:")
        print(fw)
    if args.word_average:
        wa = word_average(normalize_words(text))
        print(f"The length average of the words is {wa}")
    if args.uppercase:
        uc = upper_case()
    if args.lowercase: 
        lo = lower_case()    
    if args.capitalize: 
        cap = capitalized()                
    if args.clean_punctuation: 
        cp = clean_punctuation()
        print(cp)