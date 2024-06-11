import os

speed = os.getenv("SPEED")

if speed:
    with open("JOKER.txt", "w") as file:
        file.write(speed)
    os.system("python hamster.py")
else:
    print("متغير SPEED غير معرف في البيئة.")
#speed = @tcrep1
