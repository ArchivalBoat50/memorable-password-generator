
# Settings
BAR_LESS_VERY_LOW = 10
BAR_LESS_LOW = 50
BAR_LESS_MED = 100
BAR_LESS_STR = 200

# Debug
debug_mod = True

# CONST
NUM_CHAR_MULT = 4

def passLenght(password):
    if debug_mod:
        print(len(password)*NUM_CHAR_MULT)
    return len(password)*NUM_CHAR_MULT

def passLower(password):
    num_of_upper = sum(1 for c in password if c.isupper())
    if debug_mod:
        print((len(password)-num_of_upper)*NUM_CHAR_MULT/2)
    return ((len(password)-num_of_upper)*NUM_CHAR_MULT/2)

def passUpper(password):
    num_of_lower = sum(1 for c in password if c.islower())
    if debug_mod:
          print((len(password)-num_of_lower)*NUM_CHAR_MULT/2)
    return ((len(password)-num_of_lower)*NUM_CHAR_MULT/2)

def passDigits(password):
    num = 0
    return num

def passSymbols(password):
    num = 0
    return num

def passSimple(password):
    num = 0
    return num
        

def passwordStrength(password):
    strength = passLenght(password) + passUpper(password) + passLower(password) + passDigits(password) + passSymbols(password) - passSimple(password)
    return strength


def main():

    password = input('Enter Password: ')
    strength = passwordStrength(password)

    print(strength)

    if strength < BAR_LESS_VERY_LOW:
        print("Very Weak")
    elif strength < BAR_LESS_LOW:
        print("Weak")
    elif strength < BAR_LESS_MED:
        print("Medium")
    elif strength < BAR_LESS_STR:
        print("Strong")
    else:
        print("Very Strong")





main()
