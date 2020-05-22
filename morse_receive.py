from time import time, sleep
from Arduino import Arduino
from math import floor
from pythonosc import udp_client

start_time = time()

last_beep = 0
time_unit = 25
threshold = 15
beep_start_time = 0
gap_start_time = 0

letter_space_lower = 3.1
letter_space_higher = 1.1
space_lower = 6.1
space_higher = 0

dot_lower = .8
dot_higher = 1.2
dash_lower = 2.8
dash_higher = 3.5

def s_to_ms(t):
     return floor(t * 1000)

def is_time(current_time):
    current_ms = s_to_ms(current_time)
    if (current_ms > interval * time_since_last):
        time_since_last += 1
        return True

def receive(start_time):
    # board = Arduino()
    global last_beep
    global beep_start_time
    global last_gap
    global gap_start_time
    board = Arduino("9600", port="/dev/cu.SLAB_USBtoUART")
    output_list = [1]
    processed_output_list = [0]
    interval = 50
    time_since_last = 0
    sig_bool = 0
    last_gap = 0

    while True:
        val = board.analogRead(3)
        # with open("morse_readings1.txt", "a+") as binary_file:
        current_time = time() - start_time
        # is_window_over = is_time(current_time)
        current_ms = s_to_ms(current_time)

        if (current_ms > interval * time_since_last):
            # print("computing window")
            val_sum = 0
            for val in output_list:
                val_sum += val
            mean_value = val_sum/(len(output_list))
            if mean_value < 15:
                # print("window is 0")
                sig_bool = 0
                parse_gap_window(sig_bool)
                # print("setting last beep to ", sig_bool)
                last_gap = sig_bool
                last_beep = sig_bool
                # print(last_gap)

            else:ffff
                # print("window is 1")
                # print(time_since_last, current_time, mean_value, "BEEEEEEEEEEEP")
                sig_bool = 1

                last_gap = sig_bool
            output_list = [0]
            time_since_last += 1
            # print(last_beep)a
        else:
            # return False
            output_list.append(val)
                # print(output_list)
        parse_beep_window(sig_bool)
        last_beep = sig_bool


def parse_gap_window(sig_bool):
    global last_gap
    global gap_start_time
    # last_gap = 0
    # print(last_gap, sig_bool)
    if sig_bool == 0 and last_gap == 1:
        # in_a_gap = True
        gap_start_time = time()
    if sig_bool == 1 and last_gap == 0:
        # in_a_gap = False
        gap_duration = time() - gap_start_time
        print(gap_duration)
        # if gap_duration >= letter_space_lower*time_unit and gap_duration < letter_space_higher*time_unit:
        #     print("|")
        #     #register as space between letters, 
        #     # ie do not write anything to file!!!!!
        # if gap_duration > space_lower*time_unit:
        #     print(" ")

            # output_file.write(" ")
            #write a space to the file, like " "
def parse_beep_window(sig_bool):
    global last_beep
    global beep_start_time
    # print(last_beep, sig_bool)
    if sig_bool == 1 and last_beep == 0:
        print("enter beep")
        beep_start_time = time()
    if sig_bool == 0 and last_beep == 1:
        print("exit beep")
        beep_duration = time() - beep_start_time
        print(beep_duration)
        # if beep_duration > dot_lower*time_unit and beep_duration < dot_higher*time_unit:
        #     # output_file.write(".")
        #     print(".")
        #     # client = udp_client.SimpleUDPClient(args.ip, args.port)
        # if beep_duration > dash_lower*time_unit and beep_duration < dash_higher*time_unit:
        #     print("-")
        #     # output_file.write("-")
        #     # client = udp_client.SimpleUDPClient(args.ip, args.port)



receive(start_time)

