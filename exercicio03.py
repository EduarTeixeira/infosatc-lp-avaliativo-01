altura = float(input("Digite a altura da parede que deseja pintar: "))
comprimento = float(input("Digite o comprimento da parede que deseja pintar: "))
area = altura * comprimento
litros = area / 3
qtdLatas = int(litros / 3.6)
valor = round(qtdLatas * 107.00, 2)
print("Você deverá comprar {} lata(s) e pagará {}R$ no total".format(qtdLatas,valor))