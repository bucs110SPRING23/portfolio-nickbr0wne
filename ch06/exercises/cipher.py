def caesar_cipher(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            start=ord("A")if char.isupper() else ord("a")
            new_pos=(ord(char)-start+shift)%26
            space=","
            char=str(start*new_pos)+space
        result+=char
    return result
phrase=caesar_cipher("THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG",10)
encrypted=open("encrypted.txt","w")
encrypted.write(phrase)