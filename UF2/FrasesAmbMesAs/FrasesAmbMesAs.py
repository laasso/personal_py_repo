selected_letter = 'a'
letter_counter = 0
mostLetter = ''
mostLetter_counter = 0
sentence = ''
exit = False

def inici():
    while not exit:
        printReadSentence()
        printMostLetterSentence()

def printReadSentence():
    global sentence, exit
    sentence = readSentence()
    exit = exitProgramm(sentence)

def readSentence():
    global sentence
    sentence = str(input("Escriu una frase: "))
    return sentence

def printMostLetterSentence():
    global mostLetter, mostLetter_counter,selected_letter
    mostLetter = mostLetterSentence()
    print(f"La frase amb mes {selected_letter} es: {mostLetter}")
    mostLetter_counter = count_letter(mostLetter)
    print(f"Te {mostLetter_counter} {selected_letter}")

def mostLetterSentence():
    global mostLetter
    if count_letter(sentence) >= count_letter(mostLetter):
        mostLetter = sentence
    return mostLetter
    
def count_letter(sentence):
    global letter_counter
    letter_counter = 0
    sentence = convertStrToArray(sentence)
    if len(sentence) > 0:
        for letter in sentence:
            if letter == selected_letter:
                letter_counter = letter_counter + 1
    return letter_counter
        
def convertStrToArray(sentence):
    sentence = ignoreMayusMinus(sentence)
    sentence = list(sentence)
    return sentence

def ignoreMayusMinus(sentence):
    sentence = sentence.casefold()
    return sentence

def exitProgramm(sentence):
    global exit
    if sentence == 'fi':
        exit = True
    return exit

inici()
