"""
This file holds some json functions. I honestly dont know why I put them here instead of in the main file though. 

"""

import json # you'd never guess why im importing this

# updates the json file
def updateJson() -> None:
    with open("settings.json", 'r+') as f:
        data = json.load(f)

        # writes to the start time 
        while True:
            time = input("Countdown time: ")

            try:
                time = int(time)

            except:
                print("invalid number")
                continue

            if time > 0:
                data['sTime'] = time
                break

            else:
                print("do not input negative numbers! please reinput")

        # writes to the start time 
        while True:
            cORg = input("write \'c\' for color mode or \'g\' for group mode! ").lower()

            if cORg == 'c' or cORg == 'g':
                data['mode'] = cORg
                break

            else:
                print(cORg, "is an invalid input!")
        # maybe more here!

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()


# generates a settings json file
def generateSettings():
    # file name
    fileName = 'settings.json'

    with open(fileName, "w") as f:
        defaultDict = {
            "sTime": 5,
            "mode": ' ',
        }
        
        json.dump(defaultDict, f)
        f.close()

    updateJson()
    

    