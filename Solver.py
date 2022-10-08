groups = [[90, 91, 92, 93], [94, 95, 96, 97], [98, 99, 100, 144]] #All of the groups used in the path (split into the three groups of four)

waveGroups = [[[98, 100], [], [99, 144]], [[90, 92], [91], [93]], [[96], [94], [95, 97]],
    [[98,99], [100], [144]], [[92], [90], [91,93]], [[91, 92], [93], [90]], [[144], [99,100], [98]],
    [[94,95], [96], [97]], [[100], [144], [98, 99]], [[97], [95], [94, 96]], [[], [91], [90, 92, 93]],
    [[94,96], [95, 97], []], [[94,97], [96], [95]], [[96], [95], [94, 97]], [[144], [98], [99, 100]],
    [[90,92], [93], [91]]]

def getGroups():

    def colInput():
        while True:
            new = False
            print("\nPlease input the correct color for each group or enter a '?' if you are unsure about the color or enter each possible color followed by a ',' (e.g 'P, B, R')\n")
            fGroupCol = input("Please input the FIRST LETTER of the first color ('P'urple/'B'rown/'R'ed/'M'aroon): ").split(',')
            fGroup = []
            for g in fGroupCol:
                if "?" in g:
                    fGroup = ["90", "91", "92", "93"]
                    break
                elif g.strip().upper() == "P": fGroup.append("90")
                elif g.strip().upper() == "B": fGroup.append("91")
                elif g.strip().upper() == "R": fGroup.append("92")
                elif g.strip().upper() == "M": fGroup.append("93")
                else: 
                    print("An invalid color was entered, please re-enter the color")
                    new = True
                    break
            if new == False:
                break

        while True:
            new = False
            sGroupCol = input("Please input the FIRST LETTER of the second color ('D'ark blue/'S'ilver/'B'lack/'G'rey): ").split(',')
            sGroup = []
            for g in sGroupCol:
                if "?" in g:
                    sGroup = ["94", "95", "96", "97"]
                    break
                elif g.strip().upper() == "D": sGroup.append("94")
                elif g.strip().upper() == "S": sGroup.append("95")
                elif g.strip().upper() == "B": sGroup.append("96")
                elif g.strip().upper() == "G": sGroup.append("97")
                else: 
                    print("An invalid color was entered, please re-enter the color")
                    new = True
                    break
            if new == False:
                break
        
        while True:
            new = False
            lGroupCol = input("Please input the FIRST LETTER of the third color ('R'ed/'B'lue/'Y'ellow/'G'reen): ").split(',')
            lGroup = []
            for g in lGroupCol:
                if "?" in g:
                    lGroup = ["98", "99", "100", "144"]
                    break
                elif g.strip().upper() == "R": lGroup.append("98")
                elif g.strip().upper() == "B": lGroup.append("99")
                elif g.strip().upper() == "Y": lGroup.append("100")
                elif g.strip().upper() == "G": lGroup.append("144")
                else: 
                    print("An invalid color was entered, please re-enter the color")
                    new = True
                    break
            if new == False:
                break

        return [fGroup, sGroup, lGroup]
    
    def groupInput():
        print("\nPlease input the correct group number for each group or enter a '?' if you are unsure about the group or enter each possible group followed by a ',' (e.g '90, 91, 92')\n")
        fGroup = input("Please input the first group (90-93): ").split(',')
        if "?" in fGroup: fGroup = ["90", "91", "92", "93"]
        sGroup = input("Please input the second group (94-97): ").split(',')
        if "?" in sGroup: sGroup = ["94", "95", "96", "97"]
        lGroup = input("Please input the third group (98-100 + 144): ").split(',')
        if "?" in lGroup: lGroup = ["98", "99", "100", "144"]
        return [fGroup, sGroup, lGroup]
    
    while True:
        
        while True:

            getType = input("If you want to enter the colors directly enter 'c', if you want to enter the groups directly enter 'g': ")
            if getType.lower() == 'c': 
                gArr = colInput()
                break
            elif getType.lower() == 'g': 
                gArr = groupInput()
                break
            else: print("\nPlease enter either 'c' or 'g' (without the ')\n")

        #Testing if groups are valid
        new = False

        for g in gArr[0]:
            try: 
                if int(g) not in groups[0]: new = True
            except ValueError: new = True

        for g in gArr[1]:
            try: 
                if int(g) not in groups[1]:new = True
            except ValueError: new = True

        for g in gArr[2]:
            try: 
                if int(g) not in groups[2]: new = True
            except ValueError: new = True
        
        if new: 
            print("\nAn invalid group was entered, please re-enter the groups\n")
            continue 
        else: return gArr

def findPerms():

    gArr = getGroups()

    posGroups = []
    for li in range(len(gArr[2])):
        for si in range(len(gArr[1])):
            for i in range(len(gArr[0])):
                posGroups.append([int(gArr[0][i]), int(gArr[1][si]), int(gArr[2][li])])
    return posGroups

def findPaths(posGroups):

    #Loops through all different permutations of groups entered and returns the correct path in number form for each permutation, each path is stored seperately in the paths array
    #For loop mess can probably be done improved, although it seems to return the values very quickly as is

    print("\nAll possible paths (if multiple groups were entered there will be multiple paths):")
    paths = []
    for groups in posGroups:
        nDirList = []
        for c in waveGroups:
            for r in c:
                for g in groups:
                    if g in r:
                        dir = c.index(r)
                        nDirList.append(dir)
                        continue

        paths.append(nDirList)
        findArrow(nDirList)
    return paths
        
def findArrow(nums):

    #Generates a list of the path given as an argument using arrows (used to display to the user the correct path)

    dirList = []
    for n in nums:
        if n == 0:
            dirList.append("^")
        elif n == 1:
            dirList.append(">")
        elif n == 2:
            dirList.append("v")
    print("".join(dirList))
    input("Press enter to exit...")

# OLD CODE FOR FINDING THE BEST PATH IF MULTIPLE WERE ENTERED (DIDNT WORK)
#
# def findMax(paths):
#     path = []
#     for n in range(15):
#         bestArr = [0, 0, 0]
#         for i in range(len(paths)):
#             c = paths[i][n]
#             bestArr[c] += 1
#         bestN = [0]
#         for n in bestArr:
#             if n > bestN[0]:
#                 bestN = [n]
#             elif n == bestN[0]:
#                 bestN.append(n)
#         if len(bestN) == 1: path.append([bestArr.index(bestN[0])])
#         else:
#             pos = []
#             for i in range(3):
#                 if bestArr[i] == bestN[0]:
#                     pos.append(i)
#             path.append(pos)
#     return path

# def findBest(path):    
#     best = []
#     for c in path:
#         if len(c) > 1: best.append(random.choice(c))
#         else: best.append(c[0])
#     return best

perms = findPerms()
paths = findPaths(perms)
# if len(paths) > 1:
#     # maxPath = findMax(paths)
#     # best = findBest(maxPath)
#     print("\nThe most likely path is: ")
#     findArrow(best)
