
def resetQueue(q, n):
    q = [[0, n]]
    return q


def newQueue(q, t):
    if len(q) == 1:
        n = q[0][1]
        q.append([q[0][1], str(t), '0', '0'])
    else:
        n = str(int(q[-1][0]) + 1)
        q.append([n, str(t), '0', '0'])
    print('ticket', n)
    return q


def nextQueue(q):
    q[0][0] += 1
    print('call', q[q[0][0]][0])
    return q


def orderQueue(q, t):
    q[q[0][0]][2] = str(t)
    q[q[0][0]][3] = str(int(q[q[0][0]][2]) - int(q[q[0][0]][1]))
    print('qtime', q[q[0][0]][0], q[q[0][0]][3])
    return q


def avgQT(q):
    print('avg_qtime', float(
        sum(map(lambda x: int(x[3]), q[1:])) / len([x for x in q if len(x) == 4 and x[2] != '0'])))
    return q


def main():
    q = []
    # q = [[indexofcurrentq:int, firstqnumber:str], [qnumber:str, timein:str, timeorder:str, timewait:str], ..]
    commands = []
    # commmands = [[action:str, value:str]]
    commandsdict = {
        'reset': resetQueue,
        'new': newQueue,
        'next': nextQueue,
        'order': orderQueue,
        'avg_qtime': avgQT
    }

    for i in range(int(input())):
        commands.append(str(input()).split())

    # print(commands)
    # print(q)
    for i in commands:
        try:
            q = commandsdict[i[0]](q, i[1])
        except:
            q = commandsdict[i[0]](q)
        # print(q)
    # print(q)


if __name__ == '__main__':
    main()
