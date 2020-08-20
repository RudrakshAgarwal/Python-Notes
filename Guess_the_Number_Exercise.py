n=18
num_of_guesses=1
print("no. of guesses is limited to 9")
while num_of_guesses<=9:
    guess_num=int(input("enter the guess no.\n"))
    if guess_num<18:
        print("you enter the small no., please try greater no.")
    elif guess_num>18:
        print("you enter the greater no., please try small no.")
    else:
        print("you won the game.")
        print(num_of_guesses, "gusses he took to finish")
        break
    print("no. of guesses left",9-num_of_guesses)
    num_of_guesses +=1
    if num_of_guesses > 9:
        print("you lose \ngame over")
        print("correct number is ", n)

