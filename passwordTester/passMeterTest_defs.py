import re 
# Settings
BAR_LESS_VERY_LOW = 10
BAR_LESS_LOW = 50
BAR_LESS_MED = 100
BAR_LESS_STR = 200

# Debug
debug_mod = False

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
    return (len(password)-num_of_lower)*NUM_CHAR_MULT/2

def passDigits(password):
    num_of_digits = sum(1 for c in password if c.isdigit())
    if debug_mod:
        print((len(password)-num_of_digits)*NUM_CHAR_MULT/2)
    return (len(password)-num_of_digits)*NUM_CHAR_MULT/2

def passSymbols(password):
    num_of_symbol = len(re.sub('[\w]+' ,'', password))
    if debug_mod:
        print((len(password)-num_of_symbol)*NUM_CHAR_MULT/2)
    return (len(password)-num_of_symbol)*NUM_CHAR_MULT/2

def containsSymbol(password):
   re.findall('[^A-Za-z0-9]',password)
   if (re.findall('[^A-Za-z0-9]',password)):
     return True
   else:
     return False 

def passSimple(password):
    simpleIndex = 0
    containsUpper = bool(re.match(r'\w*[A-Z]\w*', password))
    containsLower = bool(re.match(r'\w*[a-z]\w*', password))
    containsDigit = any(char.isdigit() for char in password)
    if not(containsUpper):
        simpleIndex += 1
    if not(containsLower):
        simpleIndex += 1
    if not(containsDigit):
        simpleIndex += 1
    if not(containsSymbol(password)):
        simpleIndex += 1
    return NUM_CHAR_MULT*simpleIndex
        

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
