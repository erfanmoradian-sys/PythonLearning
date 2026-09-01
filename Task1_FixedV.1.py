text = """Python is a versatile, high-level programming language loved by developers worldwide.
Why do so many programmers start with Python?
Because Python prioritizes readability, simplicity, and clear syntax!
Whether you want to build web applications, analyze data, or automate tedious tasks, Python has the tools you need.
As you write more Python code, you will discover that writing code in Python feels almost like writing structured English.
Programming takes practice, time, and patience.
So keep writing Python, keep building projects, and keep solving real problems.
Remember: Great programmers are not born; they are made through daily practice with real code!"""

#removing white spaces and split the text to count number of words
list_of_words = text.strip().lower()
new_text = list_of_words.replace(",", "").replace("?", "").replace(".", "").replace("-", "").replace("!", "").replace(":", "")
list_of_new_text = new_text.split()
num_of_words = len(list_of_new_text)
print(f"Number of words in the text is : {num_of_words}")

#creating a list to insert the characters and count them
characters = list(list_of_words)
characters_with_spaces = len(characters)
print(f"Number of characters in the text including white spaces is : {characters_with_spaces}")

#removing white spaces
removed_spaces = list_of_words.replace(" ", "").replace("\n","" )
new_list = list(removed_spaces)
num_of_characters = len(new_list)
print(f"Number of characters in the text without whitespaces is : {num_of_characters}")

#counting number of sentences through counting "\n" in characters list
num_of_lines = characters.count("\n")+1
print(f"number of lines of the text is : {num_of_lines}")

#counting sentence numbers through counting special characters for ending sentences.
sentenece_count = 0
for i in characters:
    if i=="." or i=="!" or i=="?":
        sentenece_count+=1
print(f"Number of sentences in the text is : {sentenece_count}")

#The Dictionary including words and their repetition
character_dict = {}
repetition_dict = {}
for i in list_of_new_text:
    if i in repetition_dict:
        repetition_dict[i] += 1
    else:
        repetition_dict[i]= 1

#The Dictionary including words and their lengths
for i in list_of_new_text:
    character_dict[i]=len(i)
#calculating the average of words' lengths
word_length = list(character_dict.values())
sum_of_values = 0
for i in word_length:
    sum_of_values += i
average_legth = round(sum_of_values/len(word_length))
print(f"averag of length of the words in the text is {average_legth}")

#finding 5 most common words in the text
#extracting repetitionDict values to sorting and finding 5 last elements of the list
word_ferequency = list(repetition_dict.values())
sorted_word_ferequency = sorted(word_ferequency)
most_common_words_values = sorted_word_ferequency[-5:]

common_words = []
items = list(repetition_dict.values())
new_items = sorted(items, reverse=True)
common_values = new_items[:5]
common_words_dict = {}
for k, v in repetition_dict.items():
    if v in common_values:
        common_words_dict[k] = v
print("Top 5 most common words are : ")
print(common_words_dict)

    
        




