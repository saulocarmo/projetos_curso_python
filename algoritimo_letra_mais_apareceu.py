# frase = 'O Senhor é meu Pastor'\
#     'e nada me faltará, deitar-me faz'\
#         'em verdes pastos, guia-me mansamente '\
#             'por aguas tranquilas.'\

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''

# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue
    
    
#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_apareceu_mais_vezes = letra_atual
        

#     i += 1

# print('A letra que apareceu mais vezes foi a'
#       f'letra    "{letra_apareceu_mais_vezes}" que apareceu '
#       f'{qtd_apareceu_mais_vezes}x')


frase = 'O Senhor é meu Pastor'\
     'e nada me faltará, deitar-me faz'\
         'em verdes pastos, guia-me mansamente '\
            'por aguas tranquilas.' 

i = 0
qtd_vezes_apareceu = 0
letra_mais_apareceu = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ' :
        i += 1
        continue
   

    qtd_vezes_apareceu_atual = frase.count(letra_atual)

    if qtd_vezes_apareceu < qtd_vezes_apareceu_atual:
        qtd_vezes_apareceu = qtd_vezes_apareceu_atual
        letra_mais_apareceu = letra_atual



print('A letra que mais apareceu foi a '
      f'"{letra_mais_apareceu}" que'
      f'      apareceu {qtd_vezes_apareceu}x')
    