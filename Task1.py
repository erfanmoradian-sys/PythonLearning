text = """Python is a versatile, high-level programming language loved by developers worldwide.
Why do so many programmers start with Python?
Because Python prioritizes readability, simplicity, and clear syntax!
Whether you want to build web applications, analyze data, or automate tedious tasks, Python has the tools you need.
As you write more Python code, you will discover that writing code in Python feels almost like writing structured English.
Programming takes practice, time, and patience.
So keep writing Python, keep building projects, and keep solving real problems.
Remember: Great programmers are not born; they are made through daily practice with real code!"""

#removing white spaces and split the text to count number of words
listOfWords = text.strip().split()
numOfWords = len(listOfWords)
print(f"Number of words in the text is : {numOfWords}")

#creating a list to insert the characters and count them
characters = list(text)
charactersWithSpaces = len(characters)
print(f"Number of characters int the text including white spaces is : {charactersWithSpaces}")

#removing white spaces
removedSpaces = text.replace(" ", "")
newList = list(removedSpaces)
numOfCharacters = len(newList)
print(f"Number of characters in the text without whitespaces is : {numOfCharacters}")

#counting number of sentences through counting "\n" in characters list
numOflines = characters.count("\n")+1
print(f"number of lines of the text is : {numOflines}")

#counting sentence numbers through counting special characters for ending sentences.
senteneceCount = 0
for i in characters:
    if i=="." or i=="!" or i=="?":
        senteneceCount+=1
print(f"Number of sentences in the text is : {senteneceCount}")

#The Dictionary including words and their repetition
characterDict = {}
repetitionDict = {}
for i in listOfWords:
    if i in repetitionDict:
        repetitionDict[i] += 1
    else:
        repetitionDict[i]= 1

#The Dictionary including words and their lengths
for i in listOfWords:
    characterDict[i]=len(i)

#calculating the average of words' lengths
wordLength = list(characterDict.values())
sumOfValues = 0
for i in wordLength:
    sumOfValues += i
averageLegth = int(sumOfValues/len(wordLength))
print(f"averag of length of the words in the text is {averageLegth}")

#finding 5 most common words in the text
#extracting repetitionDict values to sorting and finding 5 last elements of the list
wordFerequency = list(repetitionDict.values())
sortedWordFerequency = sorted(wordFerequency)
mostCommonWordsValues = sortedWordFerequency[-5:]


commonWords =[]
for keys ,values in repetitionDict.items():
    for i in mostCommonWordsValues:
        if values == i:
            commonWords.append(keys)
print("5 most common words in the text are :")
print(commonWords)




