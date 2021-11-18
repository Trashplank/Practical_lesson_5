input_person = str(input("Текст: "))
keychain = {}

for char in input_person:
    if char in keychain:
        keychain[char] += 1
    else:
        keychain[char] = 1

print(max(keychain))