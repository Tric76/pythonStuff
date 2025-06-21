from string import ascii_lowercase

#rolling_step = 8

def modeChooser():
    user_choice = ""
    while True:
        user_choice = input("1. Encode \n2. Decode \n3. Quit \nChoice? ")
        if user_choice == "1":
            return "encode"
        elif user_choice == "2":
            return "decode"
        elif user_choice == "3":
            return "quit"
        else:
            print("\nPlease enter 1, 2 or 3.")
         

def is_allowed_string(message):
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.? ")
    return all(char in allowed for char in message)

# wat is regex?

def modeExecution(mode):
    if mode == "encode":
        message = getMessage()
        while True:
            if message is None:
                message = getMessage()

            if len(message) > 500:
                print("\nMessage is too long.")
                message = None  
                continue

            if is_allowed_string(message) == False:
                print("Message to encode can only contain lower case letters and \'.,? \'")
                message = None
                continue

            groupSize = getGroupSize()
            baseNumber = getBaseNumber()
            rollingStep = getRollingStep()

            scr_phrase = messageToNumbers(message.lower(), baseNumber)
            split = split_in_parts(scr_phrase, 2)
            rolling = make_rolling(split, rollingStep)
            split2 = split_in_parts(rolling, groupSize)
            finalMessage = reverseParts(split2)
            revMessage = reverseMessage(finalMessage)

            print("\nEncoded message:"+"\n"+revMessage+"\n")
            break
    elif mode == "decode":
        message = getMessage()
        while True:
            if message is None:
                message = getMessage()
            if not message.isdigit():
                print("\nOnly numeric characters allowed!")
                message = None  # opnieuw om invoer vragen
                continue

            groupSize = getGroupSize()
            baseNumber = getBaseNumber()
            rollingStep = getRollingStep()

            revMessage = reverseMessage(message)
            split2 = split_in_parts(revMessage, groupSize)
            unRevered = reverseParts(split2)
            unSplit = split_in_parts(unRevered, 2)
            notrolling = undo_rolling(unSplit, rollingStep)

            finalMessage = numbersToLetters(notrolling, baseNumber)  
            print("\nDecoded message:"+"\n"+finalMessage+"\n")
            break
    else:
        print("Quit")

def getMessage():
    message = input("\nEnter message: ")
    return(message)

def getGroupSize():
    groupSize = input("\nPlease enter groupsize (2-9, enter=5): ")
    if groupSize.isdigit():
        if 2 <= int(groupSize) <= 9:
            return groupSize
        else:
            groupSize = getGroupSize()    
    elif groupSize == "":
        groupSize = 5
        return groupSize
    else:
        groupSize = getGroupSize()

def getBaseNumber():
    baseNumber = input("\nPlease enter basenumber, e.g. a=10 (10-19, enter=10): ")
    if baseNumber == "":
        baseNumber = 10
    return baseNumber

def getRollingStep():
    rollingStep = input("\nPlease enter steps of rolling code, e.g. a=10 -> a=11 etc (5/9, enter=8): ")
    if rollingStep == "":
        rollingStep = 8
    return rollingStep

#
def makeEncoderTable(baseNumber):
    encoder_table = {}
    number = int(baseNumber)
    #print(type(number))
    for letter in ascii_lowercase:
        encoder_table[letter] = str(number)
        number += 1
    encoder_table[" "] = str(number)
    encoder_table["."] = str(number+1)
    encoder_table[","] = str(number+2)
    encoder_table["?"] = str(number+3)
    return encoder_table

#
def makeDecoderTable(baseNumber):
    x = {}
    number = int(baseNumber)
    for letter in ascii_lowercase:
        x[str(number)] = letter
        number += 1
    x[str(number)] = " "
    number += 1
    x[str(number)] = "."
    number += 1
    x[str(number)] = ","
    number += 1
    x[str(number)] = "?"
    return x

def messageToNumbers(message, baseNumber): # returns string
    encoder_table1 = makeEncoderTable(baseNumber)
    secret_key = str.maketrans(encoder_table1)
    message = message.lower()
    scr_phrase = message.translate(secret_key)
    # print("scr_phrase ", scr_phrase)
    return scr_phrase


def numbersToLetters(message, baseNumber):
    decoder_table1 = makeDecoderTable(baseNumber)
    descrambled = ""
    i = 0
    while i < len(message):
        code = message[i:i+2]  # Neem 2 cijfers
        if code in decoder_table1:
            descrambled += decoder_table1[code]
            i += 2
        else:
        # Als we geen geldige 2-cijfercombinatie vinden, foutafhandeling
            descrambled += '?'
            i += 1  # Ga 1 karakter verder en probeer opnieuw       
    return descrambled

#
def split_in_parts(scr_phrase, groupSize=2): # return list with strings
    groupLength = int(groupSize)
    split_phrase = [scr_phrase[i:i+groupLength] for i in range(0, len(scr_phrase), groupLength)]
    # print("split_phrase ", split_phrase)
    return split_phrase
 
def make_rolling(split_phrase, rollingStep): # return string
    rolling_message = ""
    number = ""
    for i in range(len(split_phrase)):
        number = split_phrase[i]
        value = int(number) + (i // int(rollingStep))
        rolling_message += str(value)
    # print("rolling_message ", rolling_message)
    return rolling_message

def undo_rolling(split_phrase, rollingStep):
    rolling_message = ""
    number = ""
    for i in range(len(split_phrase)):
        number = split_phrase[i]
        value = int(number) - (i // int(rollingStep))
        rolling_message += str(value)   
    return rolling_message

def reverseParts(split_phrase): # pas aan om elke 2e groep te reversen, of elke groep?
    rolling_message = ""
    number = ""
    for i in range(len(split_phrase)):
        number = split_phrase[i]
        value = str(number)[::-1]
        rolling_message += str(value)
    # print(rolling_message)
    return rolling_message

def reverseMessage(message):
    jointMessage = "".join(message)  # Maak één string van de lijst
    revMessage = jointMessage[::-1]  # Keer de hele string om
    # print("revMessage ", revMessage)
    return revMessage


#
#encoder_table1 = makeEncoderTable(baseNumber)
#
#baseNumber = 10
#decoder_table1 = makeDecoderTable(baseNumber)


print("\nUsage: \nMessage to encode can only contain lower case letters and \'.,? \'\nNo numeric characters allowed!\nNo longer then 500 chars.\nMessage to decode will always be a series of numbers.\n")

exit_program = False

while exit_program == False:
    mode = modeChooser()
    modeExecution(mode)
    if mode == "quit":
        exit_program = True


# voeg om de zoveel stappen een oneven aantal cijfers toe (na welke stap?)
# maak groepjes van 3 en reverse deze om en om. Oppakken bij output van makeRolling
# maak daarna groepjes van 5 en reverse deze om en om
# keer alles om