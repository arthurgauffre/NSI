def chiffre(message, masque):
    message_chiffre = ''
    for k in range(len(message)):
        message_chiffre += chr(ord(message[k]) ^ ord(masque[k]))
    return message_chiffre

