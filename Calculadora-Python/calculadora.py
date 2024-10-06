import os
import time

def perguntar():
    x = float(input("Digite um número: "))
    y = float(input("Digite um outro número: "))
    return x, y


def somar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    return x / y


def encerrar():
    mensagem = "Encerrando o programa"
    for i in range(4): 
        print(f"\r{mensagem}{'.' * i}", end='', flush=True)
        time.sleep(0.5)

def voltarAoMenu():
    input("Digite qualquer tecla para voltar ao menu: ")
    os.system("cls")



def main():
    while True: 
        print("ℂ 𝔸 𝕃 ℂ 𝕌 𝕃 𝔸 𝔻 𝕆 ℝ 𝔸")

        print("""
Digite 1 para soma
Digite 2 para subtração
Digite 3 para multiplicação
Digite 4 para divisão
Digite 0 para encerrar o programa""")
        opcao = int(input("Digite sua opção: "))

        match opcao:
            case 0:
                os.system("cls")
                encerrar()
                break
            
            case 1:
                x, y = perguntar()
                print(f"Soma de {x} + {y} = {somar(x, y)}")
            
            case 2:
                x, y = perguntar()
                print(f"Subtração de {x} - {y} = {subtrair(x, y)}")

            case 3:
                x, y = perguntar()
                print(f"Multiplicação de {x} * {y} = {multiplicar(x, y)}")
            
            case 4:
                x, y = perguntar()

                if y == 0:
                    print("Impossivel fazer divisão por zero, tente novamente!")
                else:    
                    print(f"Divisão de {x} / {y} = {dividir(x, y)}")

            case _:
                print("Opção invalida, tente novamente!")

        voltarAoMenu()


if __name__ == "__main__":
    main()