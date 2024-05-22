"""
Art of the blade path reader main file thing lol

"""

import Solver # forked program. I modified it a little bit, but all the logic in it is written by Acute :)
import time
import json
import jsonHelper
from playsound import playsound

# counts down until its time for the user to start the memory
def countDown(totalTime):
    while totalTime > 5:
        time.sleep(1)
        totalTime -= 1
        # playsound("/assets/tick.mp3")

    time.sleep(1)

    # playsound("5SecondCountdown")

# reads out the memory
def memorySounds(path):
    timePerGap = 0.3 # TODO change this!

    for i in range(len(path)):
        direction = path[i]

        # plays the correct sound
        match direction:
            case 0:
                # playsound("/assets/up.mp3")
                pass
            case 1:
                # playsound("/assets/mid.mp3")
                pass
            case 2:
                # playsound("/assets/down.mp3")
                pass
        
        print(direction)
        
        # waits
        time.sleep(timePerGap)
            
# main function
def main() -> None:
    # implementation for creating a json here!
    try:
        open("settings.json")
    except:
        print("Hello! before you use this program for the first time, please run through the installer!")
        jsonHelper.generateSettings()

    # opens the json
    x = open("settings.json", 'r+')
    data = json.load(x)

    # gets the path
    perms = Solver.findPerms(data['mode'])
    print(perms)
    path = Solver.findPaths(perms)

    # if multiple paths are returned, this will allow the user to set which one they feel most confident in
    if len(path) > 1:
        while True:
            print("since you selected ? at least once, you have multiple options. Please select a path (1 -", len(path) ,")")
            selectedPath = input("path: ")

            try:
                selectedPath = int(selectedPath)
            
            except:
                print("invalid input. please input an integer!")
                continue

            # makes sure the path selected is in range
            if selectedPath > 0 and selectedPath > len(path):
                path = path[selectedPath - 1]
                print("you have succesfully selected path ", selectedPath)
                break

            else:
                print("invalid number. try again!")

    # sets the path to the 100% certain path if theres only 1 thing in the path
    else:
        path = path[0]
    uInput = input("Hit enter to start the timer, or write \'settings\' to edit your settings!")

    if uInput.lower().strip() == 'settings':
        jsonHelper.generateSettings()
        data = json.load(x)
        input("hit enter to start the count down!")

    x.close() # closes fs after settings are over.

    # does the countdown stuff
    countDown(data['sTime'])
    memorySounds(path)
    

# runs main
main()