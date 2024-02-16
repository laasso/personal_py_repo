selected_letter = 'a'
letter_counter = 0
mostLetter = ''
mostLetter_counter = 0
sentence = ''
exit = False

def inici():
    while not exit:
        printReadSentence()
        readSentence(sentence)

def printReadSentence():
    print("Escriu una frase:")
def readSentence(sentence):
    sentence = str(input)
    return sentence

def printMostLetterSentence(mostLetter, mostLetter_counter):
    print(f"La frase amb mes 'a' es: {mostLetter}")
    mostLetter_counter = count_letter(mostLetter)
    print(f"Te {mostLetter_counter}{selected_letter}")

def mostLetterSentence(sentence,mostLetter, count_letter):
    mostLetter_count = count_letter(mostLetter,selected_letter,letter_counter)
    letter_counter = count_letter(sentence,selected_letter,letter_counter)
    if mostLetter_count < letter_counter:
        mostLetter = sentence
    letter_counter = 0 
    return mostLetter, letter_counter

def count_letter(sentence,selected_letter,letter_counter):
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

def exitProgramm(sentence,exit):
    if sentence == 'fi':
        exit = True
    return exit

inici()