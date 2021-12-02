import random
import os
from unidecode import unidecode
import string

def run(word, under_scores_cadena):
    
    print('¡Adivina la palabra \n {} \n'.format(under_scores_cadena))
    letter = input('Ingresa una letra: ')
    
    while len(letter) == 0 or len(letter) > 1 or string.ascii_lowercase.find(unidecode(letter.lower())) < 0:
        os.system('clear')
        print('Favor de ingresar solo una letra.')
        print('¡Adivina la palabra \n {} \n'.format(under_scores_cadena))
        letter = input('Ingresa una letra: ')
        
    letter = unidecode(letter.upper())
    under_scores = under_scores_cadena.split()
    
    while word.find(letter) >= 0:
        ind = word.find(letter)
        under_scores[ind] = letter
        word = list(word)
        word[ind] = '_'
        word = ''.join(word)

    under_scores = ''.join(under_scores)
    under_scores_cadena = ' '.join(under_scores)
    if under_scores.find('_') < 0 :
        os.system('clear')
        return print('¡Ganaste! La palabra era {}'.format(under_scores))
    else:
        os.system('clear')
        run(word,under_scores_cadena)
    

def words_list():
    #Hay que abrir nuestra base de palabras y guardarla en una lista.
    words = []
    with open('./archivos/data.txt', 'r', encoding='utf-8-sig') as f:
        for linea in f:
            words.append(unidecode(linea.upper().replace('\n','')))
    return words


if __name__=='__main__':
    words = words_list()
    word = random.choice(words)
    large_word = len(word)
    under_scores = []
    
    for us in range(0, large_word):
        under_scores.append('_')
    under_scores_cadena = ' '.join(under_scores)
    os.system('clear')
    run(word,under_scores_cadena)