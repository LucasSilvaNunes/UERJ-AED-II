import sympy as sp                                                   # importando e abreviando a biblioteca e suas funções

def Erro(serie, final):                                              # função que calcula o erro envolvido no problema 2-b, usando como base o tratamento de erro passado em aula
    n = sp.symbols('n')                                              # tratamento de n como símbolo
    serie = sp.sympify(serie)                                        # simplificação da série como função
    print(sp.integrate(serie, (n, final, sp.oo)))                    # função de integral que recebe a serie, o simbolo a ser usado, final(limite inferior da integral) e sp.oo(limite superior infinito).
    print('\n')


def LIMITE(seq):                                                     # função utilizada para resolver o exercício 1
    n = sp.symbols('n')                                              # tratamento de n como símbolo
    seq = sp.sympify(seq)                                            # simplificação da sequência como função
    result = sp.limit(seq, n, sp.oo)                                 # variável result guarda o limite da sequência em forma de símbolo algébrico
    if result == sp.oo:                                              # |
        return 'infinito.'                                           # |
    elif result is sp.nan:                                           # |  Tratamento do resultado gerado na operação anterior.
        return 'não existe.'                                         # |
    else:                                                            # |
        return 'o limite da sequência é:{:.2f}'.format(result)       # |

def ESTIMADOR(serie=0):                                              # função utilizada para resolver os problemas da questão 2. O valor default de 0 para a variável série é para o caso de checar somente a resolução da questão 2-a ou 2-c
    n = sp.symbols('n')                                              # tratamento de n como símbolo
    serie = sp.sympify(serie)                                        # simplificação da série como função
    result10 = 0
    result100 = 0
    result1k = 0
    choice = input("Digite 'A' para as somas parciais (10, 100 e 1000) de 1/n**3 (questão 2-a), 'B' para soma infinita da série convergente (questão 2), ou 'C' para resolver a questão 2-b: ")
    if choice.upper() == 'A':
        
        print('A soma parcial de n de 1 a 10: ')                      
        for i in range(1, 11):                                       # esse for resulta na soma parcial de 10 termos da série
            result10 += 1/i**3                                           
        print(result10)                                                  
        print('O erro estimado é de: ')                              
        Erro(1/n**3, 10)                                             # chamada da função de tratamento de erro
        
        
        print('A soma parcial de n de 1 a 100: ')                    # esse for resulta na soma parcial de 100 termos da série
        for i in range(1, 101):
            result100 += 1/i**3
        print(result100)
        print('O erro estimado é de: ')
        Erro(1/n**3, 100)                                            # chamada da função de tratamento de erro
        
        
        print('A soma parcial de n de 1 a 1000: ')                   # esse for resulta na soma parcial de 1000 termos da série
        for i in range(1, 1001):
            result1k += 1/i**3
        print(result1k)
        print('O erro estimado é de: ')
        Erro(1/n**3, 1000)                                           # chamada da função de tratamento de erro
        
    elif choice.upper() == 'B':
        soma = sp.summation(serie,(n, 1, sp.oo)).evalf(5)            # a função summation retorna a soma infinita da série convergente passada como parâmetro na chamada da função e evalf transforma o símbolo gerado em um float
        print('A soma da série é: {}'.format(soma))
        
    elif choice.upper() == 'C':
        aux = 1                                                      # variável a ser acrescida na série
        x = 1.644934                                                 # valor de pi^2/6
        valor = 0                                                    # variável responsável por armazenar as somas feitas
        erro = x - valor                                             # erro que vai dizer quando o while deve parar
        while erro > 1e-6:                                           # quando o erro for menor que a quantidade de 6 casas decimais, o while para
            valor += 1/(aux**2)                                      # somatório
            erro = abs(x - valor)                                    # atualização do cálculo do erro
            aux += 1                                                 # atualização da variável de crescimento
        print("A quantidade de termos necessários é: {}".format(aux))
        
    else:
        print("Digite uma opção válida!")

# QUESTÃO 1:
seq = input("digite sua sequência em termos de n: ")
print(LIMITE(seq))

# QUESTÃO 2:
serie = input("Digite a sua série CONVERGENTE: ")
ESTIMADOR(serie)