# started the 17/10/2020 by Frej R. AKA Lustitiae
GlobalLevel = 0
print("Welcome to mou3adel calculator!")
print("Please follow the steps below. Have a nice day! Created by: Lustitiae")
while GlobalLevel not in range(1, 5):
    GlobalLevel = int(input("Please indicate your school global level: "))
if GlobalLevel == 2:
    print(
        "Now indiacte your orientation. Each orientation is related to a number stated below: "
    )
    print(" Science = 1\n ECO = 2\n Lettre = 3\n Info = 4\n")
    orientation = int(input("Please indicate your orientation: "))
elif GlobalLevel > 2:
    print(
        "Now indiacte your orientation. Each orientation is related to a number stated below: "
    )
    print(" Science = 1\n ECO = 2\n Lettre = 3\n Info = 4\n Math = 5\n Technique = 6\n")
    orientation = int(input("Please indicate your orientation: "))


def get_mark(subject):
    mark = None
    while mark is None or mark not in range(20):
        if mark is not None:
            print("Stop lying to me!")
        mark = float(input(f"Insert your {subject} mark here: "))
    print(f"Mark registered: {subject}: {mark}")
    return mark


math = get_mark("math")
science = get_mark("science")
physics = get_mark("physics")
french = get_mark("french")


average_without_dividing = math * 4 + science * 2 + physics * 3 + french * 1.5
average = average_without_dividing / 10.5
print(f"Your average is: {average}")
messages = {
    range(1): "Idk what to say man",
    range(1, 10): "Wake up",
    range(10, 13): "Man you kinda suck",
    range(13, 16): "C'mon you can better than that",
    range(16, 18): "You did a good job mate",
    range(18, 20): "Just reach ou to NASA they'll hire you ",
    (20): "Yeah could have fooled me",
}
for _range, message in messages.items():
    if int(average) in _range:
        print(message)
        break
print("Mou3adel calculator shutting down...")
print("Mou3adel calculator pre-Alpha made by : Lustitiae")
