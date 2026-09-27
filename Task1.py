from text_analysis_utils import get_text, normalize_words, analyze

def main():
    while True:
        text = get_text()
        if text:
            break
    clean_text = normalize_words(text)
    result = analyze(text, clean_text)
    print(f"The text contains {result['words']} words")
    print(f"{result['characters_with_spaces']} characters with spaces")
    print(f"{result['characters_without_spaces']} characters without spaces")
    print(f"{result['lines']} lines")
    print(f"{result['sentences']} sentences")
    print(f" five common words are {result['five_common_words']}")
    print(f"average length of words is {result['average_length']}")




if __name__ == "__main__":
    main()