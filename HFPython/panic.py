phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

selected = plist[1:3]
selected.extend(plist[-7:-9:-1])
selected.extend(plist[-5:-7:-1])
new_phrase = ''.join(selected)

print(plist)
print(new_phrase)
