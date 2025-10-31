def xor_encryption(text, key):
    encrypted_text = ""
    
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i]))  
    
    return encrypted_text


plain_text = "Educative Accelerates Developer Productivity"
key = "Educative Accelerates Developer Productivity"  

encrypted_text = xor_encryption(plain_text, key)
print(f'Encrypted Text: {encrypted_text}')
