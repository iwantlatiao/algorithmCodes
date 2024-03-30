from queue import Queue


rules = []
mapA, mapB = {}, {}


def bfs():
    # (str, num_of_transformation)
    qA, qB = Queue(), Queue()
    qA.put((A, 0)), qB.put((B, 0))
    # 双向 bfs, 当规则有匹配字符串 且 深度 <= 5 才继续搜索
    while qA.empty() == False or qB.empty() == False:
        if qA.empty() == False:
            strA, numA = qA.get()
            for i in range(len(rules)):
                posA = strA.find(rules[i][0])
                while posA != -1:
                    newstrA = strA[:posA] + strA[posA:].replace(
                        rules[i][0], rules[i][1], 1
                    )
                    if mapA.get(newstrA) == None and numA + 1 <= 5:
                        newnumA = numA + 1
                        if mapB.get(newstrA) != None:
                            return newnumA + mapB.get(newstrA)
                        mapA[newstrA] = newnumA
                        qA.put((newstrA, newnumA))
                    posA = strA.find(rules[i][0], posA + 1)

        if qB.empty() == False:
            strB, numB = qB.get()
            for i in range(len(rules)):
                posB = strB.find(rules[i][1])
                while posB != -1:
                    newstrB = strB[:posB] + strB[posB:].replace(
                        rules[i][1], rules[i][0], 1
                    )
                    if mapB.get(newstrB) == None and numB + 1 <= 5:
                        newnumB = numB + 1
                        if mapA.get(newstrB) != None:
                            return newnumB + mapA.get(newstrB)
                        mapB[newstrB] = newnumB
                        qB.put((newstrB, newnumB))
                    posB = strB.find(rules[i][1], posB + 1)

    return -1


if __name__ == "__main__":
    A, B = map(str, input().split())
    mapA[A], mapB[B] = 0, 0

    try:
        while True:
            rules.append(input().split())
    except:
        pass

    step = bfs()

    # print("mapA:")
    # for key in mapA:
    #     print(key, mapA[key])

    # print("mapB:")
    # for key in mapB:
    #     print(key, mapB[key])

    if step == -1:
        print("NO ANSWER!")
    else:
        print(step)
