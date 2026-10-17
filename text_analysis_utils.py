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

def word_counter(cleaned_text):
    num_of_words = len(cleaned_text)
    return num_of_words

def char_cuonter(raw_text):
    char_with_space = len(raw_text)
    return char_with_space

def no_space_char_counter(raw_text):
    removed_spaces = raw_text.replace(" ", "")
    num_characters_without_space = len(removed_spaces)
    return num_characters_without_space

def line_counter(raw_text):
    lines = raw_text.splitlines()
    num_of_lines = len(lines)
    return num_of_lines

def sentence_counter(raw_text):
    sentenece_count = 0
    for i in raw_text:
        if i=="." or i=="!" or i=="?":
            sentenece_count+=1
    return sentenece_count

def five_common_words(cleaned_text):
    counter = Counter(cleaned_text)
    common_words = counter.most_common()
    five_common_words = common_words[0:5]
    return five_common_words

def word_average(cleaned_text):
    character_dict = {}
    words = list(cleaned_text)
    for i in words:
        character_dict[i]=len(i)
    word_length = list(character_dict.values())
    sum_of_values = 0
    for i in word_length:
        sum_of_values += i
    average_length = 0
    try:
        average_length = round(sum_of_values/len(word_length), 2)
    except ZeroDivisionError:
        print("There is no text to analyze")
    return average_length

# --- text counter ---
def analyze(raw_text, cleaned_text):
    num_of_words = word_counter(cleaned_text)
    char_with_space = char_cuonter(raw_text)
    num_characters_without_space = no_space_char_counter(raw_text)
    num_of_lines = line_counter(raw_text)
    sentenece_count = sentence_counter(raw_text)
    five_words = five_common_words(cleaned_text)
    word_length_average = word_average(cleaned_text)
    return {"words": num_of_words, "characters_with_spaces": char_with_space,
             "characters_without_spaces" : num_characters_without_space,
             "lines": num_of_lines,
              "sentences": sentenece_count,
               "five_common_words": five_words,
                "average_length": word_length_average }













