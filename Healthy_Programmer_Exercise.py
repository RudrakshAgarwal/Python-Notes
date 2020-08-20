#----------HEALTHY PROGRAMMER-----------

# We all programmers works very hard and some of us sit on chair and do the programming more than 8 hours.
#
# Which causes eyes weeks and we don't drink water or we don't leave the chair which causes back pain in whole day
# which make us unhealthy
#
# To solve this problem I have make a program wich alert us to drink water , eyes exercise , to do physical exericse
# by playing a song for your healthy body
#
# # It will also make saves your log in a file which you enter in the program

#-----------REQUIREMENTS-----------

# python3 and pygame module
#
# File required
# water.mp3 , eyes.mp3 , physical.mp3
#
# How to install pygame module
# Simply you have to only run this command on your terminal or command prompt
#
# pip install pygame

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 10

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")
