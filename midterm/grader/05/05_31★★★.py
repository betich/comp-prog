def cut():
    pile[0:len(pile)//2], pile[len(pile) //
                               2:] = pile[len(pile)//2:], pile[0:len(pile)//2],


def shuffle():
    pile[:len(pile):2], pile[1:len(pile):2] = pile[0:len(pile)//2], pile[len(pile) //
                                                                         2:]


pile = str(input()).split()
action = [*filter(lambda x: x in ['C', 'S'], str(input()).replace(' ', ''))]

for i in action:
    {'C': cut, 'S': shuffle}[i]()

print(' '.join(pile))
