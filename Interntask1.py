import random
while True:
    print("\n")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    user_selection = int(input("Enter User Selection: "))
    if (user_selection == 1):
        player = "Rock"
    elif (user_selection == 2):
        player = "Paper"
    else:
        player = "Scissors"
    print("\n")
    print("Player throws", player)
    throws = ["Rock", "Paper", "Scissors"]
    ai = random.choice(throws)
    print("AI throws", ai)
    if (player == ai):
        print("Tie Game!")
    elif (player == "Rock"):
        if (ai == "Paper"):
            print("Player Wins!")
        elif (ai == "Scissors"):
            print("Player Wins!")
    elif (player == "Paper"):
        if (ai == "Scissors"):
            print("AI Wins!")
        elif (ai == "Rock"):
            print("Player Wins!")
    elif (player == "Scissors"):
        if (ai == "Rock"):
            print("AI Wins!")
        elif (ai == "Paper"):
            print("Player Wins!")
    print("\n")
    print("1) Play Again")
    print("2) Quit")
    user_selection = int(input("Enter Choice: "))
    if (user_selection == 2):
        print("ThankYou For Playing!!")
        break
    