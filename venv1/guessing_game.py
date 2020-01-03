secret_word = "Giraffe"
guess = ""
limit = 0;
isWin = False
while guess != secret_word and limit < 3:
    guess = raw_input("Enter your guess: ")
    if guess == secret_word:
        isWin = True
    limit += 1;

if isWin:
    print("You Win!!")
else:
    print("You Lose!!")