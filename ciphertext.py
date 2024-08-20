alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encryption(plain_text,alphabet):
    cipher_text=" "
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=(position+shift)%26
        cipher_text+=alphabet[new_position]
    print(f"the encrpyted code{cipher_text}")
def decryption(cipher_text,shift):
    decrypted_text=" "
    for letter in cipher_text:
        new_letter=alphabet.index(letter)
        text_original=(new_letter-shift)%26
        decrypted_text+=alphabet[text_original]
    print(f"the decrypted code{decrypted_text}")
encryption(text,alphabet)
decryption(text,shift)
        