#create string for all letters
plain='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalPositions=len(plain)


#create encryption function to accept message and print coded message
def encryptMessage():
    encrypted=''
    #ask the user for a message
    message=input('Type a message that you want to encrypt: ').upper()
    shift=int(input(f'How many shifts to the right(1-{totalPositions}): '))
    for letter in message:
        if letter in plain:
            position=plain.index(letter)+shift
            if position>totalPositions-1:
                encrypted+=plain[position-totalPositions]
            else:encrypted+=plain[position]
        else:
            encrypted+=letter
    print(f'Your encrypted message: {encrypted}')        

#create decryption function to accept coded message and print original message
def decryptMessage():
    decrypted=''
    #ask the user for a message
    message=input('Type a message that you want to decript: ').upper()
    shift=int(input(f'How many shifts to the right was your encription(1-{totalPositions}): '))
    for letter in message:
        if letter in plain:
            position=plain.index(letter)-shift
            if position>totalPositions+1:
                decrypted+=plain[position+totalPositions]
            else:decrypted+=plain[position]
        else:
            decrypted+=letter
    print(f'Your original message: {decrypted}')        

#ask user if encrypt or decript
choice=input('encrypt or decrypt? ').lower()
if choice=='encrypt':
    encryptMessage()
elif choice=='decript':
    decryptMessage()
else:
    print('wrong! (encrypt/decrypt)')