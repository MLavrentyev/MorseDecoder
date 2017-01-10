import re
import winsound
import time

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
    returnString = ""
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

            returnString += translatedLetter
        returnString += " "

    print(returnString)
    return returnString

def encodeMorse(inputText): #Encoder function
    cInputText = re.sub("[^A-za-z0-9\s/]", "", inputText) #Clean input to only have alpha numeric chars
    cInputText = cInputText.lower() #lower case everything
    returnString = ""
    words = cInputText.split(" ")
    for word in words:
        word.strip()
        letters = list(word)
        for letter in letters:
            returnString += morseDictionary.get(letter, "!") + " "

        returnString += "/ "
    returnString = returnString[:-3]
    print(returnString)
    return returnString

def beepCode(morseText):
    frequency = 500
    dotBeepLength = 100
    dashBeepLength = 200
    letterSpace = .200
    wordSpace = .500

    morseTextSplitWords = morseText.split(" / ")
    for word in morseTextSplitWords:
        letters = word.split(" ")
        for letter in letters:
            dotDashSeq = list(letter)
            for dotDash in dotDashSeq:
                if(dotDash == "-"):
                    winsound.Beep(frequency,dashBeepLength)
                elif(dotDash == "."):
                    winsound.Beep(frequency,dotBeepLength)
            # End parsing each dot/dash
            time.sleep(letterSpace)
        #End parsing letters
        time.sleep(wordSpace)
    #End parsing words


encodeMorse("Hello World")
decodeMorse(encodeMorse("Hello World"))
beepCode(encodeMorse("Hello World"))