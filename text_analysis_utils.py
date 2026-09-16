# --- imports ---
import string
from collections import Counter

def get_text():
    raw_text = ""
    lines = []
    while True:
        option = input("How do you import the text? copy/file ")
        if option == "copy":
            while True:
                line = input("Paste enter the text: ")
                if line == "end":
                    break
                lines.append(line)
            raw_text = "\n".join(lines)
            break
                
        #if the user choose import the text through a text file
        elif option == "file":
            file_path = input("Enter the path of the file: ").strip("'")
            try:
                with open(file_path, "r") as file:
                    raw_text = file.read()

            except FileNotFoundError:
                print("The file wasn't fount! check the file path.")
                continue
            except PermissionError:
                print("You have not permission to access this file!")
                continue
            break

        else:
            print("Invalid choice.")
    return raw_text
# --- analysis helpers ---
def normalize_words(raw_text):
    words = []
    for to_be_stripped in raw_text.lower().split():
        word = to_be_stripped.strip(string.punctuation)
        if word:
            words.append(word)
    cleaned_text = words
    return cleaned_text

# --- text counter ---
def analyze(raw_text, cleaned_text):
    num_of_words = len(cleaned_text)
    char_with_space = len(raw_text)
    removed_spaces = raw_text.replace(" ", "")
    num_characters_without_space = len(removed_spaces)
    lines = raw_text.splitlines()
    num_of_lines = len(lines)
    sentenece_count = 0
    for i in raw_text:
        if i=="." or i=="!" or i=="?":
            sentenece_count+=1
    words = list(cleaned_text)
    character_dict = {}
    counter = Counter(cleaned_text)
    common_words = counter.most_common()
    five_common_words = common_words[0:5]
    for i in words:
        character_dict[i]=len(i)
    word_length = list(character_dict.values())
    sum_of_values = 0
    for i in word_length:
        sum_of_values += i
    try:
        average_legth = round(sum_of_values/len(word_length), 2)
    except ZeroDivisionError:
        print("There is no text to analyze")
    return {"words" : num_of_words,
             "characters with spaces": char_with_space,
             "characters withot spaces": num_characters_without_space,
               "lines": num_of_lines,
                 "sentences": sentenece_count,
                  "5 common words": five_common_words,
                  "average length": average_legth
                        }
