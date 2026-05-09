# encryption and decryption

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encryption(plain_text,shift_num):
    cipher_text = ""
    for i in text:
        if i in alphabets:
            position = alphabets.index(i)
            new_position = ((position + shift_num)%52)
            cipher_text += alphabets[new_position]
        else:
            cipher_text += i
    print("the cipher text of the text is ",cipher_text)
    
def decryption(cipher_text,shift_num):
    plain_text = ""
    for i in text:
        if i in alphabets:
            position = alphabets.index(i)
            new_position = ((position - shift_num)%52)
            plain_text += alphabets[new_position]
        else:
            plain_text += i
    print("the cipher text of the text is ",plain_text)

end = False
while not end:
    n = input("enter '0' for encryption, '1' for decryption:\n ")
    text = input("Enter the text: ")
    shift = int(input("Enter the shift number: "))
    if n == '0':
        encryption(plain_text = text,shift_num = shift)
    elif n == '1':
        decryption(cipher_text = text,shift_num = shift)
    a = input("enter 'c' to continue, 'e' to exit:\n ")
    if a == 'e':
        end = True
        print("Goodbye!")
    