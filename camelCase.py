rawString = input()


def filterString(string):
    return "".join([x for x in string if x.isalnum()])


def formatString(string, i):
    fString = filterString(string)
    out = "".join([fString[0].upper() if i >
                   0 else fString[0].lower(), fString[1:].lower()])
    return out


parsedString = "".join([formatString(e, i)
                       for i, e in enumerate(rawString.split())])

print(parsedString)
