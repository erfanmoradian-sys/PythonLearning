from collections import Counter
import string
text = """Python is a versatile, high-level programming language loved by developers worldwide.
Why do so many programmers start with Python?
Because Python prioritizes readability, simplicity, and clear syntax!
Whether you want to build web applications, analyze data, or automate tedious tasks, Python has the tools you need.
As you write more Python code, you will discover that writing code in Python feels almost like writing structured English.
Programming takes practice, time, and patience.
So keep writing Python, keep building projects, and keep solving real problems.
Remember: Great programmers are not born; they are made through daily practice with real code!"""

#removing white spaces and split the text to count number of words
words = []
for to_be_stripped in text.lower().split():
    word = to_be_stripped.strip(string.punctuation)
    if word:
        words.append(word)
num_of_words = len(words)
print(f"Number of words in the text is : {num_of_words}")
new_text = " ".join(words)
text_count_spaces = list(new_text)

#creating a list to insert the characters and count them
characters = list(new_text)
characters_with_spaces = len(characters)
print(f"Number of characters in the text including white spaces is : {characters_with_spaces}")

#removing white spaces
removed_spaces = new_text.replace(" ", "")
new_list = list(removed_spaces)
num_of_characters = len(new_list)
print(f"Number of characters in the text without whitespaces is : {num_of_characters}")

#counting number of lines through counting "\n" in characters list
lines = text.split("\n")
num_of_lines = len(lines)
print(f"number of lines of the text is : {num_of_lines}")

#counting sentence numbers through counting special characters for ending sentences.
sentence_text = list(text.lower().strip())
sentenece_count = 0
for i in sentence_text:
    if i=="." or i=="!" or i=="?":
        sentenece_count+=1
print(f"Number of sentences in the text is : {sentenece_count}")

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


    
        




