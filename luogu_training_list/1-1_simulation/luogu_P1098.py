p1, p2, p3 = map(int, input().split())
s = list(input().split()[0])
s_len = len(s)


def isDigit(unkAscii):
    if unkAscii <= ord("9") and ord("0") <= unkAscii:
        return True
    else:
        return False


def isLower(unkAscii):
    if unkAscii <= ord("z") and ord("a") <= unkAscii:
        return True
    else:
        return False


for i in range(s_len):
    if s[i] == "-" and i - 1 >= 0 and i + 1 < s_len:
        leftAscii = ord(s[i - 1])
        rightAscii = ord(s[i + 1])

        if (isDigit(leftAscii) == True and isDigit(rightAscii) == True) or (
            isLower(leftAscii) == True and isLower(rightAscii) == True
        ):  # 左右均为数字或字母
            if leftAscii >= rightAscii:  # 右边的字符小于或等于左边字符 保留减号
                print(s[i], end="")
            elif leftAscii + 1 == rightAscii:  # 减号右边的字符恰好是左边字符的后继
                continue
            else:
                if p1 == 3:  # 填充星号
                    print("*" * (rightAscii - leftAscii - 1) * p2, end="")
                    continue
                elif p1 == 2 and isLower(leftAscii):  # 填充大写字母
                    leftAscii -= 32
                    rightAscii -= 32

                if p3 == 1:  # 正序输出
                    for j in range(leftAscii + 1, rightAscii):
                        print(str(chr(j)) * p2, end="")
                else:
                    for j in range(rightAscii - 1, leftAscii, -1):
                        print(str(chr(j)) * p2, end="")

        else:
            print(s[i], end="")
    else:
        print(s[i], end="")
