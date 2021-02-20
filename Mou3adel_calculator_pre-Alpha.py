#started the 17/10/2020 by Frej R. AKA Lustitiae
count_average = 0
count = 0
math = 0
science = 0
physics = 0
french = 0
GlobalLevel = 0
while True :
    print("Intialiating Mou3adel calculator...")
    count += 1
    if count >= 3 :
        break
print("Welcome to mou3adel calculator ! Please follow the steps below. Have a nice day ! Created by : Lustitiae")
input("type in anything to continue...")
print("Please write your High school global Level in NUMBERS (example : 1 )")
GlobalLevel_txt = input("Please indicate your school global level  : ")
GloablLevel = int(GlobalLevel_txt)
while GlobalLevel != 1 and GlobalLevel != 2 and  GlobalLevel == 3 a<<    GlobalLevel == 4 or GlobalLevel == 0:
    print("Please indicate your correct global level...")
    GlobalLevel = input("Please indicate your school global level : ")
if  GlobalLevel == 1 :
        print("Good, let's begin")
        average_without_dividing = math * 4 + science * 2 + physics * 3 + french * 1.5
        average = average_without_dividing / 10.5
elif GlobalLevel == 1 or GlobalLevel == 2 :
        print("Now indiacte your orientation. each orientation is related to a number stated below : ")
        print("Science = 1\n ECO = 2\n Lettre = 3\n Info = 4\n")
        orientation = input("Please indicate your orientation : ")
elif GlobalLevel > 2 and GlobalLevel <= 4 :
        print("Now indiacte your orientation. each orientation is related to a number stated below : ")
        print("Science = 1\n ECO = 2\n Lettre = 3\n Info = 4\n Math = 5\n Technique = 6\n  ")

math_txt = input("insert your math mark here : ")
math = float(math_txt)
if  math > 20 or math < 0 :
    print("please write your correct mark")
else :
    print("math mark = " ,math)
    science_txt = input("insert your science mark here : ")
    science = float(science_txt)
if  science > 20 or science < 0 :
    print("please write your correct mark")
    science_txt = input("insert your science mark here : ")
    science = float(science_txt)
else :
    print("science mark = " ,science)
physics_txt = input("insert your physics mark here : ")
physics = float(physics_txt)
if  physics > 20 or physics < 0 :
    print("please write your correct mark")
    physics_txt = input("insert your physics mark here : ")
    physics = float(physics_txt)
else :
    print("physics mark = " , physics)
french_txt = input("insert your french mark here : ")
french = float(french_txt)
if  french > 20 or french < 0 :
    print("please write your correct mark")
    french_txt = input("insert your french mark here : ")
    french = float(french_txt)
else:
    print("french mark = " ,french)
while 3.5 < 5 :
    print("calculating your average...")
    count_average += 1
    if count_average >= 3:
        break
average_without_dividing = math * 4 + science * 2 + physics * 3 + french * 1.5
average = average_without_dividing / 10.5
print("your average is : " ,average)
if  average >= 18 :
    print("Just reach ou to NASA they'll hire you ")
elif average == 20 :
    print("Yeah could have fooled me")
elif  average >= 16 and average < 18 :
    print("you did a good job mate")
elif  average >= 13 and average < 16 :
    print("c'mon you can better than that")
elif  average > 20 :
    print("wow slow down here")
elif  average >= 10 and average < 13 :
    print("man you kinda suck")
elif  average > 0 and average < 10 :
    print("wake up")
elif  average == 0 :
    print("idk what to say man")
print("Mou3adel calculator shutting down...")
print("Mou3adel calculator pre-Alpha made by : Lustitiae")
input("press any key to exit...")
