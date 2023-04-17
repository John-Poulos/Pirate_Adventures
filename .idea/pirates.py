import os
import time
import random

os.system('cls')

print('''

  _              _                                      
 (_|   |   |_/  | |                                     
   |   |   | _  | |  __   __   _  _  _    _    _|_  __  
   |   |   ||/  |/  /    /  \_/ |/ |/ |  |/     |  /  \_
    \_/ \_/ |__/|__/\___/\__/   |  |  |_/|__/   |_/\__/                                                                                    
                                                                        
    
      ___                                    ___                                      o    
  / (_)                    o             / (_)      o                              /    
 |      __,    _ _|_  __,      _  _     |      ,_       _  _  _    ,   __   _  _     ,  
 |     /  |  |/ \_|  /  |  |  / |/ |    |     /  |  |  / |/ |/ |  / \_/  \_/ |/ |   / \_
  \___/\_/|_/|__/ |_/\_/|_/|_/  |  |_/   \___/   |_/|_/  |  |  |_/ \/ \__/   |  |_/  \/ 
            /|                                                                          
            \|                                                                          
            
            
            
######                                     #                                                                  
#     # # #####    ##   ##### ######      # #   #####  #    # ###### #    # ##### #    # #####  ######  ####  
#     # # #    #  #  #    #   #          #   #  #    # #    # #      ##   #   #   #    # #    # #      #      
######  # #    # #    #   #   #####     #     # #    # #    # #####  # #  #   #   #    # #    # #####   ####  
#       # #####  ######   #   #         ####### #    # #    # #      #  # #   #   #    # #####  #           # 
#       # #   #  #    #   #   #         #     # #    #  #  #  #      #   ##   #   #    # #   #  #      #    # 
#       # #    # #    #   #   ######    #     # #####    ##   ###### #    #   #    ####  #    # ######  ####           
                                                                                                                                                                     
''')

fateChosen = 2 #Two is invalid, looking for modulo 2 so either 1 or 0
exitGame = input("Press any key to begin or 'q' to quit.")
if(exitGame == "q"):
    exit()
else:
    os.system('cls')
    fate = int(input('''Roll to set your course and fate....
                You pick up the bones and roll...
                (Choose a number from 1-10): '''))
    plank = 0
    while fate not in range(1,11):
        os.system('cls')
        plank +=1
        if(plank > 1):
            print('''
                You were warned... now walk!!
                You are left alone in the ocean to die.
            ''')
            time.sleep(3)
            exit()
        else:
            fate = int(input('''You fool! The bones don't lie.
                Roll again or walk the plank!!
                (Choose a number from 1-10): '''))

    fateChosen = fate % 2
    print("The die is cast....so be it.")
    time.sleep(3)
    os.system('cls')

match fateChosen:
    case 0:
        os.system('cls')
        print('''       Your crew signals that they have spotted a large castle on the horizon...
        
                                                          !_
                                                          |*~=-.,
                                                          |_,-'`
                                                          |
                                                          |
                                                         /^\\
                           !_                           /   \\
                           |*`~-.,                     /,    \\
                           |.-~^`                     /#"     \\
                           |                        _/##_   _  \_
                      _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
                     [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
                   !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
                   |*`--,_- _        |            |*`~-.,= []  |
                   |.-'|=     []     |   !_       |_.-"`_-     |
                   |   |_=- -        |   |*`~-.,  |  |=_-      |
                  /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
              _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
             [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
              |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
             _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\\
            [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \\
            |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \\
             | _- =-     |-_   | ((* |      |= _=       | -    |___\\
             |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
             | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
             |-_=- _     |=_   =            |=_= -_     |  =   ||+||
             |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
             |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
             |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
             |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
             | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
             |=_ =       | =_-_| |  | |     |   =_      | -_   |
             |_=-_       |=_=  | |  | |     |=_=        |=-    |
        ^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^
        ''')
        castle_choice = int(input(
            '''...the men eye you wearily after being at sea
            What do you do:
                1. Attack and plunder the castle
                2. Set aground close by, but out of range of the castle
                3. Do nothing and sail on            
        '''))
        deadman = 0
        while castle_choice not in range(1,4):
            os.system('cls')
            deadman+=1

            if deadman == 2:
                print('''Your inability to make a choice led to your first mate
                        plunging his boot knife into your heart from behind....
                        you die quickly without seeing your attacker.''')
                time.sleep(3)
                exit()

            else:
                castle_choice = int(input('''The men grow impatient...
              Choose you fool:! 
                    1. Attack and plunder the castle
                    2. Set aground close by, but out of range of the castle
                    3. Do nothing and sail on   
                '''))

        roll_Modifier = 0
        if deadman == 0:
            roll_Modifier = 5
        else:
            roll_Modifier = -5 * deadman

        match castle_choice:

            case 1:
                roll = random.randrange(1,20) + roll_Modifier
                if roll > 15:
                    print('''
                        Your decisive action has taken the castle by suprise!
                        You set fire and sac the castle and surrounding village
                        filling your ship to the point of sinking!
                    ''')
                elif roll == 15:
                    print('''   
                        You manage to escape most of the barrages from the castle wall
                        defenders. You've lost some men, but you manage to storm the castle
                        making off with some loot and licking your wounds. Better luck next time!
                    ''')
                elif roll >= 10 and roll < 15:
                    print('''
                        You've no luck mate... most of the crew is captured or killed in the botched
                        attempt at storming the castle. You've been clapped in irons and await 
                        execution for piracy!
                    ''')
                elif roll < 10:
                    print(''' 
                        A stray salvo blows a hole in the side of the ship, as she list hard to port
                        you are thrown overboard by a loose cannon, crushing you to the depths of Davy Jones'
                        locker...
                    ''')
                    time.sleep(3)
                    exit()


            case 2:
                roll = random.randrange(1,20) + roll_Modifier
                if roll > 12:
                    print('''
                        You come ashore unseen and have found a fresh water supply.
                        You fill your barrels and manage to take some wild game before being spotted
                        by a castle scout. You set sail without incident and the men are happier 
                        for the excursion. Huzzah!  
                    ''')
                else:
                    print(''' 
                        After making landing and doing some minor foraging, you notice the forest grow 
                        quiet... before you can motion to your first mate, you are surronded by the castle
                        guard, muskets drawn and a bevy of archers in the distance... curses..
                        You are clapped in irons and hauled off to the dungeons.
                        ''')


            case 3:
                print(''' 
                    The men grumble, but with water in the hold and some fresh fish caught while circling
                    the island, they are content enough to set sail...
                    ''')

    case 1: #treasure hunt on deserted island? Need lead up - sail into port - tavern --> 1. fight fire map
        # 2. overhear drunken brag about a treasure - buy him drinks / tool him up - confesses he heard it from
        #someone else --> 1. find the other person 2. sit at tavern
        #maybe build story line as functions that can get called to do a better job of randomizing the story?
        print("Todo")
