S = raw_input()
O = ''
for s in S:
    if s.isupper():
        O += s.lower()
    elif s.islower():
        O += s.upper()
    else:
        O += s
print O
