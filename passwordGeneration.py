# Example sentence list
list1 = ["The", "Quick", "Brown", "Fox", "Jumped", "Above", "The", "Fence"]

replacements2 = (('A', '@'), ('B', '8'))
replacements3 = ( ('a', '@'), ('T', '7'), ('A', '@'), ('B', '8'), ('F', 'Ph'))
# The higher the complexity, the more possible character replacements there are for the mnemonic password
def mneumonicPass(wordList, complexity):
    letters = [s[0] for s in wordList]
    password = "".join(letters)

    if (complexity == 2):
        for old, new in replacements2:
            password = password.replace(old, new)
        return password
    elif (complexity == 3):
        for old, new in replacements3:
            password = password.replace(old, new)
        return password
    else:
        return password


def main():
    print("Complexity of 1")
    print(mneumonicPass(list1, 1), "\n")
    print("Complexity of 2")
    print(mneumonicPass(list1, 2), "\n")
    print("Complexity of 3")
    print(mneumonicPass(list1, 3))

main()
