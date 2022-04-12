# so hacking a Caesar code. Using common words, percentage of them ok,  return the ones that meet the criteria
from sys import argv, exit
from time import time
# from itertools import repeat NO. TOO SLOW

if len(argv) == 2:
    with open(argv[1]) as f:
        s = f.read()
else:
    s = input('Gimme an ecrypted text: ')

one_letter_words   = ('a','i')
two_letter_words  = ('of','to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am')
three_letter_words = ('the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has',
                      'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use')
four_letter_words = ('that', 'with', 'have', 'this', 'will', 'your', 'from', 'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time')
special_words = ('hello', 'world')
total_words = one_letter_words + two_letter_words + three_letter_words + four_letter_words + special_words


def decode(new_try):
    letters = {}
    for i in range(26):
        letters[chr(ord('a')+i)] = chr((ord('a') + (i + new_try) %  26))
    return letters


def decyphering(c): #i as second argument, better not
    #letters = decode(i)
    if c.isupper():
        return letters[c.lower()].upper()
    elif c.isalpha():
        return letters[c]
    return c

def are_actual_words(text):        
    words_in_text = text.lower().split(" ")
    #word_count = list(filter(lambda x: len(x) > 4, words_in_text))
    word_count = []
    words_in_list = []
    for word in words_in_text:
        if len(word) > 3:
            word_count.append(word)
        if word in total_words:
            words_in_list.append(word) 
    #print(words_in_text)
    #words_in_list = list(filter(lambda x: x in total_words, words_in_text))
    #return len(words_in_list) / len(words_in_text)
    return len(words_in_list) / len(words_in_text) > 0.11  # 0.01 false positive, 0.015-0.25 ok, 0.4 false negative


start = time()
for i in range(26):
    letters = decode(i)
    #print(f'i: {-i}\n{letters}\n')
    #repeat(i)
    tithe = int(len(s)*0.1)
    t = ''.join(list(map(decyphering, s[tithe:tithe+750])))
    '''t = ''
    for char in s[tithe:tithe+750]:
        t += decyphering(char)'''

    #rate = are_actual_words(t) 
    #print(f'Rate for code +{26-i} or -{i}:\t\t {rate:.6f}')
    if are_actual_words(t):
        print(f'Code key was either +{26-i} or -{i}\nText below:\n')
        if len(argv) == 2:
            # start2 = time()
            t = ''.join(list(map(decyphering, s))) 
            # whole process with common loop, 0.35 secs, decyphering only 0.34 sec
            # end2 = time()
            # print('time taken2:', end2 - start2) 
            with open('decrypted.txt', 'a') as w:
                #w.write(f'Code key was either +{26-i} or -{i}\nText below:\n')
                w.write(t)
                w.write('\n')
            print(f'Output with code +{26-i} in file decrypted.txt ')        
        else:
            print(t)
        break
         
#hack_caesar_cyphering(s) problem using repeat slows down like hell
end = time()

print('time taken:', end - start)

# note: gives error with special characters: correct that WILL increase time

# hacking with code 2 -> 7 seg, 9 -> 5 segs, 14 -> 4 segs 
# with 750 chars 0.12 segs, 2000 0.25 segs (before optimizing iterations)
# 0.4 rate is nearly constant from 30 to above, what varies are the other, but never goes above 20% of the rate of the real one. F+ spike on 300
# faster
# from m2 disk hdd sata disk: +0.01 secs
# map reduces times in half 0.36 secs vs 0.17 secs
# filter is slower than common if inside for. 750 chars ~ 0.01 sec faster

# last note: decyphering text between       0.15 and 0.16 segs
# looping through the whole loop            0.007 segs             
# it is 5% of the time
# a million texts of 738K would be 7000 segs or almost 2 hours 


        




