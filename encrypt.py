import random

def getKey(quote): #Generates 1to1 key using quote as random seed
    random.seed(quote)
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ""
    for i in range(26):
        n = random.randrange(0, 26-i)
        key += alpha[n]
        alpha = alpha[:(n)] + alpha[(n+1):]
    return key

def encrypt(quote):
    alphadict = {}
    key = getKey(quote)
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        alphadict[alpha[i]] = key[i]
    quote = quote.upper()
    ciphertext = ''
    for char in quote:
        if char in alpha:
            ciphertext += alphadict[char]
        else:
            ciphertext += char
    ciphertext = ciphertext + ' ' * (26 - len(ciphertext) % 26) #adds spaces to end until char count is 0 mod 26
    return ciphertext

def encryptArray(quotes):
    ciphertexts = []
    for quote in quotes:
        ciphertexts.append(encrypt(quote))
    return ciphertexts