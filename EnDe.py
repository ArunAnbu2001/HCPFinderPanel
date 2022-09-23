import base64
cipherText = ''
plainText = ''
exceptions = ''
def encode(message):
    try:
        cipherText = base64.b64encode(message.encode())
    except Exception as e:
        exceptions = str(e)
        
    return cipherText

def decode(message):
    try:
        plainText = base64.b64decode(message)
    except Exception as e:
        exceptions = str(e)
    
    return plainText.decode()
