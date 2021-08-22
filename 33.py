print("Iremos calcular o seu imprestimo imobiliário.")
a=float(input("Digite O valor do imovél:R$"))
b=float(input("Renda do comprador:R$"))
c=float(input("Tempo para quitação:"))
d=float(input("Quantos % será de juros bancário:"))
jur=a/100*d+a
temp=c*12
prest=jur/temp
renda=b/100*30
if renda>prest:
    print("Parabéns seu financiamento foi aprovado e a parcela será de R${:.2f}".format(prest))
else:
    print("Infelizmente a parcela ultrapassa o limite permitido, tente um imóvel com valor inferior.")