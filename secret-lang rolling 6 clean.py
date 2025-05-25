from string import ascii_lowercase

rolling_step = 8

def mode_choice():
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
    allowed = set("abcdefghijklmnopqrstuvwxyz,.? ")
    return all(char in allowed for char in message)

def selectMode(mode):
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

            scr_phrase = encode(message)
            split = split_in_parts(scr_phrase)
            rolling = make_rolling(split)
            print("\nEncoded message:"+"\n"+rolling+"\n")
            break
    elif mode == "decode":
        message = getMessage()
        while True:
            if message is None:
                message = getMessage()
            if not message.isdigit():
                print("\nOnly numeric characters allowed!")
                message = None
                continue
            split = split_in_parts(message)
            notrolling = undo_rolling(split)
            descrambled = decode(notrolling)  
            print("\nDecoded message:"+"\n"+descrambled+"\n")
            break
    else:
        print("Quit")

def getMessage():
    message = input("\nEnter message: ")
    return(message)

def make_encoder_table(min_value):
    encoder_table = {}
    number = min_value
    for letter in ascii_lowercase:
        encoder_table[letter] = str(number)
        number += 1
    encoder_table[" "] = str(number)
    encoder_table["."] = str(number+1)
    encoder_table[","] = str(number+2)
    encoder_table["?"] = str(number+3)
    return encoder_table

def make_decoder_table(min_value):
    x = {}
    number = min_value
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

def encode(message):
    secret_key = str.maketrans(encoder_table1)
    message = message.lower()
    scr_phrase = message.translate(secret_key)
    return scr_phrase

def decode(message):    
    descrambled = ""
    i = 0
    while i < len(message):
        code = message[i:i+2] 
        if code in decoder_table1:
            descrambled += decoder_table1[code]
            i += 2
        else:
            descrambled += '?'
            i += 1
    return descrambled

def split_in_parts(scr_phrase):
    group_length = 2
    split_phrase = [int(scr_phrase[i:i+group_length]) for i in range(0, len(scr_phrase), group_length)]
    return split_phrase
 
def make_rolling(split_phrase):
    rolling_message = ""
    number = ""
    for i in range(len(split_phrase)):
        number = split_phrase[i]
        value = number + (i // rolling_step)
        rolling_message += str(value)
    return rolling_message

def undo_rolling(split_phrase):
    rolling_message = ""
    number = ""
    for i in range(len(split_phrase)):
        number = split_phrase[i]
        value = number - (i // rolling_step)
        rolling_message += str(value)
    return rolling_message



encoder_table1 = make_encoder_table(10)

decoder_table1 = make_decoder_table(10)


print("\nUsage: \nMessage to encode can only contain lower case letters and \'.,? \'\nNo numeric characters allowed!\nNo longer then 500 chars.\nMessage to decode will always be a series of numbers.\n")

exit_program = False

while exit_program == False:
    mode = mode_choice()
    selectMode(mode)
    if mode == "quit":
        exit_program = True