

import os


def checkWatchdir(dir):
    foundFiles = {}

    for root, dirs, files in os.walk(dir):
        for name in files:
            path = str(root).replace(dir, "")
            foundFiles[name] = path.strip("/")
            print("Found new {}".format(name))
    return foundFiles


def removeEmptyDirs(baseDir):
    emptyDirs = getEmptyDirs(baseDir)
    emptyDirs = orderByDeepestDir(emptyDirs)
    for dir in emptyDirs:
        if len(os.listdir(dir)) == 0:
            os.rmdir(dir)


def getEmptyDirs(baseDir):
    emptyDirs = []
    for root, dirs, files in os.walk(baseDir):
        for dir in dirs:
            path = os.path.join(root, dir)
            emptyDirs.append(path)

    return emptyDirs


def orderByDeepestDir(dirs):
    ordered = {}
    while dirs:
        deep = 0
        dir = dirs[0]
        for char in dir:
            if char == "/":
                deep += 1
        ordered[dir] = deep
        dirs.pop(0)
    ordered = dict(reversed(sorted(ordered.items(), key=lambda item: item[1])))
    return ordered

    # print(path)
    # if len(os.listdir(path)) == 0:
    #     print("Dir is empty")
    # os.rmdir(dir)
