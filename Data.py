def opendFileInput(filename):
    file = open(filename)
    fileData = []
    for i in file:
        data = i.rstrip().split()
        fileData.append(data)
    file.close()
    return fileData
def ndfInput(filedata):
    state_start = []
    state_final = []
    states = []
    alphabet = []
    tran = []
    for i in range(len(filedata)):
        if i == 0:
            state_start = filedata[i]
        elif i == 1:
            state_final = filedata[i]
        else:
            states.append(filedata[i][0])
            alphabet.append(filedata[i][1])
            tran.append(filedata[i])

    ndftData = {
        'state_start': state_start,
        'state_final': state_final,
        'states': sorted(set(states)),
        'alphabet': sorted(set(alphabet)),
        'tran': tran
    }
    return ndftData




