valor = float(input("Digite o valor do prêmio da loteria: "))
imposto = valor * 0.07
valornovo = valor - imposto
premioprimeiro = round(valornovo * 0.46, 2)
premiosegundo = round(valornovo * 0.32, 2)
premioterceiro = round(valornovo * 0.22, 2)
print("O prêmio total foi de {}R$, o valor descontado ficou {}R$ e o imposto ficou {}R$".format(valor,valornovo,imposto))
print("O primeiro ganhador ganhou {}R$, o segundo ganhador ganhou {} e o terceiro ganhador ganhou {}R$".format(premioprimeiro,premiosegundo,premioterceiro))