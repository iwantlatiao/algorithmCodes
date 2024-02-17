str = input()
index, strLen = 0, len(str)


def getInput():
    global index
    if index < strLen:
        t = str[index]
        index += 1
        return t
    else:
        return "-1"


def getNumber():
    global index
    num = 0
    while "0" <= str[index] and str[index] <= "9" and index < strLen:
        num = (num << 3) + (num << 1) + int(str[index])
        index += 1
    return num


def unzip():
    ch = getInput()
    s = ""
    while ch != "-1":
        if ch == "]":
            return s
        elif ch == "[":
            mul = getNumber()
            tmpStr = unzip()
            s += tmpStr * mul
        else:
            s += ch

        ch = getInput()
    return s


# print(unzip())
import time

startTime = time.time()
unzip()
endTime = time.time()

print("time:{}".format(endTime - startTime))
