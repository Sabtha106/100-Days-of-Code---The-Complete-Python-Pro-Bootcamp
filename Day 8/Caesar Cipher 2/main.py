alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(text, shift):
    encrypted_text = ''
    alphabet_max_index = len(alphabet) - 1
    for letter in text:
        text_index = alphabet.index(letter)
        encrypted_index = text_index + shift

        #Accommodate last letters shift by shifting the alphabet Z to the begging of the list.
        if encrypted_index > alphabet_max_index:
            shift_diff = encrypted_index - alphabet_max_index
            alphabet_b = alphabet[-1:] + alphabet[:-1]
            encrypted_text += alphabet_b[shift_diff]
        else:
            encrypted_text += alphabet[encrypted_index]

    print(f"Here is the encoded result: {encrypted_text}")


def decrypt(text, shift):
    decrypted_text = ''
    alphabet_max_index = len(alphabet) - 1
    for letter in text:
        text_index = alphabet.index(letter)
        decrypted_index = text_index - shift

        # Accommodate first letters shift by shifting the alphabet A to the end of the list.
        if decrypted_index < 0:
            shift_diff = decrypted_index + alphabet_max_index
            alphabet_b = alphabet.remove(alphabet[0])
            alphabet_b = alphabet.append(alphabet[0])
            decrypted_text += alphabet_b[shift_diff]
        else:
            decrypted_text += alphabet[decrypted_index]

    print(f"Here is the encoded result: {decrypted_text}")
decrypt(text, shift)
encrypt(text, shift)



