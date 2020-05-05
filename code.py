def caesar():

    plain_text=input("enter message")
    key=int(input("enter number of keys"))
    alphabet="abcdefghijklmnopqrstuvwxyz"
    cipher=""
    for c in plain_text:
        if c in alphabet:
            cipher = cipher + alphabet[(alphabet.index(c) + key) % (len(alphabet))]
    return ("your encrypted message is:"  + cipher)

def caesar2():
    plain_text=input("enter message")
    key=int(input("enter number of keys"))
    alphabet="abcdefghijklmnopqrstuvwxyz"
    cipher=""
    for c in plain_text:
        if c in alphabet:
            cipher = cipher + alphabet[(alphabet.index(c) - key) % (len(alphabet))]
    return ("your decrypted message is:"  + cipher)
