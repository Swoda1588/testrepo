import vlc
from time import sleep
import os
import math

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

num_to_song = {
    "1": "on_and_on.mp3",
    "2": "good_lookin.mp3",
    "3": "stay_strapped.mp3",
    "4": "spit_in_my_face.mp3",
    "5": "ed.mp3",
    "6": "perfect_girl.mp3",
    "7": "ballin_wrong_neighbourhood.mp3",
    "8": "rose_colored_lenses.mp3",
    "9": "gimme_gimme_gimme.mp3",
    "0": "metamorphesis.mp3",
}

num_to_sound = {
    "1": "prank.mp3",
    "2": "get_back_here.mp3",
    "3": "metal_pipe.mp3",
    "4": "rizz.mp3",
    "5": "avi_screaming.mp3",
    "6": "doioioing.mp3",
    "7": "naaah.mp3",
    "8": "huh.mp3",
    "9": "alarm.mp3",
    "0": "",
}

def log():
    b = input("Enter base.\n#")
    y = input("Enter y")
    print("x = "+str(math.log(int(b), int(y))))

def sin():
    theta = input("Enter theta.\n#")
    print("= "+str(math.sin(int(theta))))

def cos():
    theta = input("Enter theta.\n#")
    print("= "+str(math.cos(int(theta))))

def tan():
    theta = input("Enter theta.\n#")
    print("= "+str(math.tan(int(theta))))

def too_lazy_for_maths():
    os.system("cls")
    print("Choose your operation:")
    print("-------------------------------")
    print("#1 Distance between 2 coordinates")
    print("#2 Midpoint between 2 coordinates")
    print("#3 Linear equations")
    print("#4 Logarithm")
    print("#5 Sine")
    print("#6 Cosine")
    print("#7 Tangent")
    print("#. leave")
    print("-------------------------------")
    operation = input("#")
    if operation == "1":
        distance()
    elif operation == "2":
        midpoint()
    elif operation == "3":
        linear_equation()
    elif operation == "4":
        log()
    elif operation == "5":
        sin()
    elif operation == "6":
        cos()
    elif operation == "7":
        tan()
    elif operation == "2":
        pass
    elif operation == "2":
        pass
    elif operation == "2":
        pass
    elif operation == "2":
        pass
    elif operation == ".":
        main_menu()
    else:
        print("Command not recognised")
        return too_lazy_for_maths()
    return too_lazy_for_maths()
    

def distance():
    os.system("cls")
    x1 = input("x1: ")
    x2 = input("x2: ")
    y1 = input("y1: ")
    y2 = input("y2: ")
    x3 = int(x1) - int(x2)
    y3 = int(y1) - int(y2)
    x3 = x3**2
    y3 = y3**2
    toSquare = x3+y3
    print(toSquare**0.5)
    recurse = input("Input:\n#1?")
    if recurse == "y":
            return distance()
    return too_lazy_for_maths()

def midpoint():
    os.system("cls")
    x1 = input("Enter x1: ")
    x2 = input("Enter x2: ")
    y1 = input("Enter y1: ")
    y2 = input("Enter y2: ")
    x3 = int(x1)+int(x2)
    y3 = int(y1)+int(y2)
    print(f"({int(x3)/2}, {int(y3)/2})")
    recurse = input("Repeat?\n<y/n# ")
    if recurse == "y":
            return midpoint()
    return too_lazy_for_maths()

def linear_equation():
    os.system("cls")
    lin_equation = input("Enter your linear equation in the format [a𝑥+b] where a is the coefficient and b is constant: ")
    ran_x = int(input("Enter the range of 𝑥: "))+1
    coef = lin_equation.split('x')[0]
    print(f"Debug coefficient: {coef}")
    cons = lin_equation.split('+')[1]
    print(f"Debug constant: {cons}")
    #table
    for i in range(1, ran_x):
        y = i*int(coef)+int(cons)
        print(f"If 𝑥 was {i}, 𝑦 would be: {y}")
    recurse = input("Repeat?\n<y/n# ")
    if recurse == "y":
        return midpoint()
    return too_lazy_for_maths()

def nine_11():
    for i in range(0, 10):
        os.system("clear")
        f = open(f'911/{i}.txt', 'r')
        content = f.read()
        print(content)
        f.close()
        sleep(0.2)
    sleep(0.2)
    os.system("clear")
    return calculator()

def calculator():
    operation = input("#")
    if operation == ".":
        return main_menu()
    elif operation == "80085":
        print("You think you're so fucking funny don't you?")
        sleep(0.5)
        print("Little fucking piece of shit.")
        return calculator()
    elif operation == "9/11":
        nine_11()
        return calculator()
    print("= "+str(eval(operation)))
    return calculator()

def tic_tac_toe():
    os.system("cls")
    i = 2
    gameboard = [[" "]*3 for _ in range(3)]
    while True:
        os.system("cls")
        if i % 2:
            sign = "O"
        else:
            sign = "X"
        print(sign)
        print("┌─┬─┬─┐")
        print(f"│{gameboard[0][0]}│{gameboard[0][1]}│{gameboard[0][2]}│")
        print("├─┼─┼─┤")
        print(f"│{gameboard[1][0]}│{gameboard[1][1]}│{gameboard[1][2]}│")
        print("├─┼─┼─┤")
        print(f"│{gameboard[2][0]}│{gameboard[2][1]}│{gameboard[2][2]}│")
        print("└─┴─┴─┘")
        place = input("#")
        if place == "1":
            gameboard[2][0] = sign
        elif place == "2":
            gameboard[2][1] = sign
        elif place == "3":
            gameboard[2][2] = sign
        elif place == "4":
            gameboard[1][0] = sign
        elif place == "5":
            gameboard[1][1] = sign
        elif place == "6":
            gameboard[1][2] = sign
        elif place == "7":
            gameboard[0][0] = sign
        elif place == "8":
            gameboard[0][1] = sign
        elif place == "9":
            gameboard[0][2] = sign
        elif place == ".":
            return main_menu()
        else:
            print("Only enter numbers")
        i+=1

def play_sound(sound):
    os.system("cls")
    p = vlc.MediaPlayer("sounds/"+sound)
    p.play()
    input("Press enter to stop")
    p.stop()
    return soundboard()

def soundboard():
    os.system("cls")
    print("Choose your sound:")
    print("------------------------------------------")
    print("#1 Prank")
    print("#2 Get back here!")
    print("#3 Metal pipe falling")
    print("#4 Rizz")
    print("#5 Avi screaming")
    print("#6 DOIOIOIOIOING")
    print("#7 NAAAAAH")
    print("#8 huh")
    print("#9 Loud alarm")
    print("#0 HEEEEELP")
    print("#. Leave")
    print("------------------------------------------")
    sound_choice = input("#")
    if sound_choice in num_to_sound:
        play_sound(num_to_sound[sound_choice])
    elif sound_choice == ".":
        return main_menu()
    else:
        return soundboard()

def play_song(song):
    os.system("cls")
    global p
    p = vlc.MediaPlayer(song)
    p.play()
    print("Playing:")
    print("======================================")
    print(song)
    print("======================================")
    print("Actions:")
    print("#. Leave")
    print("#/ Leave and stop playing:")
    print("----------------------------------")
    action = input("#")
    if action == ".":
        song_choice()
    elif action == "/":
        p.stop()
        song_choice()

def song_choice():
    os.system("cls")
    print("Choose song:")
    print("------------------------------------------")
    print("#1 On and on")
    print("#2 Good lookin'")
    print("#3 Stay strapped")
    print("#4 Spit in my face")
    print("#5 ED")
    print("#6 Perfect girl")
    print("#7 Ballin' in the wrong neighbourhood")
    print("#8 Rose colored lenses")
    print("#9 Gimme! Gimme! Gimme!")
    print("#10 Metamorphesis")
    print("#11 There's no cock like horse cock")
    print("#12 Spongebob r34")
    print("#. Leave")
    print("#/ Stop playing")
    print("------------------------------------------")
    chosen_song = input("#")
    if chosen_song in nums:
        play_song("songs/"+num_to_song[chosen_song])
    elif chosen_song == ".":
        main_menu()
    elif chosen_song == "/":
        p.stop()
        song_choice()
    else:
        print("Input not recognised.")
        return song_choice()

def main_menu():
    os.system("cls")
    print("Choose function: ")
    print("-----------------------------------")
    print("#1 Operation calculator")
    print("#2 TooLazyForMaths calculator")
    print("#3 Music player")
    print("#4 Aquarium")
    print("#5 idk")
    print("#6 idk")
    print("#7 player tic tac toe")
    print("#8 Soundboard")
    print("#9 idk")
    print("-----------------------------------")
    action = input("#")
    if action == "1":
        os.system("cls")
        print("Enter calculation. Enter *// to leave.")
        calculator()
    elif action == "2":
        too_lazy_for_maths()
    elif action == "3":
        song_choice()
    elif action == "4":
        print("idk")
        return main_menu()
    elif action == "5":
        print("idk")
        return main_menu()
    elif action == "6":
        print("idk")
        return main_menu()
    elif action == "7":
        tic_tac_toe()
    elif action == "8":
        soundboard()
    elif action == "9":
        print("idk")
        return main_menu()
    else:
        print("Command not recognised.\n")
        return main_menu()

main_menu()
