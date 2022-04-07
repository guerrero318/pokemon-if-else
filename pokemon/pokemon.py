#!/usr/bin/env python3
import time
import sys
playerName = ""
pokemonChoice = ""
pokemonNickname = ""
nicknameInput = ""

# need to use a stream to get everything in the right place and you also need to flush the stream buffer
def delay(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.05)

print('''                                  
                                  ,',
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|''')


delay("\nHello there! Welcome to the world of POKEMON!")
print()

while playerName == "":
    playerName = input("\nFirst, what is your name?: ").strip().upper()
    delay("\n"f"Right! So your name is {playerName}")
    time.sleep(1)
    print()
    delay("\n"f"{playerName}! Your very own POKEMON legend is about to unfold! \nA world of dreams and adventures with POKEMON awaits! \nLet's go!")
    print()
    time.sleep(1)
    delay("\n"f"Here, {playerName}! There are 3 POKEMON here! Haha! \nThey are inside the POKE BALLS. \nI have only 3 left, but you can have one! \nChoose!")
    print()
while (pokemonChoice != "CHARMANDER" and "SQUIRTLE" and "BULBASAUR" and "25"):
    time.sleep(1)
    pokemonChoice = input("\n"f"Now, {playerName}, which POKEMON do you want?: ").strip().upper()
    time.sleep(1)
    if pokemonChoice == "CHARMANDER":
        delay("\n"f"You have chosen {pokemonChoice}. A fire type POKEMON.")
    elif pokemonChoice == "SQUIRTLE":
        delay("\n"f"You have chosen {pokemonChoice}. A water type POKEMON.")
        break
    elif pokemonChoice == "BULBASAUR":
        delay("\n"f"You have chosen {pokemonChoice}. A grass/poison type POKEMON.")
        break
    elif pokemonChoice == "25":
        pokemonChoice = "PIKACHU"
        delay("\n"f"You have been given {pokemonChoice}. An electric type POKEMON.")
        time.sleep(1.25)
        print()
        delay("\n"f"{pokemonChoice}: PIKA PIKA")
        print()
        time.sleep(1.25)
        delay("\n...")
        print()
        time.sleep(1.25)
        delay("\n"f"Seems like {pokemonChoice} does not like being inside a POKE BALL.")
        break
    else: 
        print("\nSorry, Pokemon entered is not available or has not been discovered yet!")

print()
while nicknameInput == "":
    time.sleep(1)
    nicknameInput = input("\n"f"Would you like to give {pokemonChoice} a nickname? (Y|N): ").strip().lower()
    if nicknameInput == "yes" or nicknameInput == "y":
        time.sleep(1)
        pokemonNickname = input("\nPlease enter desired nickname: ").strip()
        pokemonChoice = pokemonNickname
    else:
        delay("\n"f"{pokemonChoice} has not been given a nickname.")
        pokemonNickname = pokemonChoice
        print()

delay("\n"f"Congratulations! {pokemonNickname} has been registered to your pokedex.")
print()
time.sleep(1)
delay("\n"f"If a wild POKEMON appears, {pokemonNickname} can fight against it!")
print()
time.sleep(1)
print("\n"f"You and {pokemonNickname} are looking great! Take care now!")

