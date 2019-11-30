# bad
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chardict = {}
        output = ''
        for char in chars:
            if char in chardict:
                chardict[char] += 1
            else:
                chardict[char] = 1

        for word in words:
            lettercount = 0
            letterdict = {}
            for letter in word:

                if letter in letterdict:
                    letterdict[letter] += 1
                else:
                    letterdict[letter] = 1

            for key in letterdict:
                if key in chardict and letterdict[key] <= chardict[key]:
                    lettercount += letterdict[key]

            if lettercount == len(word):
                output += word

        return len(output)
