def countCharacters(self, words: List[str], chars: str) -> int:
    sortedChars = sorted(chars)
    output = ''
    for word in words:
        sortedWord = sorted(word)

        for i in range(len(sortedWord)):
            if sortedWord[i] in sortedChars:
                pass
            else:
                break
        output += word

    return len(output)
