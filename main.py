# AS07
# Caesar Cipher

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

message = list(input("Input message").lower())
shift = int(input("Input shift"))

for e in range(0, shift):
    a = alphabet[0]
    alphabet.remove(a)
    alphabet.append(a)

for i in range(0, len(message)):
    if message[i] in alphabet:
        b = alphabet.index(message[i])
        message[i] = alphabet[b + shift]

print("".join(message))
