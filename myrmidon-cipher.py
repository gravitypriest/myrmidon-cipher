code = 'CQUJHNMTEONERAXDFMIOVPBYOLWXYPXSVZEQGTKRTLED'
cipher = '198449351'
soln = ''
pos = -1

for c in cipher:
    steps = int(c)
    pos = (pos + steps) % len(code)
    soln += code[pos]

print(soln)
