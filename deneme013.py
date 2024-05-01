
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
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
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


the_way_list = ["left", "right", "straight"]
the_way = input("Which way do you want to go? left, right or straight?\n").lower()
the_door_list = ["glass door", "wooden door", "iron door"]
# the_door = input("Which door do you wwant to open? glass door, wooden door or iron door?\n").lower()
the_action_list = ["fight", "run", "hide"]
the_bottle_list = ["red bottle", "blue bottle"]

if the_way == "left":
    print("Well you are in the right way. Now you have to chose a door.")
    the_door = input(" Which door do you want to open? Glass, wooden or iron door?\n").lower()
    if the_door == "wooden door":
        print("You are face to face a monster. Now time to chose a action.")
        the_action = input("Do you want to fight, run or hide?\n").lower()
        if the_action == "fight":
            print("Monster killed you.Game Over.")
        elif the_action == "run":
            print("Monster caught you. Game Over.")
        elif the_action == "hide":
            print( "Good choice.You got over the monster. Now there are two bottles above the tresaure.You have to chose one.")
            the_bottle = input ("Which one do you want to drink? Red or blue?\n").lower()
            if the_bottle =="blue":
                print("""
                                                 ,.        ,.      ,.
                                                 ||        ||      ||  ()
        ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
      //`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
     ||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
      \\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
        `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                                //           .--------.
                            ,-.//          .: : :  :___`.
                            `--'         .'!!:::::  \\_\\ `.
                                    : . /%O!!::::::::\\_\\. \
                                   [""]/%%O!!:::::::::  : . \
                                   |  |%%OO!!::::::::::: : . |
                                   |  |%%OO!!:::::::::::::  :|
                                   |  |%%OO!!!::::::::::::: :|
                          :       .'--`.%%OO!!!:::::::::::: :|
                        : .:     /`.__.'\\%%OO!!!::::::::::::/
                       :    .   /        \\%OO!!!!::::::::::/
                      ,-'``'-. ;          ;%%OO!!!!!!:::::'
                      |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
                      | .   :| |_.','`.`._|  `%%%OO!%%'
                      | . :  | |--'    `--|    `%%%%'       Congragulations.  
                      |`-..-'| ||   | | | |     /__\\`-.
                      \\::::::/ ||)|/|)|)|\\|           /
              ---------`::::'--|._ ~**~ _.|----------( -----------------------
                         )(    |  `-..-'  |           \\    ______
                         )(    |          |,--.       ____/ /  /\\ ,-._.-'
                      ,-')('-. |          |\\`;/   .-()___  :  |`.!,-'`'/`-._
                     (  '  `  )`-._    _.-'|;,|    `-,    \\_\\__\\`,-'>-.,-._
                      `-....-'     ````    `--'      `-._       (`- `-._`-.  """)
            elif the_bottle == "red":
                print("Unfortunately you drank poison. Game Over.")
            else:
                print("That is not a valid answer.Game Over.")



        else:
            print("That is not a valid answer. Game over")
    elif the_door == "glass door":
        print("The glass door is opend to a pool of water. You drowned. Game Over.")
    elif the_door == "iron door":
        print("The iron door is opend to hell. You burned. Game Over.")
    else:
        print("Please enter a valid answer. Game Over.")
elif the_way == "right":
    print ("Again you are in the safe way.Now you have to choose a door to continue the game.")
    the_door = input("Which door do you want to push? Glass, wooden or iron?\n").lower()
    if the_door == "wooden door":
        print("You are in the forest. Be careful there will be some creatures. Now it's time to choose an action.")
        the_action = input("Do you want to fight, run or hide?\n").lower()
        if the_action == "fight":
            print("There was a anaconda didn't you see? You can't fight it. The anaconda has bitten you. Game Over.")
        elif the_action == "hide":
            print("The anaconda has bitten you. Game Over.")
        elif the_action == "run ":
            print("Now you are in safe.You got through it.It's time to drink a bottle to get your treasure.")
            the_bottle = input("Which one do you want to drink? Red or blue?\n").lower()
            if the_bottle == "red":
                print("""                              ||     ||      || ()
      ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-. ||-.,. ,-. ,.,-. ,--.
    //`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
    ||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
     \\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|||| ,-.))
      `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                                //           .--------.
                            ,-.//          .: : :  :___`.
                            `--'         .'!!:::::  \\_\\ `.
                                    : . /%O!!::::::::\\_\\. \
                                   [""]/%%O!!:::::::::  : .  \
                                   |  |%%OO!!::::::::::: : . |
                                   |  |%%OO!!:::::::::::::  :|
                                   |  |%%OO!!!::::::::::::: :|
                          :       .'--`.%%OO!!!:::::::::::: :|
                        : .:     /`.__.'\\%%OO!!!::::::::::::/
                       :    .   /        \\%OO!!!!::::::::::/
                      ,-'``'-. ;          ;%%OO!!!!!!:::::'
                      |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
                      | .   :| |_.','`.`._|  `%%%OO!%%'
                      | . :  | |--'    `--|    `%%%%'           You are the winner. Congratulations!
                      |`-..-'| ||   | | | |     /__\\`-.
                      \\::::::/ ||)|/|)|)|\\|           /
              ---------`::::'--|._ ~**~ _.|----------( -----------------------
                         )(    |  `-..-'  |           \\    ______
                         )(    |          |,--.       ____/ /  /\\ ,-._.-'
                      ,-')('-. |          |\\`;/   .-()___  :  |`.!,-'`'/`-._
                     (  '  `  )`-._    _.-'|;,|    `-,    \\_\\__\\`,-'>-.,-._
                      `-....-'     ````    `--'      `-._       (`- `-._`-. 

              You quenched your thirst and get your treasure. Happy to you.""")
            elif the_bottle == "blue":
                print("You drank poison. Game Over.")
            else:
                print("Please enter a valid answer. Game Over.")
        else:
            print("Please enter a valid answer. Game Over.")

    elif the_door =="glass door":
        print("Well you are okay for a while. There is a bridge in front of you. Now time to choose an action ")
        the_action = input("Do you want to fight, run or hide?\n").lower()
        if the_action == "fight":
            print("Oopps! what a bad choise. Game Over.")
        elif the_action == "hide":
            print("Game Over.")
        elif the_action == "run":
            print \
                ("You are bleeding because of glass. But don't worry there are two bottles, one of them healing you, and then get your treasure.")
            the_bottle = input("Whice bottle do you want to take? Red or blue?\n").lower()
            if the_bottle == "red":
                print("""
                                             ||      ||      ||  ()
    ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
  //`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'-'
  ||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
   \\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,--
      `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                                //           .--------.
                            ,-.//          .: : :  :___`.
                            `--'         .'!!:::::  \\_\\ `.
                                    : . /%O!!::::::::\\_\\. \
                                   [""]/%%O!!:::::::::  : . \
                                   |  |%%OO!!::::::::::: : . |
                                   |  |%%OO!!:::::::::::::  :|
                                   |  |%%OO!!!::::::::::::: :|
                          :       .'--`.%%OO!!!:::::::::::: :|
                        : .:     /`.__.'\\%%OO!!!::::::::::::/
                       :    .   /        \\%OO!!!!::::::::::/
                      ,-'``'-. ;          ;%%OO!!!!!!:::::'
                      |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
                      | .   :| |_.','`.`._|  `%%%OO!%%'
                      | . :  | |--'    `--|    `%%%%'           You are the winner. 
                      |`-..-'| ||   | | | |     /__\\`-.
                      \\::::::/ ||)|/|)|)|\\|           /
              ---------`::::'--|._ ~**~ _.|----------( -----------------------
                         )(    |  `-..-'  |           \\    ______
                         )(    |          |,--.       ____/ /  /\\ ,-._.-'
                      ,-')('-. |          |\\`;/   .-()___  :  |`.!,-'`'/`-._
                     (  '  `  )`-._    _.-'|;,|    `-,    \\_\\__\\`,-'>-.,-._
                      `-....-'     ````    `--'      `-._       (`- `-._`-. 
              You win! Congragulations.""")
            elif the_bottle == "blue":
                print("Oops! You poisened yourself.Game Over.")
            else:
                print("Please enter a valid answer.Game Over.")
        else:
            print("Please enter a valid answer. Game Over.")

    elif the_door == "iron door":
        print("You are in the room of fire. You burned. Game Over.")
    else:
        print("Please enter a valid answer. Game Over.")
elif the_way == "straight":
    print("There was a big hole and you fell into it.Now time to wait for dead.Game Over.")
else:
    print("Give me a valid answer. Game Over.")