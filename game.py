rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

listaOpcoes = [rock,paper,scissors]
computerChoice = random.choice(listaOpcoes)
# print(computerChoice)
input_user = input("Voce deseja escolher Pedra (R), Papel(P) ou Tesoura (T) ?").upper()
userChoice = ""
if input_user == "R" or input_user == "P" or input_user == "T":
    if input_user == "R":
        userChoice = rock
    elif input_user == "P":
        userChoice = paper
    else:
        userChoice = scissors

else:
    print("Escolha um formato válido")

print(f"O Computador escolheu : \n {computerChoice}")
print(f"Voce escolheu : \n {userChoice}")

if computerChoice == userChoice:
    print("Empataram!")
elif computerChoice == rock:
    if userChoice == paper:
        print("Voce ganhou! ")
    else:
        print("Voce perdeu")
elif computerChoice == paper:
    if userChoice == scissors:
        print("Voce Ganhou!")
    else:
        print("Voce perdeu.")
else:
    if userChoice == rock:
        print("Voce Ganhou!")
    else:
        print("Voce perdeu.")