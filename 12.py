a=float(input("Digite o valor do produto R$:"))
b=float(input("Digite quantos % de desconto será dado:"))
desconto=a-(a/100*b)
print("O valor total ficará em R${:.2f}".format(desconto))
