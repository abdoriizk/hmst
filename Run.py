# بتعمل اي هنا يخماط 😂😂😂
import os

speed = os.getenv("SPEED")

if speed:
    with open("JOKER.txt", "w") as file:
        file.write(speed)
    os.system("python hamster.py")
else:
    print("فار SPEED غير موجود .")
#speed = @tcrep1
