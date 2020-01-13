import map

def simplifier_main_func(levelfile):
    f = open(levelfile, 'r')
    f = isSurrounded(f)
    f = removeFloor(f)
    toSend = generateSimpleMap(f)
    return toSend


def removeWalls(file_handle): #TODO: Replace mock
    return file_handle

def removeFloor(file_handle): #TODO: Replace mock
    return file_handle

def toSend(file_handle): #TODO: Replace mock
    ret = []
    return ret

def isSurrounded(file_handle):

    if len(set(file_handle[0])) != 1:
        return file_handle
    else:
        wall = file_handle[0][0]

    for line in file_handle:
        if line[0] != wall:
            return file_handle
        if line[-2] != wall: #-1 is \n
            return file_handle

    if len(set(file_handle[-1])) != 1:
        return file_handle
    elif file_handle[-1][0] != wall:
        return file_handle

    return removeWalls(file_handle)
