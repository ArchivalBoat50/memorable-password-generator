# IMPORTS:
from random import randint

# CONSTANTS:
# Additional settings:
# UPPERCASE_MAX = 2/3     # Should be in the range from 1 (100%) to 0 (0%)

# Special number code
I_CHANGER_L = '1'
I_CHANGER_U = '!'

# Special character code
A_CHANGER_L = '^'
A_CHANGER_U = '@'
S_CHANGER_L = '$$'
S_CHANGER_U = '$$'

### TODO: CONVERT SPECIAL CODE TO TUPPLE

# GLOBAL VARIABLES:
# A list of most common words in English (Just for illustration purposes)
list_of_words = ['time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world', 'life', 'hand', 'part', 'child', 'eye', 'woman', 'place', 'work', 'week', 'case', 'point', 'government',
    'company', 'number', 'group', 'problem', 'fact']
user_list = []

# Complexity of the password:
    # 1 - 
    # 2 - 
    # 3 - 
complexity = 1

# Generation settings:
is_uppercase = True
is_lowercase = True
is_number = True
is_symbols = True
pass_length = 12 


# FUNCTION:
# Converts random characters in a string to uppercase
def toUpper(in_str):

     # TO BE RETURNED
    out_str = ''

    for letter in in_str:

        if (randint(0, 100)) % 2 == 0:
            out_str += letter
        else:
            out_str += letter.upper()
            
    return out_str

# FUNCTION:
# Converts special characters to numbers
def addNumbers(in_str):

     # TO BE RETURNED
    out_str = ''

    for letter in in_str:

        # Number Code
        if letter == 'i':
            out_str += I_CHANGER_L
        else:
            out_str += letter
            
    return out_str

# FUNCTION:
# Converts special characters to numbers
def addSymbols(in_str):

     # TO BE RETURNED
    out_str = ''

    for letter in in_str:

        # Character Code
        if letter == 'I':
            out_str += I_CHANGER_L
        elif letter == 'a':
            out_str += A_CHANGER_L
        elif letter == 'A':
            out_str += A_CHANGER_U
        elif letter == 's':
            out_str += S_CHANGER_L
        elif letter == 'S':
            out_str += S_CHANGER_U
        else:
            out_str += letter
            
    return out_str
    

# FUNCTION:
# Generates the password based on words
# TONOTE: All words in the list form should be lowercase
def generatePass():

    # Local variables:
    pass_str = ''

    # Randomly choose 2-3 word
    rand_pass_len = randint(2, 5)

    # Creates a password from words
    for i in range(rand_pass_len):
        # Randomly choose a words
        if (randint(0, 100)) % 2 == 0:
            pass_str = pass_str + user_list[randint(0, len(user_list)-1)]
        else:
           pass_str = pass_str + list_of_words[randint(0, len(list_of_words)-1)]

    # Add uppercase at random
    if is_uppercase:
        pass_str = toUpper(pass_str)

    # Add numbers at random
    if is_number:
        pass_str = addNumbers(pass_str)
    
    # Add numbers at random
    if is_symbols:
        pass_str = addSymbols(pass_str)

    return pass_str

# MAIN:
def main():

    print("Please enter real words, as there is no error detection.")

    u_in = '_'
    while(u_in != ''):
        print("Enter empty string to skip...")
        u_in = input("Please enter a word for password generation: ")
        user_list.append(u_in)

    pass_str = ''
    while(len(pass_str) != pass_length):
        pass_str = generatePass()
    print(pass_str)

# RUN:
main()
