letters = ['a', 'b', 'c', 'd']
out = []

for ch in letters:
    if ch < 'c':
        out.append(ch)
    letters.remove(ch)

size = len(letters) + len(out)
print(size)
print("letters:", letters)
print("out:", out)
