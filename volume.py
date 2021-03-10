largura = float(input("Qual a largura ? :"))
altura = float(input("Qual a altura ? :"))
pi = 3.14
volume = 0
farinha =1.66
acucar = 1.18
largura = largura / 2


largura = largura *largura

largura = largura * pi

volume = largura * altura

farinha = volume / farinha
acucar = volume / acucar

print("Volume :", round(volume,2))

print("Peso em gramas Farinha", round(farinha,2))

print("Peso em gramas Açucar", round(acucar,2))
