guess = "pursuant"
print("WELCOME TO THE GUESS GAME, WHERE YOU TRY TO GUESS A WORD AND GET ABSOLUTELY NOTHING FOR IT!")
print("Let's start! Enter a total of four words. Remember, the guess word is eight letters long.")
print("Also, make sure two of your words start with a consonant, and the other two with a vowel.")
words = []


def takewords():
    for x in range (4):
        temp = input("Now enter a word!")
        words.append(temp)


takewords()
print("Checking if you followed the instructions...")
consonant = 0
vowel = 0
for y in words:
    if y.startswith(("a","e","i","o","u")):
        vowel += 1
    elif y.startswith(("b", "c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "q", "s", "t", "v", "x", "z", "h", "r", "w", "y")):
        consonant += 1
    else:
        continue

if consonant != 2 or vowel != 2:
    print ("Uh oh! Someone didn't read the instructions well and now they have to rerun the game again!")
    quit()
else:
    print("Seems okay to me! Now searching...")
    points = 0
    index = 0
    for z in words:
        while guess.find(z,index) != -1:
            points += 1
            index +=len(z)

    if points >= 4:
        print("YOU'RE AWESOME! YOU SOMEHOW FOUND MORE THAN 3 SUBSTRINGS!")
    else:
        print("That's not enough... Maybe next time!")



