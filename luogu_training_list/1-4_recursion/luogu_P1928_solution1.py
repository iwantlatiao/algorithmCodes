def unzip(s):
    s = s.strip("[]")
    digit = 0
    for t in s:
        if "0" <= t and t <= "9":
            digit += 1
        else:
            break
    num = int(s[:digit])
    residualS = s[digit:]
    return residualS * num


str = input()

while True:
    try:
        left = str.rindex("[")
        right = str.index("]", left)
    except:
        break

    zipString = str[left : right + 1]
    str = str.replace(zipString, unzip(zipString))


print(str)
