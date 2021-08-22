print("Controle de tráfego terrestre. A velocidade da via é de 80km/h e será cobrado R$5,00 a cada km/h acima da velocidade permitida.")
a=float(input("Digite a velocidade do carro KM/H:"))
b=(a-80)*5
if a>80:
    multa=print("O valor da sua multa é de R${:.2f}".format(b))
else:
    print("Parabéns você está dentro do limite permitido")