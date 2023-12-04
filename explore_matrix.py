#Import libraries
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.legacy import text
from luma.core.legacy.font import TINY_FONT
import time
import threading

#Initialize max7219 device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

INPUT_CHARACTER = "  "

#Device function to display 'ring pattern' via threading
def max_led_pattern():
    global INPUT_CHARACTER


    #Three different scenarios if character is a digit, alpha, or other
    if INPUT_CHARACTER.isdigit():
        numeric_display()
    
    elif INPUT_CHARACTER.isalpha():
        alpha_display()
    else:
        other_display()
    return

def numeric_display():
    matrix_edges = 7
    matrix_start_position = 0
    max_matrix_sleep_seconds = 0.01
    #Top vertical
    for trailing_count in range(matrix_edges):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((matrix_start_position,trailing_count-i), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Left horizontal
    for trailing_count in range(matrix_edges):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((trailing_count-i,matrix_edges), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Bottom vertical
    for trailing_count in range(matrix_edges, -1, -1):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((matrix_edges,trailing_count+i), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Right horizontal
    for trailing_count in range(matrix_edges, -1, -1):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((trailing_count+i,0), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    return

def alpha_display():
    matrix_edges = 7
    matrix_start_position = 0
    max_matrix_sleep_seconds = 0.01
    #Top vertical
    for trailing_count in range(matrix_edges):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((matrix_start_position,0), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Left horizontal
    for trailing_count in range(matrix_edges):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((0,matrix_edges), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Bottom vertical
    for trailing_count in range(matrix_edges, -1, -1):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((matrix_edges,7), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Right horizontal
    for trailing_count in range(matrix_edges, -1, -1):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((7,0), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    return

def other_display():
    matrix_edges = 7
    matrix_start_position = 0
    max_matrix_sleep_seconds = 0.01
    #Top vertical
    for trailing_count in range(matrix_edges):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((matrix_start_position,trailing_count), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Left horizontal
    for trailing_count in range(matrix_edges):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((trailing_count,matrix_edges), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Bottom vertical
    for trailing_count in range(matrix_edges, -1, -1):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((matrix_edges,trailing_count), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    #Right horizontal
    for trailing_count in range(matrix_edges, -1, -1):
            with canvas(device) as draw:
                for i in range(matrix_edges):
                    draw.point((trailing_count,0), fill="white")
                    time.sleep(max_matrix_sleep_seconds)
            character_display()
    return

def character_display():
    #Sleep time for each LED segment
    global INPUT_CHARACTER
    max_function_sleep_seconds = 0.1

    with canvas(device) as draw:
        text(draw, (2, 0), INPUT_CHARACTER, fill="white", font=TINY_FONT)
        time.sleep(max_function_sleep_seconds)


    return

def matrix_thread():
    global INPUT_CHARACTER
    max_function_sleep_seconds = 0.1
    while True:
            
        # with canvas(device) as draw:
        #     text(draw, (2, 0), INPUT_CHARACTER, fill="white", font=TINY_FONT)
        #     time.sleep(max_function_sleep_seconds)

        for trailing_count in range(8):
            for x in range(8):
                with canvas(device) as draw:
                    character_display()
                    max_led_pattern()
    


#Main function
def main():
    threadMaxMatrix = threading.Thread(name='matrix_thread', target = matrix_thread)
    threadMaxMatrix.start()

    while True:
        #Character to be displayed from user input
        #Error checking for a single character
        global INPUT_CHARACTER
        INPUT_CHARACTER = input("Enter a character to display: ")
        if len(INPUT_CHARACTER) > 1:
            print("Error: you must enter a single character (e.g. 'A')")
        #Runs character_display function
    return



main()