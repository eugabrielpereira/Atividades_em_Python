print("Iremos calcular sua média, iremos solicitar 2 notas:")
a=float(input("Digite a primeira nota:"))
b=float(input("Digite a segunda nota:"))
c=(a+b)/2
if c==4.9 or c<4.9:
    print("Você está reprovado com a média de {}".format(c))
if c>5.0 and c<6.9:
    print("Você está de recuperação com a média de {}".format(c))
if c>7.0:
    print("Parabéns você está aprovado com a média de {}".format(c))