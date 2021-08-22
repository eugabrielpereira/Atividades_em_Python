print("iremos calcular a sua corrida")
print("Nossas tarifas estão atualizadas para R$0,50 em viagens de até 200km e superiores R$0,45")
a=float(input("Digite quantos KM será a viajem:"))
curta=a*0.50
longa=a*0.45
if a<200:
    print("A sua viagem de {:.2f} km custará R${:.2f}".format(a,curta))
else:
    print("A sua viagem de {:.2f} km custará R${:.2f}".format(a,longa))