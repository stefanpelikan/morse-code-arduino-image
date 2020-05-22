from time import time, sleep
from Arduino import Arduino
from math import floor
from random import Random
from pythonosc import udp_client

start_time = time()

last_beep = 0
beep_start_time = 0
gap_start_time = 0
i = 0
unit = 50

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def s_to_ms(t):
     return floor(t * 1000)

def is_time(current_time):
    current_ms = s_to_ms(current_time)
    if (current_ms > interval * time_since_last):
        time_since_last += 1
        return True

def Count_time(start_time):
    # board = Arduino()
    global i
    global last_beep
    global last_space
    global random_int
    global beep_start_time
    global processed_output
    global interval
    global letter_list
    global osc_client
    global MORSE_CODE_DICT
    processed_output = ""
    letter_list = ""
    board = Arduino("115200", port="/dev/cu.SLAB_USBtoUART")
    output_list = [1]
    interval = 100 #miliseconds
    time_since_last = 0
    is_beep = 0

    while True:
        with open("morse_photo2.txt", "a+") as binary_file:
            val = board.analogRead(4)
            osc_client = udp_client.SimpleUDPClient("127.0.0.1", 5005)
            current_time = time() - start_time
            current_ms = s_to_ms(current_time)
            # print(val)
            if (current_ms > interval * time_since_last):
                # print("computing window")
                val_sum = 0
                for val in output_list:
                    val_sum += val
                mean_value = val_sum/(len(output_list))
                # print(mean_value)
                if mean_value < 10:

                    is_beep = 0
                else:

                    is_beep = 1
                parse_window(is_beep, binary_file)
                parse_gap_window(is_beep, binary_file)
                last_beep = is_beep
                output_list = [0]
                time_since_last += 1
            else:
                # return False
                output_list.append(val)


def parse_gap_window(is_beep, output_file):
    global last_beep
    global gap_start_time
    global processed_output
    global inteval
    global osc_client
    global letter_list
    global MORSE_CODE_DICT
    # last_gap = 0
    # print(last_beep, is_beep)
    if is_beep == 0 and last_beep == 1:
        # in_a_gap = True
        gap_start_time = time()
    elif is_beep == 1 and last_beep == 0:
        # in_a_gap = False
        gap_duration = time() - gap_start_time
        # print("gap", gap_duration)
        # print("")
        print("GAP of:", gap_duration)
        # if gap_duration >= 1.8*(interval/100) and gap_duration < 2.1*(interval/100):

        #     print("letter space", gap_duration)
            # print('new_word before osc send', new_word, len(new_word), type(new_word))
            # osc_client.send_message("/string", 1)
            # output_file.write("")
            #register as space between letters, 
            # ie do not write anything to file!!!!!
        if gap_duration >= 2.9*(interval/100) and gap_duration < 12*(interval/100):
            # print("space")
            print("word_space", gap_duration)
            output_file.write(" ")
            print(processed_output)
            if processed_output in MORSE_CODE_DICT.values():             
                new_letter = decrypt(processed_output)
                print(new_letter)
                processed_output = ""
                #         # processed_output = ""
                letter_list += new_letter
                # if len(letter_list) >= 3:
                if letter_list.isdigit() == True:
                    print(letter_list)
                    osc_client.send_message("/string", letter_list)
                    letter_list = ""
                else:
                    print("glitched decoding")
                    print(letter_list)
                    osc_client.send_message("/string", "0")
                    letter_list = ""
            else:
                processed_output = ""

            # print('new_word before osc send', new_word, len(new_word), type(new_word))
            # if len(new_word):





def parse_window(is_beep, output_file):
    global last_beep
    global beep_start_time
    global processed_output
    # print(last_beep, is_beep)
    if is_beep == 1 and last_beep == 0:
        # in_a_beep = True
        beep_start_time = time()
    elif is_beep == 0 and last_beep == 1:
        # in_a_beep = False
        beep_duration = time() - beep_start_time
        # print("beep of:", beep_duration)
        print("BEEEEP of:", beep_duration)
        if beep_duration > .9*(interval/100) and beep_duration < 1.3*(interval/100):
            print("short", beep_duration)
            output_file.write(".")
            processed_output += (".")
        if beep_duration >= 1.8*(interval/100) and beep_duration < 3.2*(interval/100):
            print("long", beep_duration)
            output_file.write("-")
            processed_output += ("-")


def decrypt(message): 

    # extra space added at the end to access the 
    # last morse code 
    message += ' '

    decipher = '' 
    citext = '' 
    for letter in message: 

        # checks for space 
        if (letter != ' '): 

            # counter to keep track of space 
            i = 0

            # storing morse code of a single character 
            citext += letter 

        # in case of space 
        else: 
            # if i = 1 that indicates a new character 
            i += 1

            # if i = 2 that indicates a new word 
            if i == 2 : 

                # adding space to separate words 
                decipher += ' '
            else: 

                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 

    return decipher 


Count_time(start_time)



