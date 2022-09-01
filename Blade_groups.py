#groups = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 144]
import random

waveGroups = [[[98, 100], [], [99, 144]], [[90, 92], [91], [93]], [[96], [94], [95, 97]],
    [[98,99], [100], [144]], [[92], [90], [91,93]], [[91, 92], [93], [90]], [[144], [99,100], [98]],
    [[94,95], [96], [97]], [[100], [144], [98, 99]], [[97], [95], [94, 96]], [[], [91], [90, 92, 93]],
    [[94,96], [95, 97], []], [[94,97], [96], [95]], [[96], [95], [94, 97]], [[144], [98], [99, 100]],
    [[90,92], [93], [91]]]

def findPerms():

    print("Please input each group number, if theres multiple seperate each number with a comma.")
    fGroup = input("Please input the first group (90-93): ").split(',')
    sGroup = input("Please input the second group (94-97): ").split(',')
    lGroup = input("Please input the third group (98-100 + 144): ").split(',')

    posGroups = []
    for li in range(len(lGroup)):
        for si in range(len(sGroup)):
            for i in range(len(fGroup)):
                posGroups.append([int(fGroup[i]), int(sGroup[si]), int(lGroup[li])])
    return posGroups

def findPaths(posGroups):
    print("\nAll possible permutations:")
    paths = []
    for groups in posGroups:
        nDirList = []
        #sDirList = []
        for c in waveGroups:
            for r in c:
                for g in groups:
                    if g in r:
                        dir = c.index(r)
                        nDirList.append(dir)
                        #sDirList.append(str(dir))
                        continue

        paths.append(nDirList)
        #print("List in number form (0=up, 1=middle, 2=bottom): " + " ".join(sDirList))
        findArrow(nDirList)
    return paths
        
def findArrow(nums):
    dirList = []
    for n in nums:
        if n == 0:
            dirList.append("^")
        elif n == 1:
            dirList.append(">")
        elif n == 2:
            dirList.append("v")
    print("List in arrow form: " + "".join(dirList))

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
