import argparse
import string

parser = argparse.ArgumentParser(description="Text analyzer program")
parser.add_argument("filename", help="Enter the file name")
parser.add_argument("-uc", "--uppercase", action="store_true", help="Choose the option to change the text to uppercase letters")
parser.add_argument("-lc", "--lowercase", action="store_true", help="Choose the option to change the text to lowercase letters")
parser.add_argument("-c", "--capitalize", action="store_true", help="Choose the option to change the text to capitalize")
parser.add_argument("-cp", "--clean-punctuation", action="store_true", help="Choose the option to clean punctuations")

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
    print(new_text)

if __name__ == "__main__":
    if args.uppercase:
        upper_case()
    if args.lowercase: 
        lower_case()    
    if args.capitalize: 
            capitalized()                
    if args.clean_punctuation: 
        clean_punctuation()
