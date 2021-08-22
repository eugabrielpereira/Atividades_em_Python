a=input("Digite o nome do funcionário:")
b=float(input("Digite o salário atual do funcionário:"))
c=float(input("Quantos % será de aumento salárial?"))
aumento=b/100*c+b
print("O salário de {} era de R${:.2f} agora será de R${:.2f}".format(a,b,aumento))