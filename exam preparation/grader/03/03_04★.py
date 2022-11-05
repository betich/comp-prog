num = [*str(input())]

if num[:2] in [['0', '6'], ['0', '8'], ['0', '9']] and len(num) == 10:
    print('Mobile number')
else:
    print('Not a mobile number')
