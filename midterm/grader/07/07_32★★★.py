import re
import string


def case1(p):
    return len(p) >= 8


def case2_1(p):
    a = re.findall(r'[a-z]', p)
    return a != []


def case2_2(p):
    a = re.findall(r'[A-Z]', p)
    return a != []


def case2_3(p):
    a = re.findall(r'[0-9]', p)
    return a != []


def case2_4(p):
    for x in p:
        if x in ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', '"', ';', "'", '<', '>', '?', ',', '.', '/'):
            return True
    return False


def case3(p):
    a = re.findall(r'(.)\1{3,}', p)
    return a == []


def case4(p):
    p = [*p]
    t1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2']
    t2 = t1[:]
    t2.reverse()
    for i in range(len(p) - 3):
        try:
            if p[i:i + 4] == t1[t1.index(p[i]):t1.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t2[t2.index(p[i]):t2.index(p[i]) + 4]:
                return False
        except:
            pass
    return True


def case5(p):
    p = [x.lower() if x in string.ascii_letters else x for x in p]
    t1 = list(string.ascii_lowercase)
    t2 = t1[:]
    t2.reverse()
    for i in range(len(p) - 3):
        try:
            if p[i:i + 4] == t1[t1.index(p[i]):t1.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t2[t2.index(p[i]):t2.index(p[i]) + 4]:
                return False
        except:
            pass
    return True


def case6(p):
    p = [x.lower() if x in string.ascii_letters else x for x in p]
    t1 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    t2 = t1[:]
    t2.reverse()
    t3 = [*'qwertyuiop']
    t4 = t3[:]
    t4.reverse()
    t5 = [*'asdfghjkl']
    t6 = t5[:]
    t6.reverse()
    t7 = [*'zxcvbnm']
    t8 = t7[:]
    t8.reverse()
    for i in range(len(p) - 3):
        try:
            if p[i:i + 4] == t1[t1.index(p[i]):t1.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t2[t2.index(p[i]):t2.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t3[t3.index(p[i]):t3.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t4[t4.index(p[i]):t4.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t5[t5.index(p[i]):t5.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t6[t6.index(p[i]):t6.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t7[t7.index(p[i]):t7.index(p[i]) + 4]:
                return False
        except:
            pass
        try:
            if p[i:i + 4] == t8[t8.index(p[i]):t8.index(p[i]) + 4]:
                return False
        except:
            pass
    return True


def main():
    e = []
    p = str(input()).strip()
    if not case1(p):
        e.append('Less than 8 characters')
    if not case2_1(p):
        e.append('No lowercase letters')
    if not case2_2(p):
        e.append('No uppercase letters')
    if not case2_3(p):
        e.append('No numbers')
    if not case2_4(p):
        e.append('No symbols')
    if not case3(p):
        e.append('Character repetition')
    if not case4(p):
        e.append('Number sequence')
    if not case5(p):
        e.append('Letter sequence')
    if not case6(p):
        e.append('Keyboard pattern')
    if e == []:
        print('OK')
    else:
        for x in e:
            print(x)


if __name__ == '__main__':
    main()
