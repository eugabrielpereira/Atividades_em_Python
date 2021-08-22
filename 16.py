print("Iremos calcular a sua redução de vida")
a=float(input("Quantos cigarros você fuma por dia?"))
b=float(input("Quantos anos você fuma:"))
cigarros=a*10/60
anos=b*365
total=cigarros*anos
div=total/365
print("você perdeu {:.0f} dias de vida, O que totaliza {:.0f} anos".format(total,div))