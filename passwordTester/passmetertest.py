import re

lengthLevel = None                  #Gives relative value for password length (1-  <8, 2-  >=8 & <12, 3- >=12)
charLevel = None                    #Gives relative value for character 'complexity' (1- upper and lower case, 2- upper or lowercase, 3- no letters)
includesDigits = None
lowerRegex = re.compile(r'[a-z]+')      # Regex function for finding lowercase letters
upperRegex = re.compile(r'[A-Z]+')      # Regex function for finding uppercase letters
digitRegex = re.compile(r'[0-9]+')      # Regex function for finding digits

def passwordLength (password):
# Defines relative password length
    if passwordText.len() < 8:
        lengthLevel = 0
    elif passwordText.len() >= 8 and passwordText.len() < 12:
        lengthLevel = 1
    elif passwordText.len() >= 12:
        lengthLevel = 2


def characterCases (password):
#Defines relative password inclusion of letters
    if upperRegex.findall(password) and lowerRegex.findall(password):
        charLevel = 2
    elif upperRegex.findall(password) or lowerRegex.findall(password):
        charLevel = 1
    elif
        print("You have not entered any characters: ")
        charLevel =0

def hasDigits (password):
# Defines if password contains digits
    if digitRegex.findall(password):
        includesDigits = True
    elif
        includesDigits = False


def passwordStrength():

    passwordText = input('Enter Password: ')

    passwordLength(passwordText)
    characterCases(passwordText)
    hasDigits(passwordText)



"""             very_weak        weak    medium      strong
passwordLength   <8              >=8     >=8 & <=12  >=12
upperRegex       yes or          yes     yes         yes
lowerRegex       yes             yes     yes         yes
digitRegex       no              no      yes         yes
"""
