print("promoção exclusiva para o Dia da Mulher")
a=input("Digite o seu nome:")
print("Para Masculino digite:2 / Para feminino digite:1")
b=float(input("Digite o seu genêro:"))
c=float(input("Digite o preço do produto:R$"))
desconto_fem=c-(c/100*13)
desconto_mas=c-(c/100*5)
if b==1:
    print("Você participa da promoção e teve um desconto de 13%. Assim o seu produto que custaria R$ {:.2f} e agora caiu para R$ {:.2f}".format(c,desconto_fem))
else:
    print("Você tem um desconto especial de 5% logo sua compra de R$ {:.2f} será de R$ {:.2f}".format(c,desconto_mas))
