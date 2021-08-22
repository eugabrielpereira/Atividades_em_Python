print("Iremos calcular a sua média, se for maior que 7.0 irá ser aprovado!")
a=float(input("Digite a sua nota no primeiro trimestre:"))
b=float(input("Digite a sua nota no segundo trimestre:"))
media=(a+b)/2
if media>7.0:
    print("Parabéns, você está aprovado com a média de {}".format(media))
else:
    print("Infelizmente você ficou em recuperação, estude bantante e boa sorte.")