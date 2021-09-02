valorReal = float(input("Digite um valor em reais: "))
cotacao = float(input("Digite a cotação atual do dólar: "))
valorDolar = valorReal / cotacao
print("Este mesmo valor em dólares é {}$".format(valorDolar))