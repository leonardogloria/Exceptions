def exemplo():
    frase = "este é um exemplo"
    if True:
        print(frase)


def dividir(dividendo,divisor):

    if not( (isinstance(dividendo, int)) and isinstance(divisor, int) ):
        raise ValueError("dividir() recebe apenas argumentos inteiros")
        print("true no if do dividir")
    try:
        #print(divisor.resultado) #ERRO FORÇADO (atributo)
        aux = dividendo/divisor
    except:
        print(f"não foi possível dividir {dividendo} por {divisor}")
        raise
        print("entrei no except de dividir()")
    return (aux)


def testa_divisao(dividendo,divisor):

    resultado = dividir(dividendo, divisor)
    # frase = "a divisão de {} por {} é {:0.0f}"
    # print(frase.format( dividendo, divisor, divisao ) )
    print(f"a divisão de {dividendo} por {divisor} é {resultado}")

def arqle_linhas(nomearq, nlin):
    arq = open(nomearq, "r")
    print(arq.readline(nlin))
    arquivo.close()


if (__name__ == "__main__"):
#    exemplo()
    try:
        testa_divisao(5.5,0)
        #arqle_linhas("palavras.txt",10) #ERRO FORÇADO (O arquivo não tem 10 linhas)
    except AttributeError as E: #BOA PRÁTICA
         print(E)
    except ZeroDivisionError as E: #BOA PRÁTICA
         print(E)
    except Exception as E:  # TESTA TODAS AS EXCEÇÕES. Manter abaixo.
        print("tratamento genérico")

    print("Fim do Código")