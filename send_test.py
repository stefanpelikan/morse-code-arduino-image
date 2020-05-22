from time import time, sleep
from Arduino import Arduino


start_time = time()

message = open("morse_portrait.txt").read()
board = Arduino("115200", port="/dev/cu.SLAB_USBtoUART17")
board.pinMode(13, "OUTPUT")

# while True:
#     board.digitalWrite(13, "LOW")
#     print("low")
#     sleep(1)
#     board.digitalWrite(13, "HIGH")
#     print("high")
#     sleep(1)
while True:
    unit = 1
    # board.digitalWrite(13, "HIGH")
    # sleep(5)
    # board.digitalWrite(13, "LOW")
    # sleep(5)
    board.digitalWrite(13, "LOW")
    for char in message:
        current_time = time() - start_time
        sleep(3*unit)
        if char == "-":
            board.digitalWrite(13, "HIGH")
            sleep(3*unit)
            board.digitalWrite(13, "LOW")
            print(char, current_time)
        elif char == ".":
            board.digitalWrite(13, "HIGH")
            sleep(1*unit)
            board.digitalWrite(13, "LOW")
            print(char, current_time)
        elif char == " ":
            print(char, current_time)
            board.digitalWrite(13, "LOW")
            sleep(6*unit)
            board.digitalWrite(13, "LOW")
    break




# while True
#     board.digitalWrite(13, "HIGH")