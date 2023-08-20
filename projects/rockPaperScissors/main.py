import random
game = {
 "0": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''"",

"1": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

"2" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

print("Welcome to the game 'Rock,Paper,Scissors'")

play = True
while play:

        correctAnswer = True
        choice = ""
        while correctAnswer:
            choice = input("Do you want to play type Y or N: ").upper()
            if(choice == "Y" or choice == "N"):
                correctAnswer = False
        if(choice == "N"):
            break

        optionalList = ['0','1','2']
        playerChoice = ''
        while playerChoice not in optionalList:
            playerChoice = input("Type 0 for Rock , 1 for Paper , 2 for Scissors\n: ")
        pcChoice = str(random.randint(0,2))

        print("\n\n")

        print(f"Your Choice: {game[playerChoice]}")
        print(f"The pc choice: {game[pcChoice]} : {pcChoice}")

        if(playerChoice == "0" and pcChoice == "1"):
            print("You lost!")
        elif (playerChoice == "0" and pcChoice == "2"):
            print("You won!")
        elif(playerChoice == "1" and pcChoice == "0"):
            print("You won!")
        elif(playerChoice == "1" and pcChoice == "2"):
            print("You lost!")
        elif(playerChoice == "2"and pcChoice == "1"):
            print("You won!")
        else:
            print("Remi!")