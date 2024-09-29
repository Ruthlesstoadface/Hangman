import random
try:
    with open('wordlist.10000.txt', 'r') as f:
        wordlist = f.readlines()
except:
    print("Word File Not Found")
    exit()
wrongguess = 0
word = random.choices(wordlist, k = 1)[0]
print("5 wrong guesses and you are out")
def wordFunction(word):
    currentState = []
    for char in word:
        currentState.append({"char":char, "isGuessed":False})
    return currentState

def letterCheck(userLetter, currentState):
    match = False
    for letter in currentState:
        if letter["char"] == userLetter:
            letter["isGuessed"] = True
            match = True
    return match

def printProcess(currentState):
    for letter in currentState:
        if letter["isGuessed"]:
            print(letter["char"], end="")
        else:
            print("_", end="")
    return None



if __name__ == "__main__":
    currentState = wordFunction(word)
    while True:
        guess = 0
        printProcess(currentState)
        userLetter = input(" Your guess:")
        if userLetter == "exit":
            exit()
        elif wrongguess == 5:
            print("You are out")
            print(word)
            exit()
        if letterCheck(userLetter, currentState) == False:
            wrongguess = wrongguess + 1
            print("Wrong Guess: " + str(wrongguess))
        for letter in currentState:
            if letter["isGuessed"] == False:
                guess = guess + 1
        if guess == 0:
            print(" You Win!!!")
            exit()


