print("Iremos analisar sua situação militar.")
a=float(input("Digite o seu ano de nascimento:"))
b=2021-a
faltam=18-b
devendo=b-18
if b<18:
    print("Você ainda é muito jovem, faltam {:.0f} anos para seu alistamento".format(faltam))
else:
    print("Você está pentende {:.0f} anos, aliste-se já.".format(devendo))