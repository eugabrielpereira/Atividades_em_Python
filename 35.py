print("iremos calcular a sua cobrança")
print("Tarifas são R$90,00 por dia para popular e R$150,00 para carros de grife.")
print("Considere outros custos:")
print("Carros populares, aluguel de R$90 por dia")
print("Até 100Km percorridos: R$0,20 por Km")
print("Acima de 100Km percorridos: R$0,10 por Km")
print("Carros de luxo = até 200km percorridos:R$0,60 por km e acima de 200km = R$0,25")
a=float(input("1=popular / 2=premium \/Digite a categoria do veiculo:"))
b=float(input("Quantos dias o veiculo foi alugado?"))
c=float(input("Quantos km foram rodados:"))
diap=b*90
dial=b*150
if a==1 and c<100:
    t=(c*0.20)+diap
    print("O seu custo ficou R${:.2f}".format(t))
    print("Veja as tarifas:Carro popular =R$90,00 dia = R${:.2f}".format(diap))
    print("Foram rodados {} KM no custo de R$0,20 por km".format(c))
if a==1 and c>100:
    to=(c*0.10)+diap
    print("O seu custo ficou em R${:.2f}".format(to))
    print("Veja as suas tarifas:Carro popular = R$90,00 dia =R${:.2f}".format(diap))
    print("Foram rodados {} KM no custo de R$0,10 ")
if a==2 and c<100:
    tot=(c*0.60)+dial
    print("O seu custo ficou em R${:.2f}".format(tot))
    print("Veja as suas tarifas:Carro premium= R$150,00 dia = R${:.2f}".format(dial))
    print("Foram rodados {}km no custo de R$0,60".format(c))
if a==2 and c>100:
    tota=(c*0.25)+dial
    print("O seu custo ficou em R${:.2f}".format(tota))
    print("Veja as suas tarifas:Carro premium= R$150,00 dia = R${:.2f}".format(dial))
    print("Foram rodados {}km no custo de R$0,25".format(c))

