a = set(int(a) for a in str(input()).split())
print(len(a), sorted(list(a))[:10], sep='\n')
