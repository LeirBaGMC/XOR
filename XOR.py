def xor(text, key):
    enc = [ord(text[i]) ^ key[i] for i in range(len(text))]
    print("Cifrado:", ''.join(chr(b) for b in enc))

xor("hola", [1, 0, 1, 0])
