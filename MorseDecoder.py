morseDictionary = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--.."
}
def decodeMorse(inputMorse): #Decoder function
    wordList = []
    for word in inputMorse.split(" / "): #Split morse code by word
        word.strip()
        wordList.append(word)

    for word in wordList:
        letterList = word.split(" ")
        for letter in letterList: #Clear whitespace from each letter
            letter.strip()

