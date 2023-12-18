import random

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

numeric_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|',
                      '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']


def enc(plain_text, shift_key):
    cipher_text = ''
    for char in plain_text:
        if char in alphabet_list:
            old_position_index = alphabet_list.index(char)
            new_position_index = (old_position_index + shift_key) % 26
            cipher_text += alphabet_list[new_position_index]
        else:
            cipher_text += char
    print(f'{cipher_text}')


def dec(cipher_text, shift_key):
    plain_text = ''
    for char in cipher_text:
        if char in alphabet_list:
            old_position_index = alphabet_list.index(char)
            new_position_index = (old_position_index - shift_key) % 26
            plain_text += alphabet_list[new_position_index]
        else:
            plain_text += char
    print(f'{plain_text}')


want_to_exit = False
while not want_to_exit:
    enc_dec = input('Type "enc" for encryption or Type "dec" for decryption\n')
    if enc_dec == "enc" or enc_dec == "dec":
        text = input('Type Your Text\n')
        shift = int(input('Type Your Shift_Key\n'))

        if enc_dec == 'enc':
            enc(plain_text=text, shift_key=shift)


        elif enc_dec == 'dec':
            dec(cipher_text=text, shift_key=shift)


        play_again = input('Type "yes" to continue,Type "no" to exit')
        if play_again == 'no':
            want_to_exit = True
            print('Goodbye')
    else:
        print('Type Correct Option Given')
        play_again = input('Type "yes" to continue,Type "no" to exit')
        if play_again == 'no':
            want_to_exit = True
            print('Goodbye')