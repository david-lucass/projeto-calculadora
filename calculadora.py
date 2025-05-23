import os
import time

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

operacao = input("Digite a operação: ").strip().lower()

match operacao:

    case "adicao":
        print("Adição escolhida! ")
        resultado = primeiro_numero + segundo_numero
        print(f"{primeiro_numero} + {segundo_numero} = {resultado}")


    case "subtracao":
        print("Subtração escolhida! ")
        resultado = primeiro_numero - segundo_numero
        print(f"{primeiro_numero} - {segundo_numero} = {resultado}")


    case "multiplicacao":
        print("Multiplicação escolhida! ")
        resultado = primeiro_numero * segundo_numero
        print(f"{primeiro_numero} * {segundo_numero} = {resultado}")


    case "divisao":
        print("Divisão escolhida! ")
        resultado = primeiro_numero / segundo_numero
        if segundo_numero != 0:
            print(f"{primeiro_numero} / {segundo_numero} = {resultado}")
        else:
            print("Não é possivel realizar divisão por 0")
