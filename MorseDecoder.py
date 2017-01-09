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
    "z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----."
}
def decodeMorse(inputMorse): #Decoder function
    wordList = []
    for word in inputMorse.split(" / "): #Split morse code by word
        word.strip()
        wordList.append(word)

    for word in wordList:
        letterList = word.split(" ")
        for wMorseLetter in letterList: #Clear whitespace from each letter
            nwMorseLet = wMorseLetter.strip().replace("_","-")

            translatedLetter = "!" # The default error symbol will be ! for untranslatable characters

            for key in morseDictionary: # Loop over morse dict to get needed letter
                if morseDictionary.get(key) == nwMorseLet:
                    translatedLetter = key
                    break # Once found, exit

            print(translatedLetter),
        print(" "),

