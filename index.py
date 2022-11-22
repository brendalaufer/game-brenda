# o objetivo é fazer um jogo de embaralha palavra
from random import shuffle, choice

def main():
    temas = {
        0:{
            0:['Ameixa','Amora', 'Banana','Coco''Kiwi'],
            1:['Cereja', 'Goiaba', 'Laranja', 'Limão'],
            2:['Abacate', 'Abacaxi', 'Carambo', 'Caqui']
        },
        1:{
            0:['verde', 'vinho', 'preto'],
            1:['vermelho', 'laranja', 'branco'],
            2:['turquesa', 'castanho', 'azul marinho']
        },
        2:{
            0:['Ceará', 'Bahia', 'Acre'],
            1:['Pernambuco', 'São Paulo', 'Rio de Janeiro'],
            2:['Santa Catarina', 'Tocantins', 'Rondônia']
        }
    }
    frases = ['Não foi dessa vez', 'Vamos lá, mais uma vez', 'Você consegue na próxima', 'Não desista ainda!']

    
    def montar_palavra(temas, tema, dificuldade):
        return choice(temas[tema-1][dificuldade-1])
    

    def embalhar_palavra(palavra):
        palavra_embaralhada = list(palavra.upper())
        shuffle(palavra_embaralhada)
        palavra_embaralhada = ' '.join(palavra_embaralhada)
        return palavra_embaralhada
    

    def tentativas(palavra, frases):
        x, y = 0, 4
        while x < 5:
            tentativa = input('\nDigite Aqui: ')
            if tentativa.lower() == palavra.lower():
                print('\n--- PARABÉNS VOCÊ CONSEGUIU ----')
                break
            else:
                if y > 1:
                    print('\nAinda faltam '+ str(y) +' tentativas\n\n' + choice(frases))
                else:
                    print('\nUltima tentativa\n\n' + choice(frases))
            x += 1
            y -= 1
    
            
    # mostrar para o usuario
    def jogo(temas, frases):
        print('\nBem vindo ao meu jogo com python')

        print('\nEscolha o Tema:')
        print('- 1 Frutas\n- 2 Cores\n- 3 Estados')
        tema = int(input('Digite aqui: [1, 2, 3] '))
        print('\nEscolha a Dificuldade:')
        print('- 1 Fácil\n- 2 Médio\n- 3 Difícil')
        dificuldade = int(input('Digite aqui: [1, 2, 3] '))
        palavra = montar_palavra(temas, tema, dificuldade)
        print('\nTente acertar a palavra embaralhada')
        print('\n---- ' + embalhar_palavra(palavra) + ' ----')
        tentativas(palavra, frases)
        jogar_novamente = input('\nQuer jogar novamente: [S/N] ')
        if jogar_novamente.lower() == 's':
            print('\n'+(40 * '-'))
            main()
        else:
            exit()

    jogo(temas, frases)
main()

