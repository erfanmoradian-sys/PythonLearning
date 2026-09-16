from text_analysis_utils import get_text, normalize_words, analyze

def main():
    text = get_text()
    if not text:
        print("Text is empty")
        text = get_text()
    clean_text = normalize_words(text)
    result = analyze(text, clean_text)
    print(f"The text contains {result['words']} words")
    print(f"{result['characters with spaces']} characters with spaces")
    print(f"{result['characters withot spaces']} characters withot spaces")
    print(f"{result['lines']} lines")
    print(f"{result['sentences']} sentences")
    print(f" five common words are {result['5 common words']}")
    print(f"average length of words is {result['average length']}")




if __name__ == "__main__":
    main()