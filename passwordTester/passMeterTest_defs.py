
# Settings
BAR_LESS_VERY_LOW = 10
BAR_LESS_LOW = 50
BAR_LESS_MED = 100
BAR_LESS_STR = 200
BAR_LESS_VERY_STR = 300

def passLenght(pass):
    num = 0
    return num

def passUpperLower(pass):
    num = 0
    return num

def passDigits(pass):
    num = 0
    return num

def passSymbols(pass):
    num = 0
    return num

def passSimple(pass):
    num = 0
    return num
        

def passwordStrength(pass):
    strength = passLenght(pass) + passUpperLower(pass) + passDigits(pass) + passSymbols(pass) - passSimple()
    return strength


def main():

    password = input('Enter Password: ')
    strength = passwordStrength(password)

    if strength < BAR_LESS_VERY_LOW:
        print("Very Weak")
    elif strength < BAR_LESS_LOW:
        print("Weak")
    elif strength < BAR_LESS_LOW:
        print("Medium")
    elif strength < BAR_LESS_LOW:
        print("Strong")
    else:
        print("Very Strong")





main()
