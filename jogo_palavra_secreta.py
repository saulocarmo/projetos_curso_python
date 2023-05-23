
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta =   'carroceria'
letras_acertadas = ''
numero_tentativas = 0
import os


while True:
    letras_digitadas = input ('Digite uma letra: ')
    numero_tentativas += 1

    if len(letras_digitadas) > 1:
        print('digite apenas uma letra: ')
        continue

    if letras_digitadas in palavra_secreta:
        letras_acertadas += letras_digitadas

    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'    

    print('A Palavra é:',palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS,VOCÊ ACERTOU !!') 
        print('A palavra secreta é:',palavra_secreta)
        print('Tentativas:', numero_tentativas)
        break
     



  
    

