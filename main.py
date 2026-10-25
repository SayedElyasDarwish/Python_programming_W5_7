DELIMITER = ","


def collectWords():
    words = ""

    while True:
        word = input("Insert word(empty stops): ")

        if word == "":
            break

        if words == "":
            words = word
        else:
            words = words + DELIMITER + word

    return words


def analyseWords(words):
    wordList = words.split(DELIMITER)

    if words == "":
        wordList = []

    wordCount = len(wordList)
    characterCount = 0

    for word in wordList:
        characterCount = characterCount + len(word)

    if wordCount > 0:
        averageLength = characterCount / wordCount
    else:
        averageLength = 0

    print(f"- {wordCount} Words")
    print(f"- {characterCount} Characters")
    print(f"- {averageLength:.2f} Average word length")


def main():
    print("Program starting.")

    words = collectWords()
    analyseWords(words)

    print("Program ending.")


if __name__ == "__main__":
    main()
