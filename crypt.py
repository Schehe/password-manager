from sys import argv

if len(argv) == 3:
    code = int(argv[2])
    with open(argv[1], 'r') as f:
        s = f.read()
else:
    s = input('Gimme a text: ')
    while True:
        #code = int(input('Gimme a key code for alphabet chars, from -25 to 25: '))
        if code >= -25 and code <= 25:
            break


# creating a dictionary with the conversions based on the code. upgradeable?
# creating a key: value a: a+code
def encoder_dict(code):
    letters = {}
    for i in range(26):
        letters[chr(ord('a')+i)] = chr((ord('a') + (i + code) %  26))
    return letters


# using cypher dictionary, regarless of lower uppper.
def cyphering(c):
    if c.isupper():
        return letters[c.lower()].upper()
    elif c.isalpha():
        return letters[c]
    return c


#print('Check with this list, temp printing')
letters = encoder_dict(code)
#print(letters, end='\n\n')


#t = [cyphering(c) for c in s]
t = ''.join(list(map(cyphering, s)))

if len(argv) == 3:
    with open('encrypted.txt', 'w') as w:
        w.write(t)
        #print('Output in file encrypted.txt ')        
    

else:
    #print('Your encoded phrase:\n', t)
    return t