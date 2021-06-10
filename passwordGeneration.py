import os, random, string



list1 = ["The", "Quick", "Brown", "Fox", "and"]

replacements = ( ('a', '@'), ('T', '7'))
# We can use a random  mneumonic sentence generator instead of having a user manually put it in
def mneumonicPass(wordList, complexity):
    letters = [s[0] for s in wordList]
    password = "".join(letters)

    if (complexity == 2):
        print("a")
        return password
    elif (complexity == 3):
        for old, new in replacements:
            password = password.replace(old, new)
        return password
    else:
        return password


def main():
    print(mneumonicPass(list1, 2))
    print(mneumonicPass(list1, 3))

main()