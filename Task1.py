from collections import Counter
import string
#Ask the user for choosing the way of importing the text
#Creating a list, adding lines of the text sentence by sentence
lines = []
text = ""
while True:
    option = input("How do you import the text? copy/file ")
    if option == "copy":
        while True:
            text_line = input("Paste the line: ")
            if text_line == "end":
                break
            lines.append(text_line)
        text = "\n".join(lines)
        print("The text is:")
        print(text)
        break
        
    #if the user choose import the text through a text file
    elif option == "file":
        file_path = "g:/coding/python/exercise/PythonLearning/text.txt"
        reading_type = int(input("""Reading the entire text: type 1
Reading the text line by line type 2 """))
        if reading_type ==1:
            #Exception handling:
            try:
                with open(file_path, "r") as file:
                    text = file.read()

            except FileNotFoundError:
                print("The file wasn't fount! check the file path.")
            except PermissionError:
                print("You have not permission to access this file!")

            print("The text in the file is: ")
            print(text)
            break

            
        elif reading_type ==2:
            try:
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        line.strip()
                    
            except FileNotFoundError:
                    print("The file wasn't fount! check the file path.")
            except PermissionError:
                    print("You have not permission to access this file!")
            text = "".join(lines)    
            print("The text in the file is: ")
            print(text)
            break
    else:
        print("Invalid choice.")



#Define a function to count the characters
def character_counter ():
    characters = list(new_text)
    characters_with_spaces = len(characters)
    print(f"Number of characters in the text including white spaces is : {characters_with_spaces}")


words = []
for to_be_stripped in text.lower().split():
    word = to_be_stripped.strip(string.punctuation)
    if word:
        words.append(word)

#Define a function to count the words
def word_counter():
    num_of_words = len(words)
    print(f"Number of words in the text is : {num_of_words}")

new_text = " ".join(words)
text_count_spaces = list(new_text)

#Define a function to count the characters
def character_counter ():
    characters = list(new_text)
    characters_with_spaces = len(characters)
    print(f"Number of characters in the text including white spaces is : {characters_with_spaces}")

word_counter()
character_counter ()

#removing white spaces
removed_spaces = new_text.replace(" ", "")
new_list = list(removed_spaces)
num_of_characters = len(new_list)
print(f"Number of characters in the text without whitespaces is : {num_of_characters}")

#Define a function to count the lines
def line_counter():
    lines = text.splitlines()
    num_of_lines = len(lines)
    print(f"number of lines of the text is : {num_of_lines}")



#Define a function to count the sentences
def sentence_counter():
    sentence_text = list(text.lower().strip())
    sentenece_count = 0
    for i in sentence_text:
        if i=="." or i=="!" or i=="?":
            sentenece_count+=1
    print(f"Number of sentences in the text is : {sentenece_count}")

line_counter()
sentence_counter()

#The Dictionary including words and their repetition
character_dict = {}
counter = Counter(words)
common_words = counter.most_common()
print("Most common words are: ")
print(common_words[0:5])

#The Dictionary including words and their lengths
for i in words:
    character_dict[i]=len(i)

#calculating the average of words' lengths
word_length = list(character_dict.values())
sum_of_values = 0
for i in word_length:
    sum_of_values += i
average_legth = (sum_of_values/len(word_length))
print(f"averag of length of the words in the text is {average_legth}")



            
                




    
        




