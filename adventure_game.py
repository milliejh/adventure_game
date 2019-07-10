import sys
import time
import os

os.system('clear')

# to run this program , open a terminal
# and type "cd code" (you can see what is inside the folder with the command "ls"
# and then type "python3 millies-game.py"

def print_slow(str):
        for char in str:
            time.sleep(.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\n")

print_slow("In the middle of a school, called Ivy Lane School.")
time.sleep(3.0)

print_slow("There was a bench, you were sitting on the bench with your \
sister Libbie sat next to you")
time.sleep(4.0)

print_slow("You saw nobody except from your sister.")
time.sleep(3.0)

print_slow("What action would you like to take player?")
time.sleep (5.0)
print_slow("a.you stay where you are?")
print_slow("b. You look in the car park?")
print_slow("c. You go out of the school to find somebody?")
print_slow("d.You look in the car park and out of school?")

question1 = input("Player select A, B , C or D? ")

if question1 == 'a':
    print_slow("You stand still and it starts to get a bit boring")
    time.sleep(5.0)
    print_slow("GAME OVER")
elif question1 == 'b':
    print_slow("You walked into the car park, and you found a mysterious potion")
elif question1 == 'c':
    print_slow("You went out to the front of the school and saw zombies!")
elif question1 == 'd':
    print_slow("you went  to look in the car park and out of school!")
    time.sleep (5.0)
    print_slow("your on track said your sister you found our citerzens")
    time.sleep(4.0)
    print_slow("a.we can use the misterious potions to turn them back to normal")
    print_slow("b.or we just drink the potion and see what happens")
else:
    print_slow("That is not one of the options!")
    
question2 = input("player select A or B?")

if question2 == 'a':
    print_slow("someting")
elif question2 == 'b':
    print_slow("someting")
else:
    print_slow("That is not one of the options!")

#if you press c then yo  found alot of zombies which were our citerzens
#if you press b you found a potion
#if you press a  you restart the game
#if you press ertyui you found your zombies citerzens and lot's of potins to make the zombies back to normal



