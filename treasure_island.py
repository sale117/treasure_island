# Function to clear the screen using ANSI escape sequence
def clear_screen():
    print("\033[H\033[J")
# Function to wait for user to press Enter
def press_enter_to_continue():
    input('Press ENTER to continue...')
# Game over art
game_over = ("""               ('-.     _   .-')       ('-.                           (`-.      ('-.  _  .-')   
              ( OO ).-.( '.( OO )_   _(  OO)                        _(OO  )_  _(  OO)( \( -O )  
  ,----.      / . --. / ,--.   ,--.)(,------.       .-'),-----. ,--(_/   ,. \(,------.,------.  
 '  .-./-')   | \-.  \  |   `.'   |  |  .---'      ( OO'  .-.  '\   \   /(__/ |  .---'|   /`. ' 
 |  |_( O- ).-'-'  |  | |         |  |  |          /   |  | |  | \   \ /   /  |  |    |  /  | | 
 |  | .--, \ \| |_.'  | |  |'.'|  | (|  '--.       \_) |  |\|  |  \   '   /, (|  '--. |  |_.' | 
(|  | '. (_/  |  .-.  | |  |   |  |  |  .--'         \ |  | |  |   \     /__) |  .--' |  .  '.' 
 |  '--'  |   |  | |  | |  |   |  |  |  `---.         `'  '-'  '    \   /     |  `---.|  |\  \  
  `------'    `--' `--' `--'   `--'  `------'           `-----'      `-'      `------'`--' '--'""")
# Game start
clear_screen()
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
press_enter_to_continue()
clear_screen()
# Presents you with 3 choices
print('You arrive at the shore of a mysterious island. In front of you are three paths, which path do you take ?')
start_adventure = input('\n# type [left], [right] or [middle]: ').lower()
# Left path
if start_adventure == "left":
    clear_screen()
    print('You encounter a guardian blocking your path. It presents you with a riddle. If you can solve the riddle, the treasure is all yours, but if not...')
    riddle = input('\nI am an odd number. Take away one letter, and I become even.\nWhat number am I ?\n\n# type your answer here: ').lower()
    if riddle == "seven":
        clear_screen()
        print('You win! The treasure is all yours...')
    else:
         clear_screen()
         print('You fail to answer correctly. Suddenly, the ground beneath you opens up, and you fall into a deep pit filled with sharp spikes. As you hit the bottom, your journey comes to a tragic end.\n')
         print(game_over)
# Right path
elif start_adventure == "right":
    clear_screen()
    print('You come to the end of a dark cave. Before you are three doors, barely visible in the dim light filtering through the cave entrance behind you. You must choose one to proceed, although you can`t see where each door leads.')
    choose_door = input('Which door do you choose: [A], [B] or [C]: ').lower()
    if choose_door == "a":
        clear_screen()
        print('Pit Trap: This door opens to reveal a deep pit with sharp spikes at the bottom. You fall into the pit and meet your unfortunate end.\n')
        print(game_over)
    elif choose_door == "b":
        clear_screen()
        print('Fire Trap: As you open the door, flames erupt from the floor and engulf you in a deadly blaze.\n')
        print(game_over)
    elif choose_door =="c":
        clear_screen()
        print('This door leads to the treasure you seek. You win!')
    else:
        clear_screen()
        print('You chose a door that doesn`t exist.')
        print(game_over)
# Middle PATH
else:
    clear_screen()
    print('You find yourself lost in a dense, mysterious forest. The sun is setting, and darkness is beginning to envelop the trees. As you walk deeper into the woods, you realize there is no end in sight. You succumb to the freezing cold and perish alone in the heart of the mysterious forest.\n')
    print(game_over)