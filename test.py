crops, tomatoes, delay = [int(i) for i in input().split()]
garden = input()

harvested = len([a for a in garden if int(a) <= delay])

can_make = harvested >= tomatoes

print("YOU_{0}_MAKE_A_SOUP_IN_{1}_DAY{2}".format(
    "CAN" if can_make else "CANNOT", delay, "" if delay <= 1 else "S"))
